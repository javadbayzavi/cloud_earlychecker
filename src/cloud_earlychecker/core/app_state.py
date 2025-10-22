import json
from pathlib import Path
from cloud_earlychecker.core.environment import CloudEnvironment, environment
from rich import print
import typer

STATE_FILE = Path.home() / ".cloud_earlychecker_state.json"

class AppState:
    def __init__(self, environment: CloudEnvironment = None):
        self._state = {}
        self.environment = environment
        self.load_state()

    def set(self, key, value):
        self._state[key] = value
        self.save_state()

    def get(self, key, default=None):
        return self._state.get(key, default)

    def delete(self, key):
        if key in self._state:
            del self._state[key]
            self.save_state()

    def clear(self):
        self._state.clear()
        self.save_state()

    def getEnvironment(self) -> CloudEnvironment:
        return self.environment    

    @staticmethod
    def get_app_state(ctx: 'typer.Context') -> 'AppState':
        return ctx.obj

    @staticmethod
    def create_default_state() -> 'AppState':
        return AppState(environment=environment)

    def save_state(self):
        """Persist state to a JSON file."""
        try:
            with open(STATE_FILE, "w") as f:
                json.dump(self._state, f)
        except Exception as e:
            print(f"⚠️ Failed to save state: {e}")

    def load_state(self):
        """Load state from JSON file if it exists."""
        if STATE_FILE.exists():
            try:
                with open(STATE_FILE, "r") as f:
                    self._state = json.load(f)
            except Exception as e:
                print(f"⚠️ Failed to load state: {e}")
                self._state = {}