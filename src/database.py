import sqlite3
from datetime import datetime

def store_metrics(metrics, db_path="metrics.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.executescript(open("schema.sql").read())

    for endpoint, data in metrics["endpoint_stats"].items():
        avg_latency = data["total_latency"] / data["count"]

        cursor.execute("""
            INSERT OR REPLACE INTO endpoint_metrics
            (endpoint, request_count, avg_latency)
            VALUES (?, ?, ?)
        """, (endpoint, data["count"], avg_latency))

    cursor.execute("""
        INSERT INTO system_metrics
        (total_requests, error_count, processed_at)
        VALUES (?, ?, ?)
    """, (
        metrics["total_requests"],
        metrics["error_count"],
        datetime.now()
    ))

    conn.commit()
    conn.close()
