from collections import defaultdict

def aggregate_logs(parsed_logs):
    metrics = {
        "total_requests": 0,
        "error_count": 0,
        "endpoint_stats": defaultdict(lambda: {"count": 0, "total_latency": 0})
    }

    for log in parsed_logs:
        metrics["total_requests"] += 1

        if log["level"] == "ERROR":
            metrics["error_count"] += 1

        endpoint = log["endpoint"]
        metrics["endpoint_stats"][endpoint]["count"] += 1
        metrics["endpoint_stats"][endpoint]["total_latency"] += log["latency"]

    return metrics
