#!/bin/sh
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
ROOT="$(dirname "$SCRIPT_DIR")"
cd $ROOT

python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt -r envs/local/requirements.txt

ln -s envs/local/docker-compose.yml
cp envs/local/.envrc .envrc
