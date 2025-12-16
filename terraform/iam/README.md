# IAM for AWS Load Balancer Controller

This module provisions IAM roles and policies required for the AWS Load
Balancer Controller using IAM Roles for Service Accounts (IRSA).

## Features
- OIDC-based authentication
- No static AWS credentials
- Scoped permissions for ALB management

## Notes
- Requires EKS OIDC provider
- Service account: kube-system/aws-load-balancer-controller
