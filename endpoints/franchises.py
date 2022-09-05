import typer as typer

from helpers import PrettyFormat, SortKeys, fetch, print_response

app = typer.Typer()


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
