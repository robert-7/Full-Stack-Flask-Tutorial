# Setup

The steps below are should help you get set up on an Ubuntu system.

```bash
# install python 3
sudo apt-get update
sudo apt-get install python3
python3 --version

# ensure python 3 is the default python version
echo -n '# python3 alias\nalias python=python3' '~/.bashrc' && source '~/.bashrc'

# install pip
curl 'https://bootstrap.pypa.io/get-pip.py' -o '/tmp/get-pip.py'
python '/tmp/get-pip.py'
pip --version

# verify virtualenv is installed
virtualenv --version

# install flask
pip install flask
pip list | grep 'Flask'

# clone repo
git clone git@github.com:robert-7/Full-Stack-Flask-Tutorial.git
cd Full-Stack-Flask-Tutorial

# set up virtualenv
python -m venv '.venv'
source .venv/bin/activate

# install flask, flask-wtf, and python-dotenv locally within virtualenv
pip install flask flask-wtf python-dotenv
ls -ld .venv/lib/python3.*/site-packages/{flask,flask_wtf,dotenv}
```

To deactivate and reactivate your virtual environment, simply run:

```bash
deactivate                # deactivates virtualenv
source .venv/bin/activate # reactivates virtualenv
```
