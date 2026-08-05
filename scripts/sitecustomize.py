from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parent.parent

root = str(PROJECT_ROOT)

if root not in sys.path:
    sys.path.insert(0, root)