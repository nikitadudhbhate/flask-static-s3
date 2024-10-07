# Automated Deployment of a Python-based Static Website to AWS S3 using Docker and GitHub Actions

This project demonstrates how to build a Python-based static website generator using Flask and Jinja2, package it with Docker, and automate the deployment process to AWS S3 using GitHub Actions.

## Prerequisites

Before starting, ensure you have the following:

- **AWS Account**: You need an AWS account with an S3 bucket to host the static website.
- **AWS CLI**: Installed and configured with access to AWS S3.
- **GitHub Repository**: Your static website generator hosted in a GitHub repository.
- **Docker Installed**: Docker installed on your local machine to build and run the website container.
- **GitHub Secrets**: Configure these secrets in your GitHub repository:
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`
  - `AWS_REGION`
  - `AWS_S3_BUCKET_NAME`

---

## Step-by-Step Deployment Guide

### Step 1: Write a Python Static Site Generator
### Step 2: Create a Dockerfile
- Create a Dockerfile to package your static site generator:

### Step 3: Push the Docker Image to AWS S3
Create an S3 Bucket:
- In your AWS account, create an S3 bucket that will host your static website.
- Build and Push the Static Files:
Use GitHub Actions to build the Docker container, generate the static website files, and upload them to your S3 bucket.

### Step 4: Automate Deployment with GitHub Actions
- Create a .github/workflows/deploy.yml file to define the GitHub Actions workflow. This file will automate the Docker build, static file generation, and upload to AWS S3.

### Step 5: Verify Deployment
- S3 Website Hosting:
In the AWS S3 console, enable static website hosting for your S3 bucket.
Specify the index.html file as the entry point for your website.
Access the Website:

Once deployed, access the static website using the S3 bucket’s URL.

## Conclusion

- You have successfully automated the deployment of a Python-based static website generator to AWS S3 using Docker and GitHub Actions. This setup simplifies the CI/CD process, allowing you to focus on building your site while automating the deployment.
