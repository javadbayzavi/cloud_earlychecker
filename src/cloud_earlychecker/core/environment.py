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

        # Load provider
        self.provider = os.getenv("CLOUD_PROVIDER", "").lower()
        if not self.provider:
            raise EnvironmentError(f"CLOUD_PROVIDER not set in '{self.dotenv_file}'.")

        if self.provider not in self.SUPPORTED_PROVIDERS:
            raise EnvironmentError(
                f"Unsupported CLOUD_PROVIDER '{self.provider}'. Supported: {self.SUPPORTED_PROVIDERS}"
            )
    def get_current_provider(self) -> str:
        return self.provider
        
    def get_environment(self) -> str:
        return self.env
    
    def is_aws(self) -> bool:
        return self._is_provider_of("aws")

    def is_azure(self) -> bool:
        return self._is_provider_of("azure")

    def is_gcp(self) -> bool:
        return self._is_provider_of("gcp")
    
    def _is_provider_of(self, provider_name: str) -> bool:
        return self.provider == provider_name.lower()

# singleton instance
environment = CloudEnvironment()