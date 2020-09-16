#!/usr/bin/env bash
set -e

printf '%20sinstall python code style linter%20s\n' | tr ' ' -
python3.8 -m pip install flake8

printf '%20scopy git hooks in git directory%20s\n' | tr ' ' -
cp -a git_hooks/. .git/hooks/

