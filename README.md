# IS601 Module 11 — FastAPI Calculator with SQLAlchemy and PostgreSQL

**GitHub Repository:** https://github.com/alb641/IS601-MOD11

**GitHub Actions:** https://github.com/alb641/IS601-MOD11/actions

**Docker Hub Username:** aliyahb4

## Project Overview

This project extends the FastAPI Calculator application by incorporating SQLAlchemy, PostgreSQL, and Pydantic to support database persistence, structured data validation, and arithmetic calculations.

The application supports addition, subtraction, multiplication, and division. The project also incorporates automated testing, Docker containerization, GitHub Actions CI/CD, and Trivy vulnerability scanning.

## Technologies Used

- Python 3.13
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Docker and Docker Compose
- pytest
- GitHub Actions
- Trivy

## Application Features

### SQLAlchemy Calculation Model

The application uses SQLAlchemy to represent calculation records stored in PostgreSQL. The model includes calculation identifiers, operands, operation types, and calculation results.

Using SQLAlchemy allows the application to manage database records through Python objects rather than relying on raw SQL for every operation.

### Pydantic Validation

Pydantic schemas validate incoming calculation requests and structure outgoing responses.

The validation logic checks numeric inputs, supported arithmetic operations, and invalid calculations such as division by zero.

### Arithmetic Operations

The calculator supports the following operations:

| Operation | Example | Result |
|---|---|---|
| Addition | 10 + 5 | 15 |
| Subtraction | 10 - 5 | 5 |
| Multiplication | 10 × 5 | 50 |
| Division | 10 ÷ 5 | 2 |

### Calculation Factory

The calculation factory organizes arithmetic operations and separates calculation logic from other application responsibilities.

This improves maintainability and supports future expansion.

### PostgreSQL Integration

PostgreSQL provides persistent data storage, while SQLAlchemy manages interactions between Python models and database tables.

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/alb641/IS601-MOD11.git
cd IS601-MOD11
```

### Step 2: Create a Virtual Environment

On Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies

```powershell
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Configure the PostgreSQL database connection and application authentication settings using environment variables or a local `.env` file.

Do not commit sensitive credentials to GitHub.

### Step 5: Start PostgreSQL

With Docker Desktop running:

```powershell
docker compose up -d db
```

### Step 6: Start FastAPI

```powershell
python -m uvicorn main:app --reload
```

Application URL: http://127.0.0.1:8000

Interactive API documentation: http://127.0.0.1:8000/docs

## Testing

The application uses pytest for unit, integration, end-to-end, and regression testing.

Run the tests using:

```powershell
python -m pytest -q
```

**Latest confirmed local results: 94 passed, 1 skipped.**

## Docker

Docker provides a consistent application environment, and Docker Compose simplifies running the application with PostgreSQL.

Build the Docker image:

```powershell
docker build -t is601-mod11 .
```

Start the services:

```powershell
docker compose up -d
```

A `.dockerignore` file excludes unnecessary development files, including local virtual environments, caches, and Git metadata.

## GitHub Actions CI/CD

GitHub Actions automates testing, Docker image building, vulnerability scanning, and image publishing.

**Workflow:** https://github.com/alb641/IS601-MOD11/actions

Trivy is used to scan the Docker image for known security vulnerabilities.

During troubleshooting, the reported vulnerability count was reduced from 26 to 1, eliminating all reported CRITICAL findings.

One HIGH vulnerability involving setuptools remained unresolved. Trivy's exit code was changed to `0` to make findings non-blocking while continuing to report them. This does not resolve the remaining vulnerability as mentioned by Professor in previous feedback.

## Docker Hub Repo

**Docker Hub Repo:** [https://hub.docker.com/u/aliyahb4](https://hub.docker.com/r/aliyahb4/is601-mod11/tags)

The GitHub Actions workflow includes Docker image publishing. The successful publication of the Module 11 image should be confirmed in the workflow logs.

## Project Repository

**GitHub:** https://github.com/alb641/IS601-MOD11