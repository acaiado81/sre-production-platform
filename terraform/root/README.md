# Root Terraform Module

This is the root Terraform configuration for the SRE Production Platform.

## What This Does
- Provisions AWS networking (VPC, subnets, routing)
- Provisions an EKS cluster and managed node groups
- Uses remote state with locking for safe collaboration

## State Management
Terraform state is stored remotely in:
- S3 (state storage)
- DynamoDB (state locking)

## How to Apply
```bash
terraform init
terraform plan
terraform apply
