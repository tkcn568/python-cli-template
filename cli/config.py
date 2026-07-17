"""Configuration management for the CLI application.

This module defines the standard configuration file search paths for the CLI.
Configuration files are searched in the following order:
  1. User's local config directory (~/.local/python-cli-template/settings.conf)
  2. User's home directory config (~/.python-cli-templaterc)
  3. Current working directory (~/.python-cli-template/settings.conf)
"""

from pathlib import Path

from .__version__ import __pkgname__

CONFIG_PATHS = [
    Path.home() / f".local/{__pkgname__}/settings.conf",
    Path.home() / f".{__pkgname__}rc",
    Path.cwd() / f".{__pkgname__}/settings.conf",
]
