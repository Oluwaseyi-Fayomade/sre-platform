provider "aws" {
  region = "us-east-1"
}

resource "aws_dynamodb_table" "anomalies" {
  name         = "sre-platform-anomalies"
  billing_mode = "PAY_PER_REQUEST"

  hash_key = "id"

  attribute {
    name = "id"
    type = "S"
  }

  tags = {
    Project     = "sre-platform"
    Environment = "training"
    Owner       = "oluwaseyi"
  }
}

resource "aws_s3_bucket" "reports" {
  bucket = "sre-platform-reports-oluwaseyi-2026"

  tags = {
    Project     = "sre-platform"
    Environment = "training"
    Owner       = "oluwaseyi"
  }
}

resource "aws_s3_bucket_versioning" "reports_versioning" {
  bucket = aws_s3_bucket.reports.id

  versioning_configuration {
    status = "Enabled"
  }
}