#!/bin/sh
docker-compose logs --tail=100 -f $1
