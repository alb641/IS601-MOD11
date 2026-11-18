# IS601 Module 11 — Calculation Model, Validation, Testing, and CI/CD

## Project Overview

This project extends the FastAPI Calculator application developed in previous IS601 modules by introducing a database-backed Calculation model using SQLAlchemy, Pydantic schemas for data validation, and a Calculation Factory for handling arithmetic operations.

The application uses FastAPI, PostgreSQL, SQLAlchemy, Pydantic, Docker, and GitHub Actions to demonstrate how calculations can be validated, processed, stored, tested, and incorporated into an automated CI/CD pipeline.

The primary objective of Module 11 is to strengthen the application's data modeling, validation, testing, and deployment processes while maintaining functionality from previous modules.

## Technologies Used

- Python 3.13
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Pytest
- Docker and Docker Compose
- GitHub Actions
- Docker Hub
- Trivy Vulnerability Scanner

## Module 11 Features

### 1. SQLAlchemy Calculation Model

Created a Calculation model using SQLAlchemy ORM rather than raw SQL.

The model includes the following fields:

| `id` | Unique UUID identifying each calculation |
| `a` | First numerical operand |
| `b` | Second numerical operand |
| `type` | Arithmetic operation |
| `result` | Calculated result |
| `user_id` | Optional foreign key referencing the User model |
| `created_at` | Timestamp for the calculation record |

The model supports four arithmetic operations: Add, Subtract, Multiply, and Divide.

Database constraints help prevent invalid operation types and division by zero.

### 2. Pydantic Schemas and Validation

Implemented Pydantic schemas to validate calculation data.

**CalculationCreate** accepts the operands and operation type.

**CalculationRead** represents calculation records returned from the database, including their UUID and result.

Validation includes:

- Restricting operations to supported calculation types
- Preventing division by zero
- Rejecting missing required operands
- Rejecting non-finite numerical values, including NaN and infinity

These validations help prevent invalid data from entering the application.

### 3. Calculation Factory

Implemented a Calculation Factory to separate arithmetic logic from database operations.

The factory supports addition, subtraction, multiplication, and division.

This design improves code organization, maintainability, and testability by keeping calculation processing separate from the SQLAlchemy model and Pydantic schemas.

### 4. PostgreSQL Integration

Integrated the Calculation model with PostgreSQL using SQLAlchemy.

The Calculation and User models share the same SQLAlchemy metadata, allowing their database tables and relationships to be managed consistently.

A dedicated database named `module11_test_db` was created for integration testing.

This separates test operations from the application's regular database and reduces the risk of modifying existing application data during testing.

### 5. Automated Testing

Implemented unit tests and database integration tests using Pytest.

Testing covers:

- All four arithmetic operations
- Division-by-zero validation
- Invalid operation types
- Missing operands
- NaN and infinity validation
- Calculation record creation and retrieval
- Database persistence
- User foreign-key relationships
- Database constraint enforcement

The complete test suite includes both existing application tests and the new Module 11 tests.

**Latest local test results:**

93 passed, 1 skipped

Run the complete test suite with:

```bash
python -m pytest tests/ -v --tb=short
```

Check dependency compatibility with:

```bash
python -m pip check
```

### 6. CI/CD with GitHub Actions

Configured GitHub Actions to automate testing, security scanning, and Docker image deployment.

The workflow consists of three jobs:

1. **Test:** Installs dependencies, starts a PostgreSQL service, and executes the automated test suite.
2. **Security:** Builds the Docker image and scans it using Trivy.
3. **Deploy:** Publishes the Docker image to Docker Hub after the preceding jobs complete successfully.

The workflow runs when changes are pushed to the main branch.

GitHub Actions uses repository secrets for Docker Hub authentication.

### 7. Security Scanning and Vulnerability Remediation

Trivy is integrated into the CI/CD workflow to identify HIGH and CRITICAL vulnerabilities in the Docker image. A major focus of this module was improving my security configuration based on feedback I received from my professor on Module 10.

In my previous assignment, professor pointed out that Trivy was configured with exit-code: '0', which allowed the CI/CD pipeline to continue deploying the application even when security vulnerabilities were detected. I wanted to address this feedback directly in Module 11 by implementing a stricter security configuration rather than repeating the same issue.

Initial scans detected vulnerable Python dependencies, including PyJWT, h11, Starlette, python-multipart, and dnspython.

Several dependencies were upgraded, and the application was retested to confirm compatibility.

During troubleshooting, Trivy was temporarily configured with `exit-code: '0'`, allowing the pipeline to continue while reporting vulnerabilities.

**Security remediation is ongoing.** The next objective is to resolve the remaining actionable findings, restore `exit-code: '1'`, and verify that deployment succeeds with a blocking security scan.

A successful workflow with a nonblocking scanner is not considered proof that all vulnerabilities have been resolved.

## Installation and Testing

### Clone the Repository

```bash
git clone https://github.com/alb641/IS601-MOD11.git
cd IS601-MOD11
```

### Create a Virtual Environment

```powershell
py -3.13 -m venv venv
.\venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Configure PostgreSQL

Ensure PostgreSQL is running and create a dedicated test database named:

```text
module11_test_db
```

The test suite reads the `TEST_DATABASE_URL` environment variable and verifies that the database name is `module11_test_db`.

For local testing, the default test connection is configured for PostgreSQL on `localhost:5432` with the development credentials used in this project.

### Run Tests

```bash
python -m pytest tests/ -v --tb=short
```

## CI/CD and Docker Hub

**GitHub Repository:**  
https://github.com/alb641/IS601-MOD11

**GitHub Actions:**  
https://github.com/alb641/IS601-MOD11/actions

**Docker Hub Repository:**  
https://hub.docker.com/r/aliyahb4/is601-mod11

The Docker image is published with a `latest` tag and a commit-specific tag.

## Challenges and Troubleshooting

Several challenges occurred during development:

- Correcting SQLAlchemy metadata configuration so the User and Calculation models shared the same database metadata
- Creating an isolated PostgreSQL test database
- Adjusting Pytest fixtures to avoid unnecessary database initialization
- Resolving incompatible Python dependency versions
- Correcting an unavailable Trivy GitHub Action version
- Investigating vulnerabilities reported during Docker image scanning
- Configuring GitHub Actions secrets and Docker Hub deployment

These issues were addressed incrementally through testing, dependency validation, and CI/CD troubleshooting.

## Current Project Status

- Calculation model implemented
- Pydantic schemas implemented
- Calculation Factory implemented
- PostgreSQL integration tests implemented
- 93 tests passing, 1 skipped
- GitHub Actions test pipeline passing
- Docker Hub image successfully published
- Security remediation ongoing

## Future Improvements

Future work includes resolving remaining dependency vulnerabilities, restoring blocking Trivy security checks, and continuing to expand the calculator application with additional functionality and database operations.

The goal is to maintain a reliable application that can be tested, secured, and deployed automatically.