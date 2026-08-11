# sre-platform

A full-stack SRE monitoring and incident response platform — built from scratch.

## Architecture

| Layer | Component | Purpose |
|---|---|---|
| 1 | `agents/` | Metric collection — CPU, memory, disk, network |
| 2 | `pipeline/` | Log aggregation and processing |
| 3 | `aws/` | Cloud storage, DynamoDB, CloudWatch integration |
| 4 | `terraform/` | Infrastructure as Code for all AWS resources |
| 5 | `ci/` | GitHub Actions — automated testing and deployment |

## Status

🔨 Active development

## Tech Stack

Python · Bash · AWS (S3, DynamoDB, CloudWatch) · Terraform · GitHub Actions
