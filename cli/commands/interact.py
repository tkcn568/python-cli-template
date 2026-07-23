"""Interactive command group for user engagement and prompts.

This module provides CLI commands for interactive user engagement, including
random prompt generation and name-based response handling with rich formatting.
"""

from __future__ import annotations

import time

import click
from rich.console import Console
from rich.prompt import Prompt

from ..adapters.interact import InteractAdapter

adapter = InteractAdapter()
console = Console()


@click.group("interact")
@click.pass_context
def interact(ctx: click.Context) -> None:
    """Engage with interactive prompts and responses."""
    pass


@interact.command()
def prompt() -> None:
    """Display a random prompt and capture user response.

    Retrieves a random prompt from the adapter, displays it to the user,
    captures their response, and prints it with formatted output.
    """
    prompt_message = adapter.get_random_prompt()

    response = Prompt.ask(prompt_message)
    console.print(f"[bold yellow]Your response:[/bold yellow] {response}")


@interact.command()
def ask() -> None:
    """Ask for a name and provide a personalized response.

    Retrieves a name prompt from the adapter, captures the user's response,
    displays a thinking indicator, and provides a personalized response.
    """
    name_question = adapter.get_name_prompt()

    response = Prompt.ask(name_question)
    with console.status("🤔 Thinking..."):
        time.sleep(2.0)

    console.print(adapter.respond_to_name(response))
