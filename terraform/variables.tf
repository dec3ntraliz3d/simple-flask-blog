variable "instance_type" {
  description = "The instance type for the EC2 instance"
  type        = string
  default     = "t2.micro"
}

variable "public_key" {
  description = "The public key for the EC2 instance"
  type        = string
}

