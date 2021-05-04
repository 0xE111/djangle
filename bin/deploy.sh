#!/bin/bash

unset GIT_INDEX_FILE

export ROOT=/home/estateza
export DOMAIN=redatabase
export REPO=redatabase.git

while read oldrev newrev ref
do
    if [[ $ref =~ .*/master$ ]]; then
        export GIT_DIR="$ROOT/repos/$REPO/"
        export GIT_WORK_TREE="$ROOT/domains/$DOMAIN/"
        git checkout -f master
        cd $GIT_WORK_TREE
        ./deploy.sh
    else
        echo "Doing nothing: only the master branch can be deployed on this server."
    fi
done



docker-compose up --remove-orphans
