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
    line = line.strip()
    if not line:
        return None
    
    parts = [part.strip() for part in line.split('|')]
    
    if len(parts) != 4:
        return None
    
    return tuple(parts)


def normalize_level(level: str) -> str:
    # TODO 2: return uppercase level
    return level.upper()


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
    with open(LOG_FILE, 'r', encoding='utf-8') as file:
        for line in file:
            # - total_lines += 1
            total_lines += 1
            
            # - parsed = parse_line(line)
            parsed = parse_line(line)
            
            # - if parsed is None: invalid_lines += 1; continue
            if parsed is None:
                invalid_lines += 1
                continue
            
            # Extract the parts
            timestamp, level, service, message = parsed
            
            # - normalize level
            level = normalize_level(level)
            
            # - if level NOT in ALLOWED_LEVELS: invalid_lines += 1; continue
            if level not in ALLOWED_LEVELS:
                invalid_lines += 1
                continue
            
            # - now it's valid:
            #   valid_lines += 1
            valid_lines += 1
            
            #   level_counts[level] += 1
            level_counts[level] += 1
            
            #   service_counter[service] += 1
            service_counter[service] += 1
            
            #   if level == "ERROR": error_message_counter[message] += 1
            if level == "ERROR":
                error_message_counter[message] += 1
            
            #   also store the ORIGINAL cleaned-format line into clean_lines
            # Cleaned-format line should look exactly like:
            # timestamp | LEVEL | service | message
            # (LEVEL must be uppercase)
            clean_line = f"{timestamp} | {level} | {service} | {message}"
            clean_lines.append(clean_line)

    # TODO 4: Write clean_lines into clean_logs.txt (one per line)
    with open(CLEAN_FILE, 'w', encoding='utf-8') as file:
        for clean_line in clean_lines:
            file.write(clean_line + '\n')

    # TODO 5: Build the summary dictionary with this exact structure:
    # {
    #   "total_lines": ...,
    #   "valid_lines": ...,
    #   "invalid_lines": ...,
    #   "levels": {"INFO":..., "WARN":..., "ERROR":...},
    #   "top_services": [{"service":..., "count":...}, ... up to 3],
    #   "top_errors": [{"message":..., "count":...}, ... up to 3]
    # }
    
    # Get top 3 services
    top_services = [
        {"service": service, "count": count}
        for service, count in service_counter.most_common(3)
    ]
    
    # Get top 3 error messages
    top_errors = [
        {"message": message, "count": count}
        for message, count in error_message_counter.most_common(3)
    ]
    
    summary = {
        "total_lines": total_lines,
        "valid_lines": valid_lines,
        "invalid_lines": invalid_lines,
        "levels": level_counts,
        "top_services": top_services,
        "top_errors": top_errors
    }

    # TODO 6: Save summary.json using json.dump(..., indent=2)
    with open(SUMMARY_FILE, 'w', encoding='utf-8') as file:
        json.dump(summary, file, indent=2)

    # Optional self-check prints (you can keep them):
    print(f"Valid: {valid_lines}, Invalid: {invalid_lines}")
    print(f"Clean logs saved to {CLEAN_FILE}")
    print(f"Summary saved to {SUMMARY_FILE}")


if __name__ == "__main__":
    main()
