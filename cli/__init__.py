"""Python CLI Template package.

A modern command-line interface framework for building CLI applications with Click,
featuring structured command hierarchies, rich output formatting, and HTTP adapters
for external service integration.
"""

import sys

from .main import cli

if __name__ == "__main__":
    cli(sys.argv[1:], obj={})
