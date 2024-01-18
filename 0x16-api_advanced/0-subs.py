#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """Queries to Reddit API"""

    # Updated User-Agent, client ID, and client Secret
    u_agent = 'evah/1.0 (by /u/Rude-Entrepreneur52)'
    client_id = 'vkP5KBd-vWbZS_9JvQkzRw'
    client_secret = 'BmDfHc4nRAHa0GiG9B2M3ZwQfI4HMA'

    headers = {
        'User-Agent': u_agent,
        'Authorization': f'Basic {client_id}:{client_secret}'
    }

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    res = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response status code is not 200
    if res.status_code != 200:
        return 0

    try:
        # Attempt to parse JSON only if content is not empty
        dic = res.json()
    except ValueError:
        print("Error: Unable to parse JSON response.")
        return 0

    if 'data' not in dic:
        return 0
    if 'subscribers' not in dic.get('data'):
        return 0

    return dic['data']['subscribers']
