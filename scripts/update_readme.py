"""
update_readme.py
-----------------
Scans every problem note (*.md with YAML frontmatter) in the topic folders,
aggregates stats, and rewrites README.md between the
<!-- DASHBOARD:START --> and <!-- DASHBOARD:END --> markers.

Requires: pyyaml   (pip install pyyaml)
"""

import os
import re
import datetime
import yaml

# ----------------------------------------------------------------------
# CONFIG — edit these to match your goals
# ----------------------------------------------------------------------

# Folder name -> target number of problems (used for progress bars)
TOPIC_TOTALS = {
    "Arrays": 40,
    "Sorting": 15,
    "Hashing": 15,
    "Strings": 20,
    "Linked_List": 18,
    "Stack_Queue": 12,
    "Trees": 39,
    "BST": 12,
    "Graphs": 20,
    "DP": 27,
}

# Folders the script should never treat as "topic" folders
IGNORE_DIRS = {".git", ".github", "scripts", "Resources", "node_modules"}

# Fixed list of patterns you're tracking (checked off automatically)
ALL_PATTERNS = [
    "Binary Search",
    "Two Pointers",
    "Sliding Window",
    "Prefix Sum",
    "Greedy",
    "DFS",
    "BFS",
    "Union Find",
]

README_PATH = "README.md"
START_MARKER = "<!-- DASHBOARD:START -->"
END_MARKER = "<!-- DASHBOARD:END -->"

# ----------------------------------------------------------------------
# Encoding-safe file reading
# ----------------------------------------------------------------------
# Some editors (Notepad on Windows especially) save .md files as
# UTF-16 instead of UTF-8, which makes plain open(path).read() crash.
# This tries the common encodings in order until one works, so a
# mis-saved file never breaks the whole Action run.

ENCODINGS_TO_TRY = ["utf-8", "utf-8-sig", "utf-16", "cp1252"]


def safe_read(path):
    for enc in ENCODINGS_TO_TRY:
        try:
            with open(path, "r", encoding=enc) as f:
                return f.read()
        except (UnicodeError, UnicodeDecodeError):
            continue
    # Last resort: read raw bytes and drop anything that can't decode,
    # so the run still succeeds instead of crashing.
    with open(path, "rb") as f:
        raw = f.read()
    print(f"⚠️  Warning: {path} has an unusual encoding, some characters may be dropped.")
    return raw.decode("utf-8", errors="ignore")


# ----------------------------------------------------------------------
# STEP 1 — Collect every note's frontmatter
# ----------------------------------------------------------------------

def parse_frontmatter(text):
    """Returns (meta_dict, body). meta_dict is {} if no frontmatter found."""
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    try:
        meta = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        meta = {}
    return meta, parts[2]


def collect_notes(root="."):
    notes = []
    for topic in sorted(os.listdir(root)):
        topic_path = os.path.join(root, topic)
        if not os.path.isdir(topic_path) or topic in IGNORE_DIRS:
            continue
        for fname in sorted(os.listdir(topic_path)):
            if not fname.endswith(".md") or fname.upper() == "README.MD":
                continue
            fpath = os.path.join(topic_path, fname)
            text = safe_read(fpath)
            meta, _ = parse_frontmatter(text)
            if not meta:
                # No frontmatter yet — still count it under its folder
                meta = {"topic": topic, "title": fname.replace(".md", "")}
            meta.setdefault("topic", topic)
            meta.setdefault("title", fname.replace(".md", ""))
            notes.append(meta)
    return notes


# ----------------------------------------------------------------------
# STEP 2 — Build stats from the collected notes
# ----------------------------------------------------------------------

def make_bar(solved, total, width=20):
    if total == 0:
        return "░" * width + " 0%"
    pct = min(solved / total, 1.0)
    filled = round(pct * width)
    return "█" * filled + "░" * (width - filled) + f" {round(pct * 100)}%"


def compute_streak(dates):
    """dates: list of datetime.date objects (may have duplicates)."""
    if not dates:
        return 0
    unique_dates = sorted(set(dates), reverse=True)
    today = datetime.date.today()
    # streak only counts if the most recent date is today or yesterday
    if (today - unique_dates[0]).days > 1:
        return 0
    streak = 1
    for i in range(1, len(unique_dates)):
        gap = (unique_dates[i - 1] - unique_dates[i]).days
        if gap == 1:
            streak += 1
        else:
            break
    return streak


def build_dashboard(notes):
    topic_counts = {t: 0 for t in TOPIC_TOTALS}
    difficulty_counts = {"Easy": 0, "Medium": 0, "Hard": 0}
    patterns_found = set()
    dates = []
    latest = None  # (date, title)

    for n in notes:
        topic = n.get("topic")
        if topic in topic_counts:
            topic_counts[topic] += 1

        diff = n.get("difficulty")
        if diff in difficulty_counts:
            difficulty_counts[diff] += 1

        pattern = n.get("pattern")
        if pattern:
            patterns_found.add(pattern)

        raw_date = n.get("date")
        if raw_date:
            if isinstance(raw_date, datetime.date):
                d = raw_date
            else:
                try:
                    d = datetime.datetime.strptime(str(raw_date), "%Y-%m-%d").date()
                except ValueError:
                    d = None
            if d:
                dates.append(d)
                if latest is None or d >= latest[0]:
                    latest = (d, n.get("title", "Untitled"))

    total_solved = sum(topic_counts.values())
    total_target = sum(TOPIC_TOTALS.values())
    streak = compute_streak(dates)

    lines = []
    lines.append("## 📊 Progress\n")
    for topic, total in TOPIC_TOTALS.items():
        solved = topic_counts[topic]
        lines.append(f"**{topic.replace('_', ' ')}** — {solved} / {total}")
        lines.append(f"`{make_bar(solved, total)}`\n")

    lines.append("---\n")
    lines.append("## 🎯 Overall Progress\n")
    lines.append(f"**{total_solved} / {total_target} problems solved**\n")
    lines.append(f"`{make_bar(total_solved, total_target, width=30)}`\n")

    lines.append("---\n")
    lines.append("## 🔥 Current Streak\n")
    lines.append(f"**{streak} day{'s' if streak != 1 else ''}**\n")

    lines.append("---\n")
    lines.append("## 🧠 Patterns Learned\n")
    for p in ALL_PATTERNS:
        mark = "✅" if p in patterns_found else "⬜"
        lines.append(f"- {mark} {p}")
    lines.append("")

    lines.append("---\n")
    lines.append("## 📈 Difficulty Breakdown\n")
    for level in ["Easy", "Medium", "Hard"]:
        lines.append(f"{level}: `{make_bar(difficulty_counts[level], max(total_solved,1), width=15)}` ({difficulty_counts[level]})")
    lines.append("")

    lines.append("---\n")
    lines.append("## 📅 Latest Problem\n")
    if latest:
        lines.append(f"✅ **{latest[1]}** ({latest[0].isoformat()})\n")
    else:
        lines.append("No problems logged yet.\n")

    lines.append("---\n")
    lines.append(f"*Last updated automatically: {datetime.date.today().isoformat()}*")

    return "\n".join(lines)


# ----------------------------------------------------------------------
# STEP 3 — Inject into README.md between markers
# ----------------------------------------------------------------------

def update_readme(dashboard_text):
    if not os.path.exists(README_PATH):
        content = f"# 🚀 FAANG DSA Journey\n\n{START_MARKER}\n{END_MARKER}\n"
    else:
        content = safe_read(README_PATH)

    if START_MARKER not in content or END_MARKER not in content:
        # Markers missing — append a dashboard section at the end
        content = content.rstrip() + f"\n\n{START_MARKER}\n{END_MARKER}\n"

    pattern = re.compile(
        re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
        re.DOTALL,
    )
    replacement = f"{START_MARKER}\n\n{dashboard_text}\n\n{END_MARKER}"
    new_content = pattern.sub(replacement, content)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)


def main():
    notes = collect_notes(".")
    dashboard = build_dashboard(notes)
    update_readme(dashboard)
    print(f"README updated. {len(notes)} notes scanned.")


if __name__ == "__main__":
    main()