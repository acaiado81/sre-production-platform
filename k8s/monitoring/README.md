# Monitoring

This directory contains Kubernetes observability resources for the
SRE Production Platform.

## Components
- Prometheus ServiceMonitor for application metrics
- Designed for Prometheus Operator / kube-prometheus-stack
- Metrics exposed via FastAPI `/metrics` endpoint

## Metrics Collected
- Request count by endpoint
- Request latency (p95, p99)
- Error rate (5xx)

## Notes
These resources are designed for production environments and may
require an existing Prometheus Operator installation.
