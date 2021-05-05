# Setup

The steps below are should help you get set up on an Ubuntu system.

```bash
# install python 3 and ensure python 3 is the default python version
sudo apt update
sudo apt install python3
echo -n '# python3 alias\nalias python=python3' '~/.bashrc' && source '~/.bashrc'
python --version

# install pip
curl 'https://bootstrap.pypa.io/get-pip.py' -o '/tmp/get-pip.py'
python '/tmp/get-pip.py'
pip --version

# install ruby for markdown linting
sudo apt install ruby
sudo gem install mdl

# verify virtualenv is installed
virtualenv --version

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
```

## Recurring

To deactivate or reactivate your virtual environment, simply run:

```bash
deactivate                # deactivates virtualenv
source .venv/bin/activate # reactivates virtualenv
```

To run the linter locally manually before commiting pushing, simply run:

```bash
pre-commit run --all-files
```
