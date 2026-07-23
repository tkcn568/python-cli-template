"""IO command group for simulating input/output operations.

This module provides CLI commands for simulating IO-related functionality,
including file downloads and processing operations with progress indicators.
"""

from __future__ import annotations

import time

import click
from rich.console import Console
from rich.progress import Progress

from ..adapters.io import IOAdapter

adapter = IOAdapter()
console = Console()


@click.group(name="io")
@click.pass_context
def io(ctx: click.Context) -> None:
    """Simulate executing IO-related functionality."""
    ctx.ensure_object(dict)


@io.command()
@click.argument("filename")
@click.pass_context
def simulate_download(ctx: click.Context, filename: str) -> None:
    """Simulate downloading a file with progress indication.

    Parameters
    ----------
    ctx : click.Context
        Click context object
    filename : str
        Name of the file to simulate downloading
    """
    total, advance = adapter.get_progress_values()

    with Progress() as progress:
        task = progress.add_task("[cyan]Downloading...[/cyan]", total=total)

        while not progress.finished:
            progress.update(task, advance=advance)
            time.sleep(0.02)


@io.command()
@click.argument("filename")
@click.pass_context
def simulate_process(ctx: click.Context, filename: str) -> None:
    """Simulate processing a file with progress indication.

    Parameters
    ----------
    ctx : click.Context
        Click context object
    filename : str
        Name of the file to simulate processing
    """
    total, advance = adapter.get_progress_values()

    with Progress() as progress:
        task = progress.add_task("[cyan]Processing...[/cyan]", total=total)

        while not progress.finished:
            progress.update(task, advance=advance)
            time.sleep(0.02)
