import typer

from nhl.endpoints import (
    awards,
    conferences,
    configurations,
    divisions,
    draft,
    franchises,
    prospects,
    schedule,
    seasons,
    standings,
    teams,
    tournaments,
    venues,
)

app = typer.Typer(
    name="nhl", help="An NHL API CLI", add_completion=False, no_args_is_help=True
)

app.add_typer(awards.app, name="awards")
app.add_typer(conferences.app, name="conferences")
app.add_typer(configurations.app, name="configurations")
app.add_typer(divisions.app, name="divisions")
app.add_typer(draft.app, name="draft")
app.add_typer(franchises.app, name="franchises")
app.add_typer(prospects.app, name="prospects")
app.add_typer(teams.app, name="teams")
app.add_typer(schedule.app, name="schedule")
app.add_typer(seasons.app, name="seasons")
app.add_typer(standings.app, name="standings")
app.add_typer(tournaments.app, name="tournaments")
app.add_typer(venues.app, name="venues")


if __name__ == "__main__":
    app()
