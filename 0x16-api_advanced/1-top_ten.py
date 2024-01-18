#!/usr/bin/python3
"""
A Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""
import requests

def top_ten(subreddit):
    """Queries to Reddit API"""
    # Updated User-Agent, client ID, and client Secret
    u_agent = 'evah/1.0 (by /u/Rude-Entrepreneur52)'
    client_id = 'vkP5KBd-vWbZS_9JvQkzRw'
    client_secret = 'BmDfHc4nRAHa0GiG9B2M3ZwQfI4HMA'

    headers = {
        'User-Agent': u_agent,
        'Authorization': f'Basic {client_id}:{client_secret}'
    }

    params = {
        'limit': 10
    }

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)
    if res.status_code != 200:
        print(None)
        return
    dic = res.json()
    hot_posts = dic['data']['children']
    if len(hot_posts) == 0:
        print(None)
    else:
        for post in hot_posts:
            print(post['data']['title'])
