import logging
from parser import parse_logs
from aggregator import aggregate_logs
from database import store_metrics

LOG_FILE = "logs/app.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline():
    logging.info("Log processing pipeline started")

    logging.info("Parsing log file")
    parsed_logs = parse_logs(LOG_FILE)
    logging.info(f"Parsed {len(parsed_logs)} log entries")

    logging.info("Aggregating logs")
    metrics = aggregate_logs(parsed_logs)
    logging.info("Log aggregation completed")

    logging.info("Storing aggregated metrics")
    store_metrics(metrics)
    logging.info("Metrics stored successfully")

    logging.info("Log processing pipeline completed")

if __name__ == "__main__":
    logging.info("Starting log processing application")
    run_pipeline()
