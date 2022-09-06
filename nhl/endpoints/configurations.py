import typer

from nhl.utils.helpers import fetch, print_response
from nhl.utils.options import NoColors, PrettyFormat, SortKeys

app = typer.Typer(help="Get information about configurations.")


@app.callback(invoke_without_command=True)
def configurations(
    ctx: typer.Context,
    pretty: bool = PrettyFormat,
    sort_keys: bool = SortKeys,
    no_colors: bool = NoColors,
):
    if ctx.invoked_subcommand is None:
        res = fetch(["configurations"])
        print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)


@app.command(help="List all possible image sizes for the logos.")
def image_sizes(
    pretty: bool = PrettyFormat, sort_keys: bool = SortKeys, no_colors: bool = NoColors
):
    res = fetch(["imageSizes"])
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)


@app.command(help="List all possible roster types.")
def roster_types(
    pretty: bool = PrettyFormat, sort_keys: bool = SortKeys, no_colors: bool = NoColors
):
    res = fetch(["rosterTypes"])
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)


@app.command(help="Lists all possible {language}_{site} params..")
def site_language(
    pretty: bool = PrettyFormat, sort_keys: bool = SortKeys, no_colors: bool = NoColors
):
    res = fetch(["siteLanguage"])
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)


@app.command(help="List all possible team designations.")
def team_designations(
    pretty: bool = PrettyFormat, sort_keys: bool = SortKeys, no_colors: bool = NoColors
):
    res = fetch(["teamDesignations"])
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)


@app.command(help="List all possible hockey roster statuses.")
def roster_statuses(
    pretty: bool = PrettyFormat, sort_keys: bool = SortKeys, no_colors: bool = NoColors
):
    res = fetch(["rosterStatuses"])
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)


@app.command(help="List all possible event types.")
def event_types(
    pretty: bool = PrettyFormat, sort_keys: bool = SortKeys, no_colors: bool = NoColors
):
    res = fetch(["eventTypes"])
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)


@app.command(help="List all possible tournament types.")
def tournament_types(
    pretty: bool = PrettyFormat, sort_keys: bool = SortKeys, no_colors: bool = NoColors
):
    res = fetch(["tournamentTypes"])
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)


@app.command(help="List all possible draft prospect categories.")
def prospect_categories(
    pretty: bool = PrettyFormat, sort_keys: bool = SortKeys, no_colors: bool = NoColors
):
    res = fetch(["prospectCategories"])
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)


@app.command(help="List all support languages.")
def languages(
    pretty: bool = PrettyFormat, sort_keys: bool = SortKeys, no_colors: bool = NoColors
):
    res = fetch(["languages"])
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)


@app.command(help="List all stat types.")
def stat_types(
    pretty: bool = PrettyFormat, sort_keys: bool = SortKeys, no_colors: bool = NoColors
):
    res = fetch(["statTypes"])
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)


@app.command(help="List all standings types.")
def standings_types(
    pretty: bool = PrettyFormat, sort_keys: bool = SortKeys, no_colors: bool = NoColors
):
    res = fetch(["standingsTypes"])
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)


@app.command(help="List all status types.")
def game_status(
    pretty: bool = PrettyFormat, sort_keys: bool = SortKeys, no_colors: bool = NoColors
):
    res = fetch(["gameStatus"])
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)


@app.command(help="List all play types.")
def play_types(
    pretty: bool = PrettyFormat, sort_keys: bool = SortKeys, no_colors: bool = NoColors
):
    res = fetch(["playTypes"])
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)


@app.command(help="List all play types for player.")
def play_types_player(
    pretty: bool = PrettyFormat, sort_keys: bool = SortKeys, no_colors: bool = NoColors
):
    res = fetch(["playTypesPlayer"])
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)


@app.command(help="List all possible positions.")
def positions(
    pretty: bool = PrettyFormat, sort_keys: bool = SortKeys, no_colors: bool = NoColors
):
    res = fetch(["positions"])
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)


@app.command(help="List all possible platforms.")
def platforms(
    pretty: bool = PrettyFormat, sort_keys: bool = SortKeys, no_colors: bool = NoColors
):
    res = fetch(["platforms"])
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)


@app.command(help="List all possible platforms.")
def power_play_strength(
    pretty: bool = PrettyFormat, sort_keys: bool = SortKeys, no_colors: bool = NoColors
):
    res = fetch(["powerPlayStrength"])
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)


@app.command(help="List all possible player league leader types.")
def league_leader_types(
    pretty: bool = PrettyFormat, sort_keys: bool = SortKeys, no_colors: bool = NoColors
):
    res = fetch(["leagueLeaderTypes"])
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)


@app.command(help="List all possible depth types for the stats leader endpoint.")
def depth_types(
    pretty: bool = PrettyFormat, sort_keys: bool = SortKeys, no_colors: bool = NoColors
):
    res = fetch(["depthTypes"])
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)


@app.command(help="List all possible image types for the logos.")
def image_types(
    pretty: bool = PrettyFormat, sort_keys: bool = SortKeys, no_colors: bool = NoColors
):
    res = fetch(["imageTypes"])
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)


@app.command(help="List all game types.")
def game_types(
    pretty: bool = PrettyFormat, sort_keys: bool = SortKeys, no_colors: bool = NoColors
):
    res = fetch(["gameTypes"])
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)


@app.command(help="List all possible series codes.")
def series_codes(
    pretty: bool = PrettyFormat, sort_keys: bool = SortKeys, no_colors: bool = NoColors
):
    res = fetch(["seriesCodes"])
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)


@app.command(help="List all the player status options.")
def player_status(
    pretty: bool = PrettyFormat, sort_keys: bool = SortKeys, no_colors: bool = NoColors
):
    res = fetch(["playerStatus"])
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)


@app.command(help="List all expands.")
def expands(
    pretty: bool = PrettyFormat, sort_keys: bool = SortKeys, no_colors: bool = NoColors
):
    res = fetch(["expands"])
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)


@app.command(help="List all possible schedule types.")
def schedule_types(
    pretty: bool = PrettyFormat, sort_keys: bool = SortKeys, no_colors: bool = NoColors
):
    res = fetch(["scheduleTypes"])
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)


@app.command(help="List all possible performer types.")
def performer_types(
    pretty: bool = PrettyFormat, sort_keys: bool = SortKeys, no_colors: bool = NoColors
):
    res = fetch(["performerTypes"])
    print_response(res, pretty=pretty, sort_keys=sort_keys, no_colors=no_colors)
