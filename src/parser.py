import logging
from datetime import datetime

def parse_log_line(line):
    parts = line.strip().split()

    return {
        "timestamp": datetime.strptime(parts[0] + " " + parts[1], "%Y-%m-%d %H:%M:%S"),
        "level": parts[2],
        "user_id": parts[3].split("=")[1],
        "endpoint": parts[4].split("=")[1],
        "latency": int(parts[5].split("=")[1])
    }

def parse_logs(file_path):
    parsed_logs = []

    with open(file_path, "r") as file:
        for line in file:
            try:
                parsed_logs.append(parse_log_line(line))
            except Exception as e:
                logging.warning(
                    f"Skipping malformed log line: {line.strip()} | Error: {e}"
                )
                continue

    return parsed_logs
