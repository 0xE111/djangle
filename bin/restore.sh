#!/bin/sh
set -e
zcat "$1" | docker-compose exec -T postgres sh -c 'psql -U postgres postgres'
echo "Restored $1"
