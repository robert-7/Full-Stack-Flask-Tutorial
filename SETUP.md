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
which docker docker-compose
```

Then to set up a MongoDB container, simply run: `docker-compose up -d` and to hop into
the container and view the imported documents, run:

```bash
docker-compose exec mongodb bash
mongo UTA_Enrollment
db.getCollectionNames()
db.user.find()
```

To bring down the container, run `docker-compose down -v`.

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
