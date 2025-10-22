import typer
from rich import print

from cloud_earlychecker.core.app_state import AppState

def aws_region(ctx: typer.Context, region: str = typer.Argument(..., help="AWS region to set as default, e.g., us-east-1")):
    """
    Set default AWS region.
    """
    app_state = AppState.get_app_state(ctx)
    
    app_region = app_state.get("AWS_DEFAULT_REGION")

    if app_region:
        print(f"[yellow]Warning:[/yellow] Overriding machine default region: [bold]{app_region}[/bold]")
        
    app_state.set("AWS_DEFAULT_REGION", region)

    # Placeholder for setting region logic
    print(f"Default AWS region set to: [bold]{region}[/bold]")
