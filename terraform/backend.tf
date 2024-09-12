# Use dynamodb for locking
terraform {
  backend "s3" {
    bucket = "codebuff-terraform-state-bucket"
    key    = "terraform/terraform.tfstate"
    region = "us-east-1"
    dynamodb_table = "terraform-lock"

  }
}

# Create a  bucket for the terraform state
resource "aws_s3_bucket" "terraform_state" {
  bucket = "codebuff-terraform-state-bucket"
}

# Create a dynamodb table for locking
resource "aws_dynamodb_table" "terraform_lock" {
  name     = "terraform-lock"
  hash_key = "LockID"
  billing_mode = "PAY_PER_REQUEST"
  attribute {
    name = "LockID"
    type = "S"
  }
}