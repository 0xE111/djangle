#!/bin/sh
set -e
target="data/$(date +%Y-%m-%d-%H-%M-%S).sql.gz"
docker-compose exec postgres pg_dump --clean -U postgres -d postgres | gzip > "$target"
echo "$target"
