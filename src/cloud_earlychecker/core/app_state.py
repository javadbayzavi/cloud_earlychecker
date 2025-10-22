from cloud_earlychecker.core.environment import CloudEnvironment, environment

class AppState:
    def __init__(self, environment: CloudEnvironment = None):
        self._state = {}
        self.environment = environment

    def set(self, key, value):
        self._state[key] = value

    def get(self, key, default=None):
        return self._state.get(key, default)

    def delete(self, key):
        if key in self._state:
            del self._state[key]

    def clear(self):
        self._state.clear()

    def getEnvironment(self) -> CloudEnvironment:
        return self.environment    
    
    @staticmethod
    def create_default_state() -> 'AppState':
        # Initialize default state values if needed
        app_state = AppState(environment=environment)
        return app_state