import typer

from nhl.endpoints import (
    conferences,
    configurations,
    divisions,
    franchises,
    teams,
    tournaments,
)

app = typer.Typer(
    name="nhl", help="An NHL API CLI", add_completion=False, no_args_is_help=True
)


app.add_typer(conferences.app, name="conferences")
app.add_typer(configurations.app, name="configurations")
app.add_typer(divisions.app, name="divisions")
app.add_typer(franchises.app, name="franchises")
app.add_typer(teams.app, name="teams")
app.add_typer(tournaments.app, name="tournaments")


if __name__ == "__main__":
    app()
