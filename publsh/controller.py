import os
from datetime import datetime
import json
import yaml
import requests
from urllib.parse import urljoin

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
    base_url = f"{cfg.get('api_url')}:{cfg.get('port')}"
    url = urljoin(base_url, "json")
    print("Sending to",url)
    if post["title"] != None:
      try:
        requests.post(url, json=post)
        return "Post uploaded!"
      except requests.exceptions.RequestException as e:
         return f"Error connecting to server: {e}"
    else:
       return "Post must not be empty"


# To edit a post, post data must be retrieved first
def get_post_data(post_id):
    cfg = load_config()
    base_url = f"{cfg.get('api_url')}:{cfg.get('port')}"
    url = f"{base_url}/post/{post_id}"

    # Fetch post data
    response = requests.get(url)
    if not response.ok:
        return

    post = response.json()
    original_text = f"{post['title']}\n{post["body"]}"
    return original_text

def edit_post(post_id, edited_text):
    cfg = load_config()
    base_url = f"{cfg.get('api_url')}:{cfg.get('port')}"
    url = f"{base_url}/edit/{post_id}"

    now = datetime.now()
    sqlDatetime = now.strftime('%Y-%m-%d %H:%M:%S')

    postJSON = {
        "title": edited_text[0],
        "body": ('\n'.join(edited_text[1:])).rstrip(),
        "postTime": sqlDatetime
    }

    try:
        requests.put(url, json=postJSON)
        return "Post edited!"
    except requests.exceptions.RequestException as e:
        return f"Error connecting to server: {e}"


def delete_post(post_id):
    cfg = load_config()
    base_url = f"{cfg.get('api_url')}:{cfg.get('port')}"
    url = f"{base_url}/delete/{post_id}"
    try:
        response = requests.delete(url)
        if response.ok:
            return f"Post #{post_id} deleted"
        else:
            return f"Failed to delete post #{post_id}: {response.status_code} {response.text}"
    except requests.exceptions.RequestException as e:
        return f"Error connecting to server: {e}"
