# Add project root to sys.path for all tests
from pathlib import Path
import sys


project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root) + "/src")

