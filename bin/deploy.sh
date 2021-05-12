#!/bin/bash
set -e

docker-compose down
docker image prune -f
docker-compose up --remove-orphans -d
