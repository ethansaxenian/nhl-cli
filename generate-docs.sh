# A script to generate docs using typer-cli

# typer-cli is currently incompatible with the latest versions of typer and black
# so remove them and temporarily install typer-cli (and its outdated dependencies)
poetry remove typer black
poetry add typer-cli

# rich_help_panel throws an error when generating docs
# so create a temporary copy of the cli and remove all occurances
TEXT_TO_REMOVE1=', rich_help_panel="Configurations Commands"'
TEXT_TO_REMOVE2='nhl\.'
TEXT_TO_REPLACE2='tmp\.'
cp -r nhl tmp
grep -rl $TEXT_TO_REMOVE1 tmp | LC_ALL=C xargs sed -i "" "s/$TEXT_TO_REMOVE1//g"
grep -rl $TEXT_TO_REMOVE2 tmp | LC_ALL=C xargs sed -i "" "s/$TEXT_TO_REMOVE2/$TEXT_TO_REPLACE2/g"

# generate the docs from the temporary cli and remove it
typer tmp/main.py utils docs --name nhl --output DOCS.md
rm -rf tmp

# finally, uninstall typer-cli and reinstall typer and black with latest versions
poetry remove typer-cli
poetry add typer
poetry add black -G dev
poetry lock
