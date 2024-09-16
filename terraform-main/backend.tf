
terraform {
  backend "s3" {
    bucket         = "codebuff-terraform-state-bucket"
    key            = "terraform/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-lock"

  }
}
