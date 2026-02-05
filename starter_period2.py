"""
PL202 - Day 1 (Period 2) Starter File
Task: Cloud Log Cleaner + JSON Summary (Mini Project)

You will:
1) Read logs.txt
2) Keep ONLY valid lines (4 parts AND level is INFO/WARN/ERROR)
3) Write clean logs to clean_logs.txt (same original format)
4) Create summary.json with:
   - total_lines, valid_lines, invalid_lines
   - levels: counts of INFO/WARN/ERROR (valid only)
   - top_services: top 3 services by valid log count
   - top_errors: top 3 ERROR messages by count (valid ERROR only)

IMPORTANT:
- Work independently (no teacher / classmates).
- You may copy your solutions from Period 1.
"""

import json
from pathlib import Path
from collections import Counter

LOG_FILE = Path("logs.txt")
CLEAN_FILE = Path("clean_logs.txt")
SUMMARY_FILE = Path("summary.json")

ALLOWED_LEVELS = {"INFO", "WARN", "ERROR"}


def parse_line(line: str):
    """
    Returns (timestamp, level, service, message) OR None if format invalid.
    """
    # TODO 1: Implement parse_line (same rules as Period 1)
    pass


def normalize_level(level: str) -> str:
    # TODO 2: return uppercase level
    pass


def main():
    if not LOG_FILE.exists():
        print(f"ERROR: Could not find {LOG_FILE}. Make sure logs.txt is in the same folder.")
        return

    total_lines = 0
    valid_lines = 0
    invalid_lines = 0

    level_counts = {"INFO": 0, "WARN": 0, "ERROR": 0}

    service_counter = Counter()
    error_message_counter = Counter()

    clean_lines = []  # store valid lines to write later

    # TODO 3: Read logs.txt line by line
    # For each line:
    #   - total_lines += 1
    #   - parsed = parse_line(line)
    #   - if parsed is None: invalid_lines += 1; continue
    #   - normalize level
    #   - if level NOT in ALLOWED_LEVELS: invalid_lines += 1; continue
    #   - now it's valid:
    #       valid_lines += 1
    #       level_counts[level] += 1
    #       service_counter[service] += 1
    #       if level == "ERROR": error_message_counter[message] += 1
    #       also store the ORIGINAL cleaned-format line into clean_lines
    #
    # Cleaned-format line should look exactly like:
    # timestamp | LEVEL | service | message
    #
    # (LEVEL must be uppercase)

    # TODO 4: Write clean_lines into clean_logs.txt (one per line)

    # TODO 5: Build the summary dictionary with this exact structure:
    # {
    #   "total_lines": ...,
    #   "valid_lines": ...,
    #   "invalid_lines": ...,
    #   "levels": {"INFO":..., "WARN":..., "ERROR":...},
    #   "top_services": [{"service":..., "count":...}, ... up to 3],
    #   "top_errors": [{"message":..., "count":...}, ... up to 3]
    # }

    # TODO 6: Save summary.json using json.dump(..., indent=2)

    # Optional self-check prints (you can keep them):
    # print("Valid:", valid_lines, "Invalid:", invalid_lines)
    pass


if __name__ == "__main__":
    main()
