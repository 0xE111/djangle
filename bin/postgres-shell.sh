#!/bin/sh
docker-compose exec postgres psql -p "$POSTGRES_PORT" -U postgres postgres
