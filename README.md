# SRE Production Platform

![CI](https://github.com/acaiado81/sre-production-platform/actions/workflows/ci.yml/badge.svg)

## Overview

A production-grade SRE / Platform Engineering project demonstrating:

- Containerized FastAPI application
- AWS EKS with Terraform (VPC, Subnets, IAM, Node Groups)
- CI/CD via GitHub Actions
- Kubernetes Deployment, Service, Ingress with ALB
- TLS with ACM and Route53 DNS
- Infrastructure as Code best practices

## Architecture

![Architecture Diagram](diagrams/architecture.png)

- Internet → ALB (HTTPS) → Ingress → Service → Pods → VPC → EKS

## Repository Structure

- terraform/ # Infrastructure as Code
- app/ # Python service
- k8s/ # Kubernetes manifests
- ci/ # CI/CD pipelines
- observability/ # Dashboards and alerts
- chaos/ # Failure injection experiments
- tools/ # SRE automation tooling
- postmortems/ # Incident reports
- diagrams/ # Architecture diagrams

## Current Status

- Project under active development

## Features

- Modular Terraform
- Secure CI/CD with OIDC
- Dockerized application
- High availability EKS cluster
- Health probes & resource limits in Kubernetes
- HTTPS via ACM + Route53
- Automated ECR image scanning & lifecycle

## Planned Features
- Highly available Kubernetes deployment
- CI/CD with automated rollback
- Prometheus/Grafana observability
- SLOs with error budgets
- Chaos testing and postmortems
- Python tooling for reliability reporting

## Getting Started

Add instructions for **someone to clone and explore**, e.g.:

```bash
git clone https://github.com/acaiado81/sre-production-platform.git
cd sre-production-platform
```
- Terraform: ```bash terraform init && terraform validate```
- Kubernetes (requires cluster): ```bash kubectl apply -f k8s/app```
- CI/CD: GitHub Actions runs on push to main
