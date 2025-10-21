import typer
from typing import Type
from rich import print
from aws_earlychecker.exception import AWSHealthCheckError, EmptyCommandError, InvalidCommandError, NoSuchCommandError
from aws_earlychecker.interfaces.cli_interface import CLIInterface
from aws_earlychecker.interfaces.callback import AppCallback
from click.exceptions import NoSuchOption

class AppRunner:
    """Responsible for wiring CLI implementations into Typer and executing them."""

    def __init__(self, cli_impl: Type[CLIInterface]):
        self.app = typer.Typer(help="AWS EarlyCheck CLI – detect AWS service degradation early.")
        self.cli_impl = cli_impl

    def setup(self, callback: AppCallback=None, exception_handler=None):
        """Register all commands, callbacks, and error handlers from CLI implementation."""
        cli_instance = self.cli_impl()
        cli_instance.register(self.app, callback=callback)
        return cli_instance
    
    def run(self, callback: AppCallback=None, exception_handler=None):
        """Run the CLI application."""
        instance = self.setup(callback=callback, exception_handler=exception_handler)
        instance.run()
        try:
            self.app()
        except NoSuchOption as exc:
            raise NoSuchCommandError(exc.option_name)

        except EmptyCommandError as exc:
            print(f"[red]❌ {exc}[/red]")
            raise typer.Exit(code=2)

        except NoSuchCommandError as exc:
            print(f"[red]❌ {exc}[/red]")
            raise typer.Exit(code=2)

        except AWSHealthCheckError as exc:
            print(f"[red]⚠️ AWS Health Check Failed:[/red] {exc}")
            raise typer.Exit(code=3)

        except InvalidCommandError as exc:
            print(f"[red]❌ Invalid Command:[/red] {exc}")
            raise typer.Exit(code=2)

        except Exception as exc:
            print(f"[red]💥 Unexpected error:[/red] {exc}")
            raise typer.Exit(code=1)