import typer
from rich.console import Console
from rich.table import Table
from aws_earlychecker.exception import AWSHealthCheckError
import aws_earlychecker.services.core as core

def status(
    region: str = typer.Option(..., help="AWS region to check, e.g., us-east-1"),
    services: str = typer.Option("sns,sqs,s3", help="Comma-separated list of AWS services")
):
    """
    Check AWS service health for a region.
    """
    service_list = [s.strip().upper() for s in services.split(",")]
    results = core.check_services(region, service_list)
    
    console = Console()
    table = Table(title=f"AWS Service Status for {region}", show_lines=True)
    
    table.add_column("Service", style="cyan", no_wrap=True)
    table.add_column("Status", style="magenta")
    
    for svc, state in results.items():
        status_text = f"[green]✅ {state}[/green]" if state == "OPERATIONAL" else f"[red]⚠️ {state}[/red]"
        table.add_row(svc, status_text)
    
    console.print(table)