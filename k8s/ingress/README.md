# Ingress Configuration

This directory defines external access to the SRE Production Platform using
the AWS Load Balancer Controller.

## Traffic Flow
Internet → AWS ALB → Kubernetes Ingress → Service → Pods

## Notes
- Uses ALB in internet-facing mode
- TLS/HTTPS added in a later stage
- DNS integration via Route53 planned
