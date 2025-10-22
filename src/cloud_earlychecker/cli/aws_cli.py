import typer
from rich import print
from cloud_earlychecker.cli_commands import cli_checker, connect
from cloud_earlychecker.core.app_state import AppState
from cloud_earlychecker.interfaces.callback import AppCallback
from cloud_earlychecker.interfaces.cli_interface import CLIInterface
from cloud_earlychecker.interfaces.exception import ExceptionHandler

class AWSEarlyCheckerCLI(CLIInterface):
    def __init__(self):
        self.name = "AWS EarlyChecker"

    def register(self, app: typer.Typer, callback: AppCallback=None, exception_handler: ExceptionHandler=None):
        """Attach commands, callback, and error handler."""
        from cloud_earlychecker.cli_commands import version, region, profile, status

        app.command(name="version")(version.version)
        app.command(name="connect")(connect.aws_connect)
        app.command(name="region")(region.aws_region)
        app.command(name="check_profile")(profile.profile)
        app.command(name="check_aws_cli")(cli_checker.aws_cli_checker)
        app.command(name="status")(status.status)

        if callback:
            app.callback()(callback.callback)

        if exception_handler:
            exception_handler.register_exceptions(app)

    def run(self):
        """Any pre-launch logic, like loading configuration or AWS credentials."""
        print("[blue]Initializing AWS EarlyChecker CLI...[/blue]")

    @staticmethod
    def get_app_callback(appState: AppState = None) -> AppCallback:
        """Return the main application callback."""
        from cloud_earlychecker.callbacks.cli_callback import CliCallback
        if appState is None:
            appState = AppState.create_default_state()

        return CliCallback(appState=appState)    
    
    @staticmethod
    def get_exception_handler() -> ExceptionHandler:
        """Return the exception handler for the application."""
        from cloud_earlychecker.interfaces.exception import DefaultExceptionHandler
        return DefaultExceptionHandler()