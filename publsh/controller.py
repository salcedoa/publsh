import os
from datetime import datetime
import json
import yaml
import requests

CONFIG_FILE = os.path.expanduser("~/.config/publsh/publsh.yaml")
def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE, "r") as f:
        return yaml.safe_load(f) or {}

def create_post(post_input):
    """Simulate posting to an API."""
    now = datetime.now()
    sqlDatetime = now.strftime('%Y-%m-%d %H:%M:%S')

    postJSON = {
        "title": post_input[0],
        "body": ('\n'.join(post_input[1:])).rstrip(),
        "postTime": sqlDatetime
    }
    return send_post(postJSON)

def send_post(post):
    cfg = load_config()
    url = cfg.get("api_url", "http://localhost")
    if post["title"] != None:
      try:
        requests.post(url + "/json", json=post)
      except requests.exceptions.RequestException as e:
         return e
    else:
       return "Post must not be empty"
    return "Post uploaded!"


def edit_post(post_id):
    """Simulate editing a post."""
    cfg = load_config()
    api_url = cfg.get("api_url", "http://localhost")

def delete_post(post_id):
    cfg = load_config()
    api_url = cfg.get("api_url", "http://localhost/api/delete")
