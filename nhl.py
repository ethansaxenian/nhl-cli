import typer

from helpers import fetch, print_response

app = typer.Typer(name="nhl", help="An NHL API CLI", add_completion=False)

PrettyFormat = typer.Option(False, "--pretty", help="Format output.")

SortKeys = typer.Option(False, "--sort-keys", help="Sort output.")


@app.command()
def teams(
    id: str = typer.Argument(
        "", help="The ID of the team.", show_default="Gets all teams."
    ),
    pretty: bool = PrettyFormat,
    sort_keys: bool = SortKeys,
):
    """
    Get information about NHL teams.
    """
    res = fetch(f"teams/{id}")
    print_response(res, pretty=pretty, sort_keys=sort_keys)


@app.command()
def franchises(
    id: str = typer.Argument(
        default="", help="The ID of the franchise.", show_default="Gets all franchises."
    ),
    pretty: bool = PrettyFormat,
    sort_keys: bool = SortKeys,
):
    """
    Get information about NHL franchises.
    """
    res = fetch(f"franchises/{id}")
    print_response(res, pretty=pretty, sort_keys=sort_keys)


if __name__ == "__main__":
    app()
