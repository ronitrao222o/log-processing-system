from parser import parse_logs
from aggregator import aggregate_logs
from database import store_metrics

LOG_FILE = "logs/app.log"

def run_pipeline():
    parsed_logs = parse_logs(LOG_FILE)
    metrics = aggregate_logs(parsed_logs)
    store_metrics(metrics)
    print("Log processing pipeline completed successfully.")

if __name__ == "__main__":
    run_pipeline()
