[...put project description here...]



> This project uses "djangle" template for developing & deployment. See instructions below.

----------------------------------------------------------------

# Cheatsheet

Djangle is a template which simplifies development & deployment of django apps. It's based on docker & docker-compose.

## Start new project locally

This covers case when you want to start completely new project and don't have any code yet.

First, create a project folder and init git repo:

```sh
mkdir new_project && cd new_project
git init
git config user.name "your name"
git config user.email "your email"
```

Then, set up `djangle` as one of remotes, and pull latest version. This will create a branch named `djangle/template` which is a skeleton for any new project:

```sh
git remote add djangle git@github.com:c0ntribut0r/djangle.git
git fetch --all
```

Now you have a `djangle/template` branch which contains latest `djangle` configuration and which you may use to generate project structure. Your `master` branch is still empty, let's populate if from `djangle/template` branch:

```sh
git merge djangle/template
```

Almost done! Now you can setup python venv for local development:

```sh
python -m venv venv
source venv/bin/activate
pip install --upgrade pip -r requirements.txt
```

Now you should be able to start development. Launch containers in foreground:

```sh
# run from project root folder; may require sudo
docker-compose up redis postgres
```

Switch to another terminal, activate venv and run dev Django server:

```sh
source venv/bin/activate
src/manage.py migrate
src/manage.py runserver
```

Visit http://127.0.0.1:8000 and ensure that you may see greetings page.

## Set up server

```sh
# on server
apt-get update && apt-get upgrade
apt-get install fish docker-compose git rsync
chsh -s /usr/bin/fish

NAME=project
mkdir $NAME && cd $NAME
git init
git config receive.denyCurrentBranch updateInstead
```

...

```sh
# on server
nano .git/hooks/post-receive

# ---
#!/bin/sh -eux
cd /root/project
sh bin/deploy.sh
# ---

chmod +x .git/hooks/post-receive
```

### Pull updates

### Deploy

### Update

### Manage

```sh
bin/django-manage.sh command \"arg with space\"
```
