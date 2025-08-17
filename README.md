# publsh - Microblogging for the terminal

Client CLI tool for [publsh-server](https://github.com/salcedoa/cli-blg).

## Installation
Set up on Linux/MacOS
```
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
pip install -e .
```

Config file set up:
```
mkdir -p ~/.config/publsh
touch ~/.config/publsh/publsh.yaml
```
Inside the config file (with example URL):
```
api_url: "http://127.0.0.1"
port: 5000
```

## Usage
To create a post
```
publsh
```
Then save and close the editor.

To edit a post by it's ID
```
publsh edit 2
```

To delete a post by it's ID
```
publsh delete 2
```