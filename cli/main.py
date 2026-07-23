"""Main CLI entry point.

Defines the root command group and registers all subcommand groups.
This module serves as the central dispatcher for the CLI application.
"""

from __future__ import annotations

import click

from .__version__ import __pkgname__, __version__
from .commands.endoflife import endoflife
from .commands.interact import interact
from .commands.io import io


@click.group()
@click.version_option(prog_name=__pkgname__, version=__version__)
def cli() -> None:
    """Python CLI Template - Modern command-line interface framework."""
    pass


cli.add_command(endoflife, name="endoflife")
cli.add_command(io, name="io")
cli.add_command(interact, name="interact")
