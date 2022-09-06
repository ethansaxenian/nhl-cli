from enum import Enum


class PersonExpands(str, Enum):
    stats = "stats"
    names = "names"
    currentTeam = "currentTeam"
    social = "social"
    awards = "awards"


class AwardsExpands(str, Enum):
    person = "person"
    team = "team"
    results = "results"


class RosterExpands(str, Enum):
    person = "person"


class StandingsExpands(str, Enum):
    team = "team"
    division = "division"
    conference = "conference"
    record = "record"
    record_division = "record.division"
    record_conference = "record.conference"
    record_overall = "record.overall"


class TeamExpands(str, Enum):
    league = "league"
    stats = "stats"
    roster = "roster"
    division = "division"
    conference = "conference"
    franchise = "franchise"
    leaders = "leaders"
    schedule_next = "schedule.next"
    schedule_previous = "schedule.previous"
    ticket = "ticket"
    content_home_all = "content.home.all"
    record = "record"
    playoffs = "playoffs"
    name = "name"
    social = "social"
    deviceProperties = "deviceProperties"
    content_sections = "content.sections"


class TournamentExpands(str, Enum):
    series_schedule = "series.schedule"


class ScheduleExpands(str, Enum):
    linescore = "linescore"
    scoringplays = "scoringplays"
    decisions = "decisions"
    teams = "teams"
    ticket = "ticket"
    venue = "venue"
    broadcasts = "broadcasts"
    broadcasts_all = "broadcasts.all"
    radioBroadcasts = "radioBroadcasts"
    metadata = "metadata"
    game_content_all = "game.content.all"
    game_content_media_all = "game.content.media.all"
    game_content_editorial_all = "game.content.editorial.all"
    game_content_editorial_preview = "game.content.editorial.preview"
    game_content_editorial_recap = "game.content.editorial.recap"
    game_content_editorial_articles = "game.content.editorial.articles"
    game_content_media_epg = "game.content.media.epg"
    game_content_media_milestones = "game.content.media.milestones"
    game_content_highlights_all = "game.content.highlights.all"
    game_content_highlights_scoreboard = "game.content.highlights.scoreboard"
    game_content_highlights_gamecenter = "game.content.highlights.gamecenter"
    game_content_highlights_milestone = "game.content.highlights.milestone"
    game_seriesSummary = "game.seriesSummary"


class SeriessummaryExpands(str, Enum):
    series = "series"


class GameExpands(str, Enum):
    team = "team"


class DecisionsExpands(str, Enum):
    person = "person"


class ScoringplaysExpands(str, Enum):
    person = "person"


class StatsExpands(str, Enum):
    team = "team"


class LeadersExpands(str, Enum):
    person = "person"
    team = "team"


class DivisionExpands(str, Enum):
    conference = "conference"


class RoundExpands(str, Enum):
    series = "series"


class SeriesExpands(str, Enum):
    conference = "conference"
    schedule = "schedule"
    round = "round"
    matchup_team = "matchup.team"
    games_team = "games.team"
