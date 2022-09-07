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
* `configurations`: List all configuration endpoints.
* `depth-types`: List all possible depth types for the stats...
* `divisions`: Get information about NHL divisions.
* `draft`: Get round-by-round data for the NHL Entry...
* `event-types`: List all possible event types.
* `expands`: List all expands.
* `franchises`: Get information about NHL franchises.
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
* `prospects`: Get information about NHL Entry Draft...
* `roster-statuses`: List all possible hockey roster statuses.
* `roster-types`: List all possible roster types.
* `schedule`: Get information about the schedule.
* `schedule-types`: List all possible schedule types.
* `seasons`: Get information about NHL seasons.
* `series-codes`: List all possible series codes.
* `site-language`: Lists all possible {language}_{site} params.
* `standings`: Get information about standings.
* `standings-types`: List all standings types.
* `stat-types`: List all stat types.
* `team-designations`: List all possible team designations.
* `teams`: Get information about NHL teams.
* `tournament-types`: List all possible tournament types.
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

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `-e, --expand [awards.person|awards.team|awards.results]`: See 'nhl expands' for details.  [default: ]
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
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `--help`: Show this message and exit.

## `nhl configurations`

List all configuration endpoints.

**Usage**:

```console
$ nhl configurations [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `--help`: Show this message and exit.

## `nhl depth-types`

List all possible depth types for the stats leader endpoint.

**Usage**:

```console
$ nhl depth-types [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
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

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `-e, --expand [division.conference]`: See 'nhl expands' for details.  [default: ]
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
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `--help`: Show this message and exit.

## `nhl event-types`

List all possible event types.

**Usage**:

```console
$ nhl event-types [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `--help`: Show this message and exit.

## `nhl expands`

List all expands.

**Usage**:

```console
$ nhl expands [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
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
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `--help`: Show this message and exit.

## `nhl game-status`

List all status types.

**Usage**:

```console
$ nhl game-status [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `--help`: Show this message and exit.

## `nhl game-types`

List all game types.

**Usage**:

```console
$ nhl game-types [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `--help`: Show this message and exit.

## `nhl image-sizes`

List all possible image sizes for the logos.

**Usage**:

```console
$ nhl image-sizes [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `--help`: Show this message and exit.

## `nhl image-types`

List all possible image types for the logos.

**Usage**:

```console
$ nhl image-types [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `--help`: Show this message and exit.

## `nhl languages`

List all support languages.

**Usage**:

```console
$ nhl languages [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `--help`: Show this message and exit.

## `nhl league-leader-types`

List all possible player league leader types.

**Usage**:

```console
$ nhl league-leader-types [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `--help`: Show this message and exit.

## `nhl performer-types`

List all possible performer types.

**Usage**:

```console
$ nhl performer-types [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `--help`: Show this message and exit.

## `nhl platforms`

List all possible platforms.

**Usage**:

```console
$ nhl platforms [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `--help`: Show this message and exit.

## `nhl play-types`

List all play types.

**Usage**:

```console
$ nhl play-types [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `--help`: Show this message and exit.

## `nhl play-types-player`

List all play types for player.

**Usage**:

```console
$ nhl play-types-player [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `--help`: Show this message and exit.

## `nhl player-status`

List all the player status options.

**Usage**:

```console
$ nhl player-status [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `--help`: Show this message and exit.

## `nhl positions`

List all possible positions.

**Usage**:

```console
$ nhl positions [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `--help`: Show this message and exit.

## `nhl power-play-strength`

List all possible platforms.

**Usage**:

```console
$ nhl power-play-strength [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `--help`: Show this message and exit.

## `nhl prospect-categories`

List all possible draft prospect categories.

**Usage**:

```console
$ nhl prospect-categories [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
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
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `--help`: Show this message and exit.

## `nhl roster-statuses`

List all possible hockey roster statuses.

**Usage**:

```console
$ nhl roster-statuses [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `--help`: Show this message and exit.

## `nhl roster-types`

List all possible roster types.

**Usage**:

```console
$ nhl roster-types [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `--help`: Show this message and exit.

## `nhl schedule`

Get information about the schedule. By default, returns results for the current day.

**Usage**:

```console
$ nhl schedule [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `-e, --expand [schedule.linescore|schedule.scoringplays|schedule.decisions|schedule.teams|schedule.ticket|schedule.venue|schedule.broadcasts|schedule.broadcasts.all|schedule.radioBroadcasts|schedule.metadata|schedule.game.content.all|schedule.game.content.media.all|schedule.game.content.editorial.all|schedule.game.content.editorial.preview|schedule.game.content.editorial.recap|schedule.game.content.editorial.articles|schedule.game.content.media.epg|schedule.game.content.media.milestones|schedule.game.content.highlights.all|schedule.game.content.highlights.scoreboard|schedule.game.content.highlights.gamecenter|schedule.game.content.highlights.milestone|schedule.game.seriesSummary]`: See 'nhl expands' for details.  [default: ]
* `--team-id TEXT`: Limit results to a specific team(s).  [default: ]
* `--date [%Y-%m-%d]`: Single defined date for the search.
* `--start-date [%Y-%m-%d]`: Start date for the search.
* `--end-date [%Y-%m-%d]`: End date for the search.
* `--season <DATETIME DATETIME>...`: Specify the season.  [default: (Uses the current season.)]
* `--game-type TEXT`: Restricts results to certain game types. See 'nhl configurations game-types' for options.
* `--help`: Show this message and exit.

## `nhl schedule-types`

List all possible schedule types.

**Usage**:

```console
$ nhl schedule-types [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
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

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `--current`: Show the current season.  [default: False]
* `--help`: Show this message and exit.

## `nhl series-codes`

List all possible series codes.

**Usage**:

```console
$ nhl series-codes [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `--help`: Show this message and exit.

## `nhl site-language`

Lists all possible {language}_{site} params.

**Usage**:

```console
$ nhl site-language [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `--help`: Show this message and exit.

## `nhl standings`

Get information about standings.

**Usage**:

```console
$ nhl standings [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `-e, --expand [standings.team|standings.division|standings.conference|standings.record|standings.record.division|standings.record.conference|standings.record.overall]`: See 'nhl expands' for details.  [default: ]
* `--season <DATETIME DATETIME>...`: Specify the season.  [default: (Uses the current season.)]
* `--help`: Show this message and exit.

## `nhl standings-types`

List all standings types.

**Usage**:

```console
$ nhl standings-types [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `--help`: Show this message and exit.

## `nhl stat-types`

List all stat types.

**Usage**:

```console
$ nhl stat-types [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `--help`: Show this message and exit.

## `nhl team-designations`

List all possible team designations.

**Usage**:

```console
$ nhl team-designations [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
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

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `-e, --expand [team.league|team.stats|team.roster|team.division|team.conference|team.franchise|team.leaders|team.schedule.next|team.schedule.previous|team.ticket|team.content.home.all|team.record|team.playoffs|team.name|team.social|team.deviceProperties|team.content.sections]`: See 'nhl expands' for details.  [default: ]
* `--season <DATETIME DATETIME>...`: Specify the season.  [default: (Uses the current season.)]
* `--team-id TEXT`: Can specify multiple team ids.  [default: ]
* `--roster`: Include the entire roster of a team.  [default: False]
* `--stats`: Include current season stats and the current season rankings for a specific team. (Note: Has no effect if --roster option is set.)  [default: False]
* `--help`: Show this message and exit.

## `nhl tournament-types`

List all possible tournament types.

**Usage**:

```console
$ nhl tournament-types [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `--help`: Show this message and exit.

## `nhl tournaments`

Get information about tournaments

**Usage**:

```console
$ nhl tournaments [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-p, --pretty`: Format output.  [default: False]
* `-s, --sort-keys`: Sort output.  [default: False]
* `-n, --no-colors`: Disable colored output.  [default: False]
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `-e, --expand [round.series]`: See 'nhl expands' for details.  [default: ]
* `--season <DATETIME DATETIME>...`: Specify the season.  [default: (Uses the current season.)]
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
* `-l, --locale [en_US|fr_CA|es_ES|cs_CS|sv_SV|sk_SK|de_DE|ru_RU|fi_FI]`: Set the language of the output. See 'nhl site-languages' for details  [default: en_US]
* `--help`: Show this message and exit.
