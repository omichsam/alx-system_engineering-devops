#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""    
import requests

def number_of_subscribers(subreddit):
    # Reddit API endpoint for subreddit information
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {"User-Agent": "YourAppName/1.0"}

    # Make the request to the Reddit API
    response = requests.get(api_url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        try:
            # Parse the JSON response
            subreddit_info = response.json()

            # Extract and return the number of subscribers
            return subreddit_info["data"]["subscribers"]
        except (KeyError, ValueError):
            # Invalid JSON format or missing expected keys
            return 0
    elif response.status_code == 404:
        # Subreddit not found (invalid)
        return 0
    else:
        # Other error, print the status code for debugging
        print(f"Error: {response.status_code}")
        return 0

# Example usage:
subreddit_name = "python"
subscribers_count = number_of_subscribers(subreddit_name)

if subscribers_count > 0:
    print(f"The subreddit '{subreddit_name}' has {subscribers_count} subscribers.")
else:
    print(f"The subreddit '{subreddit_name}' is not valid or does not exist.")

