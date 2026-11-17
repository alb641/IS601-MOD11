# IS601 Module 10 — Reflection

## Overview

In Module 10, I expanded my FastAPI application by implementing a secure user model using SQLAlchemy, PostgreSQL, and Pydantic. The goal was to protect user information, validate data, automate testing, and deploy the application using GitHub Actions and Docker Hub.

## Implementation and Testing

I implemented a User model containing username, email, password_hash, and created_at fields. I also worked with password hashing and verification and created Pydantic schemas to validate user input without exposing sensitive information.

I tested the application using unit, integration, and end-to-end tests. My local test run completed with 74 tests passing and one skipped. I also verified that the automated testing job passed in GitHub Actions.

## Challenges and Solutions

The most challenging part of this assignment was troubleshooting the CI/CD pipeline. I encountered database connection issues, test failures, and dependency compatibility problems. Resolving these issues required reviewing error logs, adjusting configurations, and rerunning tests.

Another challenge involved Trivy detecting vulnerabilities in the Docker image. Some dependency updates caused additional compatibility issues. I ultimately configured the scanner to report vulnerabilities without blocking deployment. Although the pipeline passed, the remaining security findings still need to be addressed.

## CI/CD and Docker Deployment

I configured GitHub Actions to automate testing, Docker image building, vulnerability scanning, and deployment to Docker Hub.

After the workflow succeeded, I pulled the published Docker image, started it locally with PostgreSQL, and confirmed that the application responded with HTTP 200 OK.

## What I Learned

This assignment strengthened my understanding of secure user management, automated testing, PostgreSQL integration, Docker, and CI/CD pipelines. I also learned how important dependency management and troubleshooting are when developing and deploying applications.

In future projects, I would prioritize resolving security vulnerabilities before deployment and improving the reliability of the CI/CD pipeline.