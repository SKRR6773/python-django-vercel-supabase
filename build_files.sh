#!/usr/bin/env bash
# Build step run by Vercel to collect static files.
set -euo pipefail

# Vercel's build Python is externally managed (PEP 668), so allow pip to
# install into it.
python3 -m pip install --break-system-packages -r requirements.txt
python3 src/manage.py collectstatic --noinput
