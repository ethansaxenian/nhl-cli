import typer

PrettyFormat = typer.Option(False, "--pretty", help="Format output.")

SortKeys = typer.Option(False, "--sort-keys", help="Sort output.")

ExpandOption = typer.Option([], help="See nhl expands for details.")

SeasonOption = typer.Option(
    None, help="Specify the season.", show_default="Uses the current season"
)
