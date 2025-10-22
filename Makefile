RED    = \033[1;31m
GREEN  = \033[1;32m
YELLOW = \033[1;33m
BLUE   = \033[1;34m
RESET  = \033[0m
PYTHON = python3
PYTHON_TEST = pytest -m
PIP    = pip
VENV   = .venv
REQUIREMENTS = requirements.txt
MAIN = cloud_earlychecker.main

.PHONY: setup test run clean help rebuild_env env_check

rebuild_env:
	@echo -e "$(YELLOW)Rebuilding virtual environment...$(RESET)"
	@rm -rf $(VENV)
	@make setup
	@echo -e "$(GREEN)Rebuild complete!$(RESET)"


env_check:
	@if [ ! -d "$(VENV)" ]; then \
		echo "$(RED)Virtual environment not found. Please run 'make setup' first.$(RESET)"; \
		exit 1; \
	else \
		echo "$(GREEN)Virtual environment found.$(RESET)"; \
	fi	


setup:
	@if [ -d "$(VENV)" ]; then \
		echo "$(YELLOW)Virtual environment already exists — skipping creation.$(RESET)"; \
	else \
		echo "$(BLUE)Creating virtual environment...$(RESET)"; \
		$(PYTHON) -m venv $(VENV); \
	fi
	@$(VENV)/bin/$(PYTHON) -m ensurepip --upgrade --default-pip
	@. $(VENV)/bin/activate && $(PIP) install --upgrade pip

	@if [ ! -f "$(REQUIREMENTS)" ]; then \
		echo "$(YELLOW)No $(REQUIREMENTS) found — skipping dependency installation.$(RESET)"; \
		exit 1; \
	fi
	@echo "$(BLUE)Installing dependencies from $(REQUIREMENTS)...$(RESET)"
	@. $(VENV)/bin/activate && $(PIP) install -r $(REQUIREMENTS)
	@echo "$(GREEN)Setup complete!$(RESET)"



test:
	@make env_check
	@echo "$(BLUE)Running tests...$(RESET)"
	@. $(VENV)/bin/activate && $(PYTHON_TEST)
	@echo "$(GREEN)Tests completed!$(RESET)"



run:
	@make env_check
	@echo "$(BLUE)Running application...  $(ARGS) $(RESET)"
	@PYTHONPATH=src . $(VENV)/bin/activate && $(VENV)/bin/$(PYTHON) -m $(MAIN) $(ARGS)
	@echo "$(GREEN)Application finished!$(RESET)"



help:
	@make setup
	@echo "$(YELLOW)Available commands:$(RESET)"
	@echo "  $(GREEN)make setup$(RESET)   - Set up the virtual environment and install dependencies"
	@echo "  $(GREEN)make test$(RESET)    - Run the test suite"
	@echo "  $(GREEN)make run$(RESET)     - Run the main application"
	@echo "  $(GREEN)make clean$(RESET)   - Clean up the virtual environment"
	@echo "  $(GREEN)make rebuild_env$(RESET) - Rebuild the virtual environment from scratch"
	@echo "  $(GREEN)make env_check$(RESET) - Check if the virtual environment exists"
	@make run help



clean:
	@deactivate || true
	@echo "$(YELLOW)Cleaning up virtual environment...$(RESET)"
	@rm -rf $(VENV)
	@echo "$(GREEN)Cleanup complete!$(RESET)"
