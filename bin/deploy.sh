#!/bin/bash
set -e
docker-compose up --build --remove-orphans -d
docker-compose ps
