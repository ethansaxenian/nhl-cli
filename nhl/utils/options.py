import typer

PrettyFormat = typer.Option(False, "--pretty", "-p", help="Format output.")

SortKeys = typer.Option(False, "--sort-keys", "-s", help="Sort output.")

NoColors = typer.Option(False, "--no-colors", "-n", help="Disable colored output.")

ExpandOption = typer.Option(
    [], "--expand", "-e", help="See 'nhl configurations expands' for details."
)

SeasonOption = typer.Option(
    None,
    help="Specify the season. Format: YYYYYYYY (ex: 20202021)",
    show_default="Uses the current season",
)
