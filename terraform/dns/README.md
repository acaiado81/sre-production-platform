# DNS and TLS Module

This module provisions HTTPS for the SRE Production Platform using:
- AWS Certificate Manager (ACM)
- Route53 DNS validation

## Flow
User → HTTPS → ALB → Ingress → Service → Pods

## Notes
- Certificates are validated automatically via DNS
- ALB terminates TLS
- Supports future multi-domain expansion
