"""Package version and metadata.

Contains version information and package name constants used throughout the CLI.
"""

from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

__pkgname__ = "python-cli-template"
__location__ = Path(__file__).resolve().parent

try:
    __version__ = version(__pkgname__)
except PackageNotFoundError:
    __version__ = "1.0.0"
