from pathlib import Path
import typer
import subprocess; 
from cloud_earlychecker.core.app_state import AppState
from rich import print

def aws_connect(ctx: typer.Context):
    """
    Establish connection to AWS.
    """
    app_state = AppState.get_app_state(ctx)

    #Check for AWS region set in the app state
    if app_state.get("AWS_DEFAULT_REGION") is None:
        print("[red]Error:[/red] AWS region is not set. Please set the region using the 'region' command before connecting.")
        return
    
    #Setting AWS region from app state
    app_state.getEnvironment().set("AWS_DEFAULT_REGION", app_state.get("AWS_DEFAULT_REGION"))

    #Check AWC Credentials are set in the machin profile
    if not aws_credentials_check(app_state):
        print("[red]Error:[/red] AWS credentials are not set. Please configure your AWS credentials before connecting.")
        return

    print("[blue]Connecting to AWS...[/blue]")
    result = subprocess.run(["aws", "sts", "get-caller-identity"])
    if result.returncode != 0:
        print("[red]Failed to connect to AWS. Please check your AWS CLI configuration.[/red]")
        app_state.set("aws_connected", False)
    else:
        print("[blue]Connection attempt finished.[/blue]")
        app_state.set("aws_connected", True)

    # Placeholder for AWS connection logic
    print("[green]Successfully connected to AWS.[/green]"   )

def aws_credentials_check(app_state: AppState) -> bool:
    # Check environment variables
    if app_state.getEnvironment().get("AWS_ACCESS_KEY_ID") and app_state.getEnvironment().get("AWS_SECRET_ACCESS_KEY"):
        return True

    # Check default credentials file
    cred_file = Path.home() / ".aws" / "credentials"
    if cred_file.exists():
        return True

    return False

