from enum import Enum

import typer

PrettyFormat = typer.Option(False, "--pretty", help="Format output.")

SortKeys = typer.Option(False, "--sort-keys", help="Sort output.")
