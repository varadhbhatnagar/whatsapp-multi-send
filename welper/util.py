from pathlib import Path
from os import sep


def get_project_root() -> Path:
    """Returns project root folder."""
    return Path(__file__).parent