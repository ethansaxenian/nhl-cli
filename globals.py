from enum import Enum

import typer

PrettyFormat = typer.Option(False, "--pretty", help="Format output.")

SortKeys = typer.Option(False, "--sort-keys", help="Sort output.")


class TeamsExpand(str, Enum):
    team_roster = "team.roster"
    person_names = "person.names"
    team_schedule_next = "team.schedule.next"
    team_schedule_previous = "team.schedule.previous"
    team_stats = "team.stats"
