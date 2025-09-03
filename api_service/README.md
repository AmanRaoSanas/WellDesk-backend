# WellDesk Backend Service

## Overview

WellDesk backend is a serverless FastAPI application built to support the WellDesk desktop app. It provides APIs for uploading daily user activity Excel files and stores them securely in AWS S3. The service is deployed on AWS Lambda using Infrastructure as Code (CloudFormation) and automated via GitHub Actions with OIDC-based authentication.

---

## Project Features

* **FastAPI backend** running on AWS Lambda
* API endpoint to upload Excel files (`POST /upload`)
* Root welcome endpoint (`GET /`)
* Stores uploaded files on AWS S3 bucket
* Uses IAM Roles with OIDC for secure, keyless CI/CD
* Infrastructure managed via CloudFormation
* CI/CD pipeline with GitHub Actions triggers on `main` branch pushes

---

## Repository Structure

```
welldesk/
├── api-service/
│   ├── main.py                   # FastAPI app entrypoint
│   ├── config.py                 # Environment config loader
│   ├── s3_utils.py               # S3 upload helper
│   ├── requirements.txt          # Python dependencies
│   ├── deploy.yaml               # CloudFormation template for infra
│   └── .env                      # Local env vars (for dev only)
│
├── .github/
│   └── workflows/
│       └── deploy.yml            # GitHub Actions CI/CD pipeline
```

---

## Configuration

* `.env` file (local development only):

```env
AWS_REGION=ap-south-1
S3_BUCKET_NAME=welldesk-user-data
```

* On AWS Lambda, these are configured via environment variables in CloudFormation.

---

## How It Works

* User uploads Excel files from desktop app via `POST /upload`
* Backend accepts multipart file upload, saves temporarily
* Uploads file to configured S3 bucket under `uploads/` prefix
* Returns JSON with upload status and file info
* Root route (`GET /`) returns a welcome message

---

## Deployment

* Infrastructure and Lambda deployed using CloudFormation (`deploy.yaml`)
* CI/CD automated with GitHub Actions (`deploy.yml`) triggered on push to `main`
* Uses OIDC to securely assume IAM Role without static AWS keys

---

## IAM & Security

* IAM Role created with S3 and Lambda permissions
* Trust relationship allows GitHub OIDC provider
* No long-term access keys used, enhancing security
* GitHub Secrets store IAM Role ARN (`AWS_OIDC_ROLE_ARN`)

---

## Next Steps

* Implement DynamoDB metadata storage for uploads
* Build ETL processing service (`cloud-etl/`)
* Add reporting API for user downloads
* Expand CI/CD workflows for ETL deployment

---

## Local Development

1. Create `.env` with required environment variables
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the FastAPI app locally:

```bash
uvicorn main:app --reload
```

4. Test endpoints via Swagger UI at `http://localhost:8000/docs`

---

## Contact

For questions or contributions, reach out to the WellDesk backend team.
Amanraosanas17@gmail.com
---
