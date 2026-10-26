#!/usr/bin/env bash
# Build step run by Vercel to collect static files.
set -euo pipefail

pip install -r requirements.txt
python src/manage.py collectstatic --noinput
