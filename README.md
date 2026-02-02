# Log Processing & Analytics System

## Overview
This project implements a batch log processing system that parses application logs,
aggregates system-level and endpoint-level metrics, and stores results in a relational database.

## Architecture
- Parser: Converts raw log lines into structured records
- Aggregator: Computes request counts, error rates, and latency metrics
- Storage: Persists aggregated metrics using SQLite
- Graceful handling of malformed log entries without breaking the pipeline
- Structured logging added to monitor parsing, aggregation, and storage stages

## How to Run
```bash
python src/pipeline.py
