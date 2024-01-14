# Setup

The steps below are should help you get set up on an Ubuntu system.

```bash
# install python 3 and dependencies
sudo apt update
sudo apt install build-essential libssl-dev libffi-dev python3 python-dev python3-pip python3-venv

# ensure python 3 is the default python version
cat >> ~/.bashrc << EOF

# python3 alias
alias python=python3
EOF
python --version

# install ruby for markdown linting
sudo apt install ruby
sudo gem install mdl

# clone repo
git clone git@github.com:robert-7/Full-Stack-Flask-Tutorial.git
cd Full-Stack-Flask-Tutorial

# set up virtualenv
python -m venv '.venv'
source .venv/bin/activate

# install requirements
pip install -r requirements.txt

# set up pre-commit so basic linting happens before every commit
pre-commit install
pre-commit run --all-files
```

## Installing MongoDB

Although the course instructs you to install MongoDB in your environment, I went down
the route of installing docker first for WSL2 and then spinning up a container for this.
Install following the installation commands
[here](https://docs.docker.com/docker-for-windows/wsl/). Verify the install with:

```bash
which docker
```

Then to set up a MongoDB container, simply run:

```bash
docker compose up -d
```

To hop into the `mongodb` container and view the imported documents, run:

```bash
# hop into our mongodb container, and begin a mongo shell with the UTA_Enrollment db selected
docker compose exec mongodb mongo UTA_Enrollment
db.getCollectionNames()
db.user.find()
```

To bring down the container, run `docker-compose down -v`.

## Install Mongo Compass

Unfortunately, for the time being, there are some steps that require Mongo Compass
(running on Windows, for me as a WSL2 user). As of writing this,
[mongodb-compass-1.41.0](https://downloads.mongodb.com/compass/mongodb-compass-1.41.0-win32-x64.exe)
is the latest version.

## Recurring

To deactivate or reactivate your virtual environment, simply run:

```bash
deactivate                # deactivates virtualenv
source .venv/bin/activate # reactivates virtualenv
```

Then spin up the Flask server separately (hoping to incorporate this into the docker
compose file):

```shell
flask run
```
