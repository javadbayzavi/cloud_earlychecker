# Cloud EarlyChecker

Cloud EarlyChecker is a Python CLI tool designed to monitor cloud service health and detect potential service degradation early. It currently supports AWS and is designed for easy extension to other cloud providers such as Azure and Google Cloud in the future.

---

## Features

- **Monitor Cloud Services:** Check the health of AWS services for a given region.
- **Dynamic Environment Configuration:** Supports multiple environments using `.env` files (`.env.prod`, `.env.test`, etc.).
- **User-Friendly CLI:** Built with [Typer](https://typer.tiangolo.com/), offering clear commands and options.
- **Rich Output:** Uses [Rich](https://rich.readthedocs.io/) for color-coded terminal output and tables.
- **Custom Exception Handling:** Centralized error management with clear messages for invalid commands or service errors.
- **Extensible Design:** Interfaces and base classes allow adding new cloud providers, commands, and custom exception handlers easily.
- **Makefile Support:** Simplifies common tasks such as environment setup, running the CLI, or executing tests.

---

## Installation

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/javadbayzavi/cloud_earlychecker.git
cd cloud_earlychecker
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Environment Setup

Cloud EarlyChecker uses environment variables to configure the cloud provider and the environment. Environment files are located in the project root:

- `.env.prod` – Production environment
- `.env.test` – Testing environment

Example `.env.prod`:

```env
CLOUD_PROVIDER=aws
```

Set the environment before running the CLI:

```bash
export ENVIRONMENT=prod
```

The application will automatically load the corresponding `.env` file (e.g., `.env.prod`) and validate that the cloud provider is supported.

---

## Usage

Activate your virtual environment and run the CLI:

```bash
source .venv/bin/activate
python3 -m aws_earlychecker.main <COMMAND> [OPTIONS]
```

### Available Commands

| Command            | Description                                |
|-------------------|--------------------------------------------|
| `version`          | Show the CLI version                        |
| `region`           | Show available regions                       |
| `check_profile`    | Check your AWS profile configuration        |
| `check_aws_cli`    | Check AWS CLI installation                  |
| `status`           | Check AWS service health for a region       |

### Example

```bash
python3 -m aws_earlychecker.main status --region us-east-1
```

Output is displayed as a color-coded table using Rich.

---

## Makefile

The project includes a Makefile to simplify common tasks:

```makefile
# Install dependencies
install:
	pip install -r requirements.txt

# Run the CLI (default environment is prod)
run:
	python3 -m aws_earlychecker.main

# Run tests (update later when test implementation is ready)
test:
	pytest tests/
```

---

## Extending to Other Cloud Providers

Cloud EarlyChecker is designed to allow additional cloud providers. To add support for Azure or Google Cloud:

1. Create a new CLI implementation class for the provider.
2. Implement the necessary commands and health checks.
3. Add provider-specific environment files (e.g., `.env.azure`, `.env.gcp`).
4. Update main application logic to select the correct implementation based on `CLOUD_PROVIDER`.
