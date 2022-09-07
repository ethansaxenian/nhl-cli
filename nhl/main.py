import typer

from nhl.endpoints import (
    awards,
    conferences,
    configurations,
    depth_types,
    divisions,
    draft,
    event_types,
    expands,
    franchises,
    game_status,
    game_types,
    image_sizes,
    image_types,
    languages,
    league_leader_types,
    performer_types,
    platforms,
    play_types,
    play_types_player,
    player_status,
    positions,
    power_play_strength,
    prospect_categories,
    prospects,
    roster_statuses,
    roster_types,
    schedule,
    schedule_types,
    seasons,
    series_codes,
    site_language,
    standings,
    standings_types,
    stat_types,
    team_designations,
    teams,
    tournament_types,
    tournaments,
    venues,
)

app = typer.Typer(
    name="nhl", help="An NHL API CLI", add_completion=False, no_args_is_help=True
)

app.add_typer(awards.app, name="awards")
app.add_typer(conferences.app, name="conferences")
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

app.add_typer(configurations.app, name="configurations")
app.add_typer(languages.app, name="languages")
app.add_typer(game_types.app, name="game-types")
app.add_typer(series_codes.app, name="series-codes")
app.add_typer(expands.app, name="expands")
app.add_typer(player_status.app, name="player-status")
app.add_typer(performer_types.app, name="performer-types")
app.add_typer(schedule_types.app, name="schedule-types")
app.add_typer(stat_types.app, name="stat-types")
app.add_typer(standings_types.app, name="standings-types")
app.add_typer(game_status.app, name="game-status")
app.add_typer(play_types.app, name="play-types")
app.add_typer(play_types_player.app, name="play-types-player")
app.add_typer(positions.app, name="positions")
app.add_typer(platforms.app, name="platforms")
app.add_typer(power_play_strength.app, name="power-play-strength")
app.add_typer(league_leader_types.app, name="league-leader-types")
app.add_typer(depth_types.app, name="depth-types")
app.add_typer(image_types.app, name="image-types")
app.add_typer(image_sizes.app, name="image-sizes")
app.add_typer(roster_types.app, name="roster-types")
app.add_typer(site_language.app, name="site-language")
app.add_typer(team_designations.app, name="team-designations")
app.add_typer(roster_statuses.app, name="roster-statuses")
app.add_typer(event_types.app, name="event-types")
app.add_typer(tournament_types.app, name="tournament-types")
app.add_typer(prospect_categories.app, name="prospect-categories")

if __name__ == "__main__":
    app()
