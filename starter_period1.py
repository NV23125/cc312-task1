"""
PL202 - Day 1 (Period 1) Starter File
Task: Cloud Log Reader – Parse + Validate + Report (TXT)

You will:
1) Read logs.txt
2) Parse each line into: timestamp | level | service | message
3) Validate:
   - If a line does NOT have exactly 4 parts => invalid line
   - Normalize level to uppercase
   - Allowed levels: INFO, WARN, ERROR
   - Anything else => INVALID_LEVEL
4) Count totals and save the summary to period1_report.txt

IMPORTANT:
- Work independently (no teacher / classmates).
- Only fill the TODO parts. Do not delete other code.
"""

from pathlib import Path

LOG_FILE = Path("logs.txt")
OUTPUT_REPORT = Path("period1_report.txt")

ALLOWED_LEVELS = {"INFO", "WARN", "ERROR"}


def parse_line(line: str):
    """
    Parse a single log line.
    Returns a tuple: (timestamp, level, service, message) OR None if format is invalid.

    Expected format:
    timestamp | level | service | message
    """
    # TODO 1: strip whitespace and ignore empty lines (treat empty as invalid)
    line = line.strip()
    if not line:
        return None
    
    # TODO 2: split by '|' and trim whitespace around each part
    parts = [part.strip() for part in line.split('|')]
    
    # TODO 3: if you do NOT have exactly 4 parts, return None
    if len(parts) != 4:
        return None
    
    # TODO 4: return the 4 parts (timestamp, level, service, message)
    return tuple(parts)


def normalize_level(level: str) -> str:
    """Normalize log level to uppercase."""
    # TODO 5: return level in uppercase (hint: .upper())
    return level.upper()


def main():
    # Counters
    total_lines = 0
    invalid_lines = 0

    level_counts = {
        "INFO": 0,
        "WARN": 0,
        "ERROR": 0,
        "INVALID_LEVEL": 0,
    }

    # Safety check
    if not LOG_FILE.exists():
        print(f"ERROR: Could not find {LOG_FILE}. Make sure logs.txt is in the same folder.")
        return

    # TODO 6: open logs.txt and loop through each line
    with open(LOG_FILE, 'r', encoding='utf-8') as file:
        for line in file:
            # - increase total_lines
            total_lines += 1
            
            # - parse the line using parse_line()
            parsed = parse_line(line)
            
            # - if parse_line() returns None -> invalid_lines += 1 and continue
            if parsed is None:
                invalid_lines += 1
                continue
            
            # Extract the parts
            timestamp, level, service, message = parsed
            
            # - normalize the level
            level = normalize_level(level)
            
            # - if level in ALLOWED_LEVELS -> level_counts[level] += 1
            # - else -> level_counts["INVALID_LEVEL"] += 1
            if level in ALLOWED_LEVELS:
                level_counts[level] += 1
            else:
                level_counts["INVALID_LEVEL"] += 1

    # TODO 7: Create a summary string (multi-line) with:
    # Total lines, Invalid lines, INFO, WARN, ERROR, INVALID_LEVEL
    summary = f"""Cloud Log Analysis Report
==========================
Total lines: {total_lines}
Invalid lines: {invalid_lines}

Log Level Counts:
INFO: {level_counts['INFO']}
WARN: {level_counts['WARN']}
ERROR: {level_counts['ERROR']}
INVALID_LEVEL: {level_counts['INVALID_LEVEL']}
"""

    # TODO 8: Print the summary
    print(summary)

    # TODO 9: Save the summary into period1_report.txt
    with open(OUTPUT_REPORT, 'w', encoding='utf-8') as file:
        file.write(summary)
    
    print(f"\nReport saved to {OUTPUT_REPORT}")


if __name__ == "__main__":
    main()

