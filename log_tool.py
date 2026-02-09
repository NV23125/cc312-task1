import argparse
from datetime import datetime

def is_valid_log(line):
    """Check if a log line is valid."""
    parts = [p.strip() for p in line.strip().split('|')]
    
    # Must have exactly 4 fields
    if len(parts) != 4:
        return False
    
    # Level must be INFO, WARN, or ERROR (case-insensitive)
    level = parts[1].upper()
    if level not in ['INFO', 'WARN', 'ERROR']:
        return False
    
    return True

def parse_log_line(line):
    """Parse a valid log line into components."""
    parts = [p.strip() for p in line.strip().split('|')]
    return {
        'timestamp': parts[0],
        'level': parts[1].upper(),
        'service': parts[2],
        'message': parts[3]
    }

def log_run_to_proof(command, valid_count, written_count, output_file):
    """Append run details to run_proof.txt"""
    try:
        # Read existing content to count runs
        try:
            with open('run_proof.txt', 'r') as f:
                content = f.read()
                run_number = content.count('RUN ') + 1
        except FileNotFoundError:
            run_number = 1
        
        # Append to run_proof.txt (commands + outputs)
        with open('run_proof.txt', 'a') as f:
            if run_number > 1:
                f.write('\n')
            f.write(f"RUN {run_number}:\n")
            f.write(f"Command: {command}\n")
            f.write(f"Terminal Output:\n")
            f.write(f"Valid lines scanned: {valid_count}\n")
            f.write(f"Lines written: {written_count}\n")
            f.write(f"Output file: {output_file}\n")
            f.write('=' * 60 + '\n')
        
        # Append to run_history.txt (detailed log with timestamps)
        with open('run_history.txt', 'a') as f:
            if run_number > 1:
                f.write('\n')
            f.write(f"{'='*60}\n")
            f.write(f"RUN {run_number}\n")
            f.write(f"{'='*60}\n")
            f.write(f"Timestamp:    {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Command:      {command}\n")
            f.write(f"\nResults:\n")
            f.write(f"  - Valid lines scanned: {valid_count}\n")
            f.write(f"  - Lines written:       {written_count}\n")
            f.write(f"  - Output file:         {output_file}\n")
            f.write(f"\nFilters Applied:\n")
            if '--level' in command:
                level = command.split('--level')[1].split()[0]
                f.write(f"  - Level: {level}\n")
            else:
                f.write(f"  - Level: None\n")
            if '--service' in command:
                service = command.split('--service')[1].split()[0]
                f.write(f"  - Service: {service}\n")
            else:
                f.write(f"  - Service: None\n")
            f.write(f"\n")
            
    except Exception as e:
        pass

def main():
    parser = argparse.ArgumentParser(description='Filter cloud logs')
    parser.add_argument('--level', type=str, help='Filter by log level (INFO, WARN, ERROR)')
    parser.add_argument('--service', type=str, help='Filter by service name')
    parser.add_argument('--out', type=str, default='filtered_logs.txt', help='Output filename')
    
    args = parser.parse_args()
    
    command = 'python log_tool.py'
    if args.level:
        command += f' --level {args.level}'
    if args.service:
        command += f' --service {args.service}'
    if args.out != 'filtered_logs.txt':
        command += f' --out {args.out}'
    
    if args.level:
        args.level = args.level.upper()
    
    valid_count = 0
    filtered_logs = []
    
    with open('logs.txt', 'r') as f:
        for line in f:
            if not is_valid_log(line):
                continue
            
            valid_count += 1
            log = parse_log_line(line)
            
            if args.level and log['level'] != args.level:
                continue
            
            if args.service and log['service'] != args.service:
                continue
            
            filtered_logs.append(log)
    
    with open(args.out, 'w') as f:
        for log in filtered_logs:
            f.write(f"{log['timestamp']} | {log['level']} | {log['service']} | {log['message']}\n")
    
    print(f"Valid lines scanned: {valid_count}")
    print(f"Lines written: {len(filtered_logs)}")
    print(f"Output file: {args.out}")
    
    log_run_to_proof(command, valid_count, len(filtered_logs), args.out)

if __name__ == '__main__':
    main()