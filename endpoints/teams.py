import typer as typer

from helpers import PrettyFormat, SortKeys, fetch, print_response

app = typer.Typer()


@app.command()
def teams(
    id: str = typer.Argument(
        default="", help="The ID of the team.", show_default="Gets all teams."
    ),
    pretty: bool = PrettyFormat,
    sort_keys: bool = SortKeys,
):
    """
    Get information about NHL teams.
    """
    res = fetch(f"teams/{id}")
    print_response(res, pretty=pretty, sort_keys=sort_keys)


if __name__ == "__main__":
    app()
