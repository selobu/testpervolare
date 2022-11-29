#!/usr/bin/env bash

set -e
set -x

mypy app
# ruff app tests docs_src scripts
black app tests --check
#isort app tests docs_src scripts --check-only