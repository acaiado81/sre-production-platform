# Ingress Configuration

This directory defines external access to the SRE Production Platform using
the AWS Load Balancer Controller.

## Traffic Flow
Internet → AWS ALB → Kubernetes Ingress → Service → Pods

## AWS Load Balancer Controller Installation

```bash
helm repo add eks https://aws.github.io/eks-charts
helm repo update

helm install aws-load-balancer-controller eks/aws-load-balancer-controller \
  -n kube-system \
  --set clusterName=sre-platform-cluster \
  --set serviceAccount.create=false \
  --set serviceAccount.name=aws-load-balancer-controller
```

## Notes
- Uses ALB in internet-facing mode
- TLS/HTTPS added in a later stage
- DNS integration via Route53 planned
