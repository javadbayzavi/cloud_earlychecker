from aws_earlychecker.cli.aws_cli import AWSEarlyCheckerCLI
from aws_earlychecker.core.app_runner import AppRunner

if __name__ == "__main__":
    #Initialize the CLI application with callback and exception handler
    callback = AWSEarlyCheckerCLI.get_app_callback()
    exception_handler = AWSEarlyCheckerCLI.get_exception_handler()

    runner = AppRunner(AWSEarlyCheckerCLI)
    runner.run(callback=callback, exception_handler=exception_handler)
