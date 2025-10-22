from cloud_earlychecker.core.app_runner import AppRunner
from cloud_earlychecker.core.environment import environment
from rich import print
from rich.panel import Panel

if __name__ == "__main__":
    match environment.get_current_provider():
        case "aws":
            from cloud_earlychecker.cli.aws_cli import AWSEarlyCheckerCLI
        # case "azure":
        case "gcp" | "azrure":
            print(Panel(f"CLOUD_PROVIDER '{environment.get_current_provider()}' is not supported in this CLI.", style="red"))
            exit(1)
        case _:    
            print(Panel(f"CLOUD_PROVIDER '{environment.get_current_provider()}' is not defined in this CLI.", style="red"))
            exit(1)
    
    #Initialize the CLI application with callback and exception handler
    callback = AWSEarlyCheckerCLI.get_app_callback()
    exception_handler = AWSEarlyCheckerCLI.get_exception_handler()
    
    runner = AppRunner(AWSEarlyCheckerCLI, environment=environment.get_environment())
    runner.run(callback=callback, exception_handler=exception_handler)
