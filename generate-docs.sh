# A script to generate docs using typer-cli
# typer-cli is currently incompatible with the latest versions of typer and black
# so the solution is to uninstall conflicting packages, temporarily install typer-cli (and its outdated dependencies)
# generate the docs using typer-cli
# then uninstall typer-cli and reinstall the latest versions of typer and black

poetry remove typer black
poetry add typer-cli
typer nhl/main.py utils docs --name nhl --output DOCS.md
poetry remove typer-cli
poetry add typer
poetry add black -G dev
poetry lock
