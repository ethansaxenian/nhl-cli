# A script to generate docs using typer-cli

# typer-cli is currently incompatible with the latest versions of typer and black
# so remove them and temporarily install typer-cli (and its outdated dependencies)
poetry remove typer black
poetry add typer-cli

# rich_help_panel throws an error when generating docs
# so create a temporary copy of the cli and remove all occurrences
TMP_DIR=tmp
cp -r nhl $TMP_DIR
RICH_HELP_PANEL_TEXT='rich_help_panel="(.*)"'
grep -rlE $RICH_HELP_PANEL_TEXT $TMP_DIR | LC_ALL=C xargs sed -Ei "" "s/$RICH_HELP_PANEL_TEXT//g"

# refactor tmp module imports
OLD_MODULE_IMPORT="^from nhl"
TMP_MODULE_IMPORT="from $TMP_DIR"
grep -rlE $OLD_MODULE_IMPORT $TMP_DIR | LC_ALL=C xargs sed -Ei "" "s/$OLD_MODULE_IMPORT/$TMP_MODULE_IMPORT/g"

# generate the docs from the temporary cli and remove it
typer $TMP_DIR/main.py utils docs --name nhl --output DOCS.md
rm -rf $TMP_DIR

# finally, uninstall typer-cli and reinstall typer and black with latest versions
poetry remove typer-cli
poetry add typer
poetry add black -G dev
poetry lock
