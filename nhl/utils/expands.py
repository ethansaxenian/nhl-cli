from enum import Enum


class PersonExpands(str, Enum):
    person_stats = "person.stats"
    person_names = "person.names"
    person_currentTeam = "person.currentTeam"
    person_social = "person.social"
    person_awards = "person.awards"


class AwardsExpands(str, Enum):
    awards_person = "awards.person"
    awards_team = "awards.team"
    awards_results = "awards.results"


class RosterExpands(str, Enum):
    roster_person = "roster.person"


class StandingsExpands(str, Enum):
    standings_team = "standings.team"
    standings_division = "standings.division"
    standings_conference = "standings.conference"
    standings_record = "standings.record"
    standings_record_division = "standings.record.division"
    standings_record_conference = "standings.record.conference"
    standings_record_overall = "standings.record.overall"


class TeamExpands(str, Enum):
    team_league = "team.league"
    team_stats = "team.stats"
    team_roster = "team.roster"
    team_division = "team.division"
    team_conference = "team.conference"
    team_franchise = "team.franchise"
    team_leaders = "team.leaders"
    team_schedule_next = "team.schedule.next"
    team_schedule_previous = "team.schedule.previous"
    team_ticket = "team.ticket"
    team_content_home_all = "team.content.home.all"
    team_record = "team.record"
    team_playoffs = "team.playoffs"
    team_name = "team.name"
    team_social = "team.social"
    team_deviceProperties = "team.deviceProperties"
    team_content_sections = "team.content.sections"


class TournamentExpands(str, Enum):
    tournament_series_schedule = "tournament.series.schedule"


class ScheduleExpands(str, Enum):
    schedule_linescore = "schedule.linescore"
    schedule_scoringplays = "schedule.scoringplays"
    schedule_decisions = "schedule.decisions"
    schedule_teams = "schedule.teams"
    schedule_ticket = "schedule.ticket"
    schedule_venue = "schedule.venue"
    schedule_broadcasts = "schedule.broadcasts"
    schedule_broadcasts_all = "schedule.broadcasts.all"
    schedule_radioBroadcasts = "schedule.radioBroadcasts"
    schedule_metadata = "schedule.metadata"
    schedule_game_content_all = "schedule.game.content.all"
    schedule_game_content_media_all = "schedule.game.content.media.all"
    schedule_game_content_editorial_all = "schedule.game.content.editorial.all"
    schedule_game_content_editorial_preview = "schedule.game.content.editorial.preview"
    schedule_game_content_editorial_recap = "schedule.game.content.editorial.recap"
    schedule_game_content_editorial_articles = (
        "schedule.game.content.editorial.articles"
    )
    schedule_game_content_media_epg = "schedule.game.content.media.epg"
    schedule_game_content_media_milestones = "schedule.game.content.media.milestones"
    schedule_game_content_highlights_all = "schedule.game.content.highlights.all"
    schedule_game_content_highlights_scoreboard = (
        "schedule.game.content.highlights.scoreboard"
    )
    schedule_game_content_highlights_gamecenter = (
        "schedule.game.content.highlights.gamecenter"
    )
    schedule_game_content_highlights_milestone = (
        "schedule.game.content.highlights.milestone"
    )
    schedule_game_seriesSummary = "schedule.game.seriesSummary"


class SeriessummaryExpands(str, Enum):
    seriesSummary_series = "seriesSummary.series"


class GameExpands(str, Enum):
    game_team = "game.team"


class DecisionsExpands(str, Enum):
    decisions_person = "decisions.person"


class ScoringplaysExpands(str, Enum):
    scoringplays_person = "scoringplays.person"


class StatsExpands(str, Enum):
    stats_team = "stats.team"


class LeadersExpands(str, Enum):
    leaders_person = "leaders.person"
    leaders_team = "leaders.team"


class DivisionExpands(str, Enum):
    division_conference = "division.conference"


class RoundExpands(str, Enum):
    round_series = "round.series"


class SeriesExpands(str, Enum):
    series_conference = "series.conference"
    series_schedule = "series.schedule"
    series_round = "series.round"
    series_matchup_team = "series.matchup.team"
    series_games_team = "series.games.team"
