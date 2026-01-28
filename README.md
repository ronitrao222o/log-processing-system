# Log Processing & Analytics System

## Overview
This project implements a batch log processing system that parses application logs,
aggregates system-level and endpoint-level metrics, and stores results in a relational database.

## Architecture
- Parser: Converts raw log lines into structured records
- Aggregator: Computes request counts, error rates, and latency metrics
- Storage: Persists aggregated metrics using SQLite

## How to Run
```bash
python src/pipeline.py
