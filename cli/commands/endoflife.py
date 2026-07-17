"""End-of-Life command group for querying product lifecycle information.

This module provides CLI commands for interacting with the endoflife.date API.
It includes subcommands for querying endpoints, products, categories, and tags.
"""

from __future__ import annotations

import click
from requests import HTTPError
from requests.exceptions import ConnectionError, RequestException
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from ..adapters.endoflife import EndOfLifeAdapter

adapter = EndOfLifeAdapter()
console = Console()

def _handle_request_error(exc: RequestException, context: str = "request") -> None:
    """Handle and display HTTP request errors.

    Parameters
    ----------
    exc : RequestException
        The exception that occurred during the request
    context : str, optional
        Context description for error message (default: "request")
    """
    console.print("[bold red]An error occurred connecting to the service.[/bold red]")
    if isinstance(exc, HTTPError):
        console.print(Panel(
            f"[bold]URL:[/bold]         {exc.response.url}\n"
            f"[bold]Status Code:[/bold] {exc.response.status_code}\n"
            f"[bold]Reason:[/bold]      {exc.response.reason}\n"
            f"[bold]Text:[/bold]        {exc.response.text or 'N/A'}",
            title="Error details"
        ))
    else:
        console.print(Panel(
            f"[bold]Error:[/bold] {exc}"
        ))

@click.group(name="endoflife")
@click.pass_context
def endoflife(ctx: click.Context) -> None:
    """Query end-of-life information for software products and frameworks."""
    ctx.ensure_object(dict)

@endoflife.command()
@click.pass_context
def endpoints(ctx: click.Context) -> None:
    """Display all available API endpoints.

    Parameters
    ----------
    ctx : click.Context
        Click context object
    """
    results = []
    try:
        result = adapter.index()
        results = result["result"]
        console.print(
            f"Using schema [bold cyan]{result['schema_version']}[/bold cyan] "
            f"at [bold]{result['generated_at']}[/bold].\n"
        )
    except (HTTPError, ConnectionError, RequestException) as exc:
        _handle_request_error(exc)
        raise click.Abort()

    table = Table(title="Main endoflife.date API endpoints")
    table.add_column("Name", style="bold cyan")
    table.add_column("URI")
    for r in results:
        table.add_row(
            r["name"],
            r["uri"]
        )

    console.print(table)

@endoflife.command()
@click.option(
    "--product",
    "-p",
    default=None,
    type=str,
    help="Get a specific product's detail."
)
@click.option(
    "--release",
    "-r",
    default=None,
    type=str,
    help="Pin a specific product release."
)
@click.option(
    "--full",
    "-f",
    default=False,
    is_flag=True,
    help="Get a full output of all products. (Does not work with --release)"
)
@click.pass_context
def products(ctx, product, release, full):
    """Query product release and lifecycle information.

    Parameters
    ----------
    ctx : click.Context
        Click context object
    product : str, optional
        Specific product name to query
    release : str, optional
        Specific product release version
    full : bool
        Include full details for all products
    """
    multi_product = True
    if product and full:
        console.print("[bold error]Invalid options.[/bold error] --product and --full cannot be set simultaneously.")
        raise click.Abort()

    products = []
    try:
        if product:
            multi_product = False
            result = adapter.get_product(product, release=release)
            product = result["result"]["label"]
            products = result["result"]["releases"]
        else:
            result = adapter.get_products(full)
            products = result["result"]
        console.print(f"Found [bold green]{len(products)}[/bold green] result(s).")
    except (HTTPError, ConnectionError, RequestException) as exc:
        _handle_request_error(exc)
        raise click.Abort(exc)

    if multi_product:
        table = Table(title="Product information")
        table.add_column("Product", style="bold cyan")
        table.add_column("Category", style="bold")
        table.add_column("Tags")
        table.add_column("URI")

        for p in products:
            table.add_row(
                p["label"],
                p["category"],
                ", ".join(p["tags"]),
                p["uri"],
            )

    else:
        table = Table(title=f"{product} release information")
        table.add_column("Major Version", style="bold cyan")
        table.add_column("Release Date")
        table.add_column("LTS Release?")
        table.add_column("End of Active Support?")
        table.add_column("End of Life?")
        table.add_column("Actively Maintained?")

        for p in products:
            table.add_row(
                p["label"],
                p["releaseDate"],
                "Yes" if p["isLts"] else "No",
                f"[bold red]Yes (ended {p['eoasFrom']})[/bold red]" if p["isEoas"] else \
                    f"[bold green]No (ends {p['eoasFrom']})[/bold green]",
                f"[bold red]Yes (ended {p['eolFrom']})[/bold red]" if p["isEol"] else \
                    f"[bold green]No (ends {p['eolFrom']})[/bold green]",
                "Yes" if p["isMaintained"] else "No",
            )

    console.print(table)

@endoflife.command()
@click.option(
    "--category",
    "-c",
    default=None,
    type=str,
    help="Get a specific category's results."
)
@click.pass_context
def categories(ctx, category):
    """Query product categories and their members.

    Parameters
    ----------
    ctx : click.Context
        Click context object
    category : str, optional
        Specific category name to query
    """
    if category:
        try:
            result = adapter.get_category(category)
            products = result["result"]
        except (HTTPError, ConnectionError, RequestException) as exc:
            _handle_request_error(exc)
            raise click.Abort(exc)

        table = Table(title=f"Products in category {category}")
        table.add_column("Product", style="bold cyan")
        table.add_column("Tags")
        table.add_column("URI")

        for p in products:
            table.add_row(
                p["label"],
                ", ".join(p["tags"]),
                p["uri"]
            )
    else:
        try:
            result = adapter.get_categories()
            categories = result["result"]
        except (HTTPError, ConnectionError, RequestException) as exc:
            _handle_request_error(exc)
            raise click.Abort(exc)

        table = Table(title="Categories")
        table.add_column("Name", style="bold cyan")
        table.add_column("URI")

        for c in categories:
            table.add_row(
                c["name"],
                c["uri"],
            )
    console.print(table)

@endoflife.command()
@click.option(
    "--tag",
    "-t",
    default=None,
    type=str,
    help="Get a specific tag's results."
)
@click.pass_context
def tags(ctx, tag):
    """Query product tags and their members.

    Parameters
    ----------
    ctx : click.Context
        Click context object
    tag : str, optional
        Specific tag name to query
    """
    if tag:
        try:
            result = adapter.get_tag(tag)
            products = result["result"]
        except (HTTPError, ConnectionError, RequestException) as exc:
            _handle_request_error(exc)
            raise click.Abort(exc)

        table = Table(title=f"Products in category {tag}")
        table.add_column("Product", style="bold cyan")
        table.add_column("Category")
        table.add_column("Tags")
        table.add_column("URI")

        for p in products:
            table.add_row(
                p["label"],
                p["category"],
                ", ".join(p["tags"]),
                p["uri"]
            )
    else:
        try:
            result = adapter.get_tags()
            tags = result["result"]
        except (HTTPError, ConnectionError, RequestException) as exc:
            _handle_request_error(exc)
            raise click.Abort(exc)

        table = Table(title="Categories")
        table.add_column("Name", style="bold cyan")
        table.add_column("URI")

        for t in tags:
            table.add_row(
                t["name"],
                t["uri"],
            )
    console.print(table)
