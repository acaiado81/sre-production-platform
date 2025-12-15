# VPC Module

This Terraform module provisions the base AWS networking layer for the SRE Production Platform.

## Resources Created
- VPC with DNS support
- Public and private subnets across multiple AZs
- Internet Gateway
- NAT Gateway for outbound private subnet access
- Route tables and associations

## Design Decisions
- Private workloads do not have public IPs
- NAT Gateway enables controlled outbound access
- Multi-AZ for high availability

## How to Apply
```bash
terraform init
terraform plan
terraform apply
