#!/bin/sh
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
ROOT="$(dirname "$SCRIPT_DIR")"
cd $ROOT

python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt -r requirements-local.txt

ln -s envs/local/docker-compose.yml
ln -s envs/local/.env
