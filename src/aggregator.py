import logging
from collections import defaultdict


def aggregate_logs(parsed_logs):
    logging.info("Starting log aggregation")

    metrics = {
        "total_requests": 0,
        "error_count": 0,
        "latencies": [],
        "endpoint_stats": defaultdict(lambda: {"count": 0, "total_latency": 0})
    }

    for log in parsed_logs:
        metrics["total_requests"] += 1

        if log["level"] == "ERROR":
            metrics["error_count"] += 1

        endpoint = log["endpoint"]
        latency = log["latency"]

        metrics["endpoint_stats"][endpoint]["count"] += 1
        metrics["endpoint_stats"][endpoint]["total_latency"] += latency
        metrics["latencies"].append(latency)

    # Calculate error rate
    error_rate = 0.0
    if metrics["total_requests"] > 0:
        error_rate = metrics["error_count"] / metrics["total_requests"]

    metrics["error_rate"] = round(error_rate, 4)

    # Calculate p95 latency
    p95_latency = 0
    if metrics["latencies"]:
        sorted_latencies = sorted(metrics["latencies"])
        index = int(0.95 * len(sorted_latencies)) - 1
        index = max(index, 0)
        p95_latency = sorted_latencies[index]

    metrics["p95_latency"] = p95_latency

    # Remove raw latency list before returning
    del metrics["latencies"]

    logging.info("Log aggregation completed")
    return metrics
