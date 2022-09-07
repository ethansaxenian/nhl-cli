# `nhl`

An NHL API CLI

**Usage**:

```console
$ nhl [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `awards`: Get information about awards.
* `conferences`: Get information about NHL conferences.
* `configurations`: Get information about configurations.
* `divisions`: Get information about NHL divisions.
* `draft`: Get round-by-round data for the NHL Entry...
* `franchises`: Get information about NHL franchises.
* `prospects`: Get information about NHL Entry Draft...
* `schedule`: Get information about the schedule.
* `seasons`: Get information about NHL seasons.
* `standings`: Get information about standings.
* `teams`: Get information about NHL teams.
* `tournaments`: Get information about tournaments
* `venues`: Get information about venues.

## `nhl awards`

Get information about awards.

**Usage**:

```console
$ nhl awards [OPTIONS] [ID] COMMAND [ARGS]...
```

**Arguments**:

* `[ID]`: Returns information for a single award.  [default: ]

**Options**:

* `-e, --expand [awards.person|awards.team|awards.results]`: See 'nhl configurations expands' for details.  [default: ]
* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

## `nhl conferences`

Get information about NHL conferences.

**Usage**:

```console
$ nhl conferences [OPTIONS] [ID] COMMAND [ARGS]...
```

**Arguments**:

* `[ID]`: Returns information for a single conference.  [default: ]

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

## `nhl configurations`

Get information about configurations.

**Usage**:

```console
$ nhl configurations [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

**Commands**:

* `depth-types`: List all possible depth types for the stats...
* `event-types`: List all possible event types.
* `expands`: List all expands.
* `game-status`: List all status types.
* `game-types`: List all game types.
* `image-sizes`: List all possible image sizes for the logos.
* `image-types`: List all possible image types for the logos.
* `languages`: List all support languages.
* `league-leader-types`: List all possible player league leader types.
* `performer-types`: List all possible performer types.
* `platforms`: List all possible platforms.
* `play-types`: List all play types.
* `play-types-player`: List all play types for player.
* `player-status`: List all the player status options.
* `positions`: List all possible positions.
* `power-play-strength`: List all possible platforms.
* `prospect-categories`: List all possible draft prospect categories.
* `roster-statuses`: List all possible hockey roster statuses.
* `roster-types`: List all possible roster types.
* `schedule-types`: List all possible schedule types.
* `series-codes`: List all possible series codes.
* `site-language`: Lists all possible {language}_{site} params..
* `standings-types`: List all standings types.
* `stat-types`: List all stat types.
* `team-designations`: List all possible team designations.
* `tournament-types`: List all possible tournament types.

### `nhl configurations depth-types`

List all possible depth types for the stats leader endpoint.

**Usage**:

```console
$ nhl configurations depth-types [OPTIONS]
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

### `nhl configurations event-types`

List all possible event types.

**Usage**:

```console
$ nhl configurations event-types [OPTIONS]
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

### `nhl configurations expands`

List all expands.

**Usage**:

```console
$ nhl configurations expands [OPTIONS]
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

### `nhl configurations game-status`

List all status types.

**Usage**:

```console
$ nhl configurations game-status [OPTIONS]
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

### `nhl configurations game-types`

List all game types.

**Usage**:

```console
$ nhl configurations game-types [OPTIONS]
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

### `nhl configurations image-sizes`

List all possible image sizes for the logos.

**Usage**:

```console
$ nhl configurations image-sizes [OPTIONS]
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

### `nhl configurations image-types`

List all possible image types for the logos.

**Usage**:

```console
$ nhl configurations image-types [OPTIONS]
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

### `nhl configurations languages`

List all support languages.

**Usage**:

```console
$ nhl configurations languages [OPTIONS]
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

### `nhl configurations league-leader-types`

List all possible player league leader types.

**Usage**:

```console
$ nhl configurations league-leader-types [OPTIONS]
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

### `nhl configurations performer-types`

List all possible performer types.

**Usage**:

```console
$ nhl configurations performer-types [OPTIONS]
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

### `nhl configurations platforms`

List all possible platforms.

**Usage**:

```console
$ nhl configurations platforms [OPTIONS]
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

### `nhl configurations play-types`

List all play types.

**Usage**:

```console
$ nhl configurations play-types [OPTIONS]
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

### `nhl configurations play-types-player`

List all play types for player.

**Usage**:

```console
$ nhl configurations play-types-player [OPTIONS]
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

### `nhl configurations player-status`

List all the player status options.

**Usage**:

```console
$ nhl configurations player-status [OPTIONS]
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

### `nhl configurations positions`

List all possible positions.

**Usage**:

```console
$ nhl configurations positions [OPTIONS]
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

### `nhl configurations power-play-strength`

List all possible platforms.

**Usage**:

```console
$ nhl configurations power-play-strength [OPTIONS]
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

### `nhl configurations prospect-categories`

List all possible draft prospect categories.

**Usage**:

```console
$ nhl configurations prospect-categories [OPTIONS]
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

### `nhl configurations roster-statuses`

List all possible hockey roster statuses.

**Usage**:

```console
$ nhl configurations roster-statuses [OPTIONS]
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

### `nhl configurations roster-types`

List all possible roster types.

**Usage**:

```console
$ nhl configurations roster-types [OPTIONS]
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

### `nhl configurations schedule-types`

List all possible schedule types.

**Usage**:

```console
$ nhl configurations schedule-types [OPTIONS]
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

### `nhl configurations series-codes`

List all possible series codes.

**Usage**:

```console
$ nhl configurations series-codes [OPTIONS]
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

### `nhl configurations site-language`

Lists all possible {language}_{site} params..

**Usage**:

```console
$ nhl configurations site-language [OPTIONS]
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

### `nhl configurations standings-types`

List all standings types.

**Usage**:

```console
$ nhl configurations standings-types [OPTIONS]
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

### `nhl configurations stat-types`

List all stat types.

**Usage**:

```console
$ nhl configurations stat-types [OPTIONS]
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

### `nhl configurations team-designations`

List all possible team designations.

**Usage**:

```console
$ nhl configurations team-designations [OPTIONS]
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

### `nhl configurations tournament-types`

List all possible tournament types.

**Usage**:

```console
$ nhl configurations tournament-types [OPTIONS]
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

## `nhl divisions`

Get information about NHL divisions.

**Usage**:

```console
$ nhl divisions [OPTIONS] [ID] COMMAND [ARGS]...
```

**Arguments**:

* `[ID]`: Returns information for a single division.  [default: ]

**Options**:

* `-e, --expand [division.conference]`: See 'nhl configurations expands' for details.  [default: ]
* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

## `nhl draft`

Get round-by-round data for the NHL Entry Draft.

**Usage**:

```console
$ nhl draft [OPTIONS] [YEAR]:[%Y] COMMAND [ARGS]...
```

**Arguments**:

* `[YEAR]:[%Y]`: Specify the draft year.

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

## `nhl franchises`

Get information about NHL franchises.

**Usage**:

```console
$ nhl franchises [OPTIONS] [ID] COMMAND [ARGS]...
```

**Arguments**:

* `[ID]`: Returns information for a single team instead of the entire league.  [default: ]

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

## `nhl prospects`

Get information about NHL Entry Draft prospects.

**Usage**:

```console
$ nhl prospects [OPTIONS] [ID] COMMAND [ARGS]...
```

**Arguments**:

* `[ID]`: Returns information for a single prospect.  [default: ]

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

## `nhl schedule`

Get information about the schedule.

**Usage**:

```console
$ nhl schedule [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-e, --expand [schedule.linescore|schedule.scoringplays|schedule.decisions|schedule.teams|schedule.ticket|schedule.venue|schedule.broadcasts|schedule.broadcasts.all|schedule.radioBroadcasts|schedule.metadata|schedule.game.content.all|schedule.game.content.media.all|schedule.game.content.editorial.all|schedule.game.content.editorial.preview|schedule.game.content.editorial.recap|schedule.game.content.editorial.articles|schedule.game.content.media.epg|schedule.game.content.media.milestones|schedule.game.content.highlights.all|schedule.game.content.highlights.scoreboard|schedule.game.content.highlights.gamecenter|schedule.game.content.highlights.milestone|schedule.game.seriesSummary]`: See 'nhl configurations expands' for details.  [default: ]
* `--team-id TEXT`: Limit results to a specific team(s).  [default: ]
* `--date [%Y-%m-%d]`: Single defined date for the search.
* `--start-date [%Y-%m-%d]`: Start date for the search.
* `--end-date [%Y-%m-%d]`: End date for the search.
* `--season <DATETIME DATETIME>...`: Specify the season.  [default: (Uses the current season.)]
* `--game-type TEXT`: Restricts results to certain game types. See 'nhl configurations game-types' for options.
* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

## `nhl seasons`

Get information about NHL seasons.

**Usage**:

```console
$ nhl seasons [OPTIONS] [YEAR]... COMMAND [ARGS]...
```

**Arguments**:

* `[YEAR]...`: Specify the season. (ex: 2021 2022)  [default: (Shows all seasons.)]

**Options**:

* `--current`: Show the current season.  [default: False]
* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

## `nhl standings`

Get information about standings.

**Usage**:

```console
$ nhl standings [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-e, --expand [standings.team|standings.division|standings.conference|standings.record|standings.record.division|standings.record.conference|standings.record.overall]`: See 'nhl configurations expands' for details.  [default: ]
* `--season <DATETIME DATETIME>...`: Specify the season.  [default: (Uses the current season.)]
* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

## `nhl teams`

Get information about NHL teams.

**Usage**:

```console
$ nhl teams [OPTIONS] [ID] COMMAND [ARGS]...
```

**Arguments**:

* `[ID]`: Returns information for a single team instead of the entire league.  [default: ]

**Options**:

* `-e, --expand [team.league|team.stats|team.roster|team.division|team.conference|team.franchise|team.leaders|team.schedule.next|team.schedule.previous|team.ticket|team.content.home.all|team.record|team.playoffs|team.name|team.social|team.deviceProperties|team.content.sections]`: See 'nhl configurations expands' for details.  [default: ]
* `--season <DATETIME DATETIME>...`: Specify the season.  [default: (Uses the current season.)]
* `--team-id TEXT`: Can specify multiple team ids.  [default: ]
* `--roster`: Include the entire roster of a team.  [default: False]
* `--stats`: Include current season stats and the current season rankings for a specific team. (Note: Has no effect if --roster option is set.)  [default: False]
* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

## `nhl tournaments`

Get information about tournaments

**Usage**:

```console
$ nhl tournaments [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-e, --expand [round.series]`: See 'nhl configurations expands' for details.  [default: ]
* `--season <DATETIME DATETIME>...`: Specify the season.  [default: (Uses the current season.)]
* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.

## `nhl venues`

Get information about venues.

**Usage**:

```console
$ nhl venues [OPTIONS] [ID] COMMAND [ARGS]...
```

**Arguments**:

* `[ID]`: Returns information for a single venue.  [default: ]

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `--help`: Show this message and exit.
