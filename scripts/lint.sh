#!/usr/bin/env bash

set -e
set -x

mypy app --follow-untyped-imports
ruff check app
ruff format app --check