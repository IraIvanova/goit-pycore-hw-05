import sys
import re
import collections

ERROR_LEVELS = ('INFO', 'DEBUG', 'WARNING', 'ERROR')


def load_logs(file_path: str) -> list:
    try:
        with open(file_path, "r") as fh:
            return list(filter(lambda l: l, [parse_log_line(line) for line in fh]))
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except OSError as e:
        print(f"Cannot read file: {e}")
        return []

def parse_log_line(line: str) -> dict:
    pattern = r'('+'|'.join(ERROR_LEVELS) + ')'
    result = re.split(pattern, line)

    if len(result) < 3:
        return {}

    date_and_time, level, msg = result
    log_date, log_time, _ = date_and_time.split(" ")

    return {'date': log_date, 'time': log_time, 'level': level, 'msg': msg.strip()}

def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log['level'] == level.upper(), logs))

def count_logs_by_level(logs: list) -> dict:
    return dict(collections.Counter(log['level'] for log in logs))

def display_log_counts(counts: dict):
    if not counts:
        return

    separator = ' | '
    headers = ['Рівень логування', 'Кількість']
    column_lengths = [16, 9]

    header_line = separator.join(
        f"{header:<{length}}" for header, length in zip(headers, column_lengths)
    )

    result = f"{header_line}\n{'-' * len(header_line)}\n"

    for level, count in counts.items():
        result += separator.join(
            f"{value:<{length}}" for value, length in zip([level, count], column_lengths)
        ) + '\n'

    print(result)

def display_detailed_info_by_level(logs: list, level: str):
    filtered_logs = filter_logs_by_level(logs, level)
    result = ''

    for log in filtered_logs:
        result += f"{log['date']} {log['time']} - {log['msg']}\n"

    print(result)

def main():
    log_file = sys.argv[1] if len(sys.argv) > 1 else None
    e_level = sys.argv[2] if len(sys.argv) > 2 else None

    if not log_file:
        print("Usage: python parser.py <log_file> [LEVEL]")
        sys.exit(1)

    if e_level and e_level.upper() not in ERROR_LEVELS:
        print(f"Invalid error level: {e_level.upper()}. Choose one of: {', '.join(ERROR_LEVELS)}.")
        sys.exit(1)

    loaded_logs = load_logs(log_file)
    display_log_counts(count_logs_by_level(loaded_logs))

    if e_level:
        display_detailed_info_by_level(loaded_logs, e_level)

if __name__ == "__main__":
    main()