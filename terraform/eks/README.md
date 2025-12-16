# EKS Module

This module provisions the compute layer for the SRE Production Platform using Amazon EKS.

## Resources Created
- EKS control plane
- Managed node group
- IAM roles and policies
- Private subnet placement for worker nodes

## Design Decisions
- Worker nodes run in private subnets
- Managed node groups for simplified operations
- IAM roles separated for control plane and nodes

## How to Apply
```bash
terraform init
terraform plan
terraform apply
```

## Notes
- AWS credentials must be configured
- kubectl access will be configured after cluster creation
