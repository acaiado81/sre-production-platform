provider "aws" {
  region = var.aws_region
}

module "ecr" {
  source = "../ecr"
}

module "vpc" {
  source = "../vpc"

  aws_region           = var.aws_region
  vpc_cidr             = "10.0.0.0/16"
  public_subnet_cidrs  = ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnet_cidrs = ["10.0.101.0/24", "10.0.102.0/24"]
}

module "eks" {
  source = "../eks"

  aws_region         = var.aws_region
  cluster_name       = var.cluster_name
  vpc_id             = module.vpc.vpc_id
  private_subnet_ids = module.vpc.private_subnet_ids
}
