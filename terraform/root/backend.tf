terraform {
  required_version = ">= 1.5"

  backend "s3" {
    bucket         = "sre-platform-terraform-state"
    key            = "root/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "sre-platform-terraform-locks"
    encrypt        = true
  }
}
