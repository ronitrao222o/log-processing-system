CREATE TABLE IF NOT EXISTS endpoint_metrics (
    endpoint TEXT PRIMARY KEY,
    request_count INTEGER,
    avg_latency REAL
);

CREATE TABLE IF NOT EXISTS system_metrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    total_requests INTEGER,
    error_count INTEGER,
    processed_at TIMESTAMP
);
