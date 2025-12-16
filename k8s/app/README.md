# Kubernetes Application Manifests

This directory contains Kubernetes manifests for deploying the SRE Production Platform application.

## Resources
- Deployment (FastAPI application)
- ClusterIP Service

## Features
- Health checks via `/health`
- Resource requests and limits
- Horizontal scaling ready

## Apply
```bash
kubectl apply -f .
