from pathlib import Path
from dotenv import load_dotenv
import os

class CloudEnvironment:
    """Loads and validates environment configuration for the CLI."""

    SUPPORTED_PROVIDERS = {"aws", "azure", "gcp"}

    def __init__(self):
        # Determine environment (default 'prod')
        self.env = os.getenv("ENVIRONMENT", "prod").lower()

        # Project root (adjust according to your folder structure)
        self.project_root = Path(__file__).resolve().parent.parent.parent.parent

        # Load the environment file
        self.dotenv_file = self.project_root / f".env.{self.env}"
        if not load_dotenv(self.dotenv_file):
            raise FileNotFoundError(f"Environment file '{self.dotenv_file}' not found or failed to load.")

    def get_current_provider(self) -> str:
        return self.get("CLOUD_PROVIDER")

    def get(self, variable: str) -> str:
        return os.getenv(variable, "")
    
    def set(self, variable: str, value: str):
        os.environ[variable] = value

    def get_environment(self) -> str:
        return self.env
    
    def is_aws(self) -> bool:
        return self._is_provider_of("aws")

    def is_azure(self) -> bool:
        return self._is_provider_of("azure")

    def is_gcp(self) -> bool:
        return self._is_provider_of("gcp")
    
    def _is_provider_of(self, provider_name: str) -> bool:
        return self.get("CLOUD_PROVIDER") == provider_name.lower()

# singleton instance
environment = CloudEnvironment()