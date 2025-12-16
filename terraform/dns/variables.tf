variable "domain_name" {
  description = "Root domain name (e.g. example.com)"
  type        = string
}

variable "hosted_zone_id" {
  description = "Route53 hosted zone ID"
  type        = string
}
