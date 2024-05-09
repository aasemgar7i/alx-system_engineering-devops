#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The total number of subscribers of the subreddit. Returns 0 if the subreddit is invalid or does not exist.
    """
    # Construct the URL for the subreddit's about page
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Define custom User-Agent header to avoid potential issues with Reddit's API guidelines
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Send GET request to the subreddit's about page, prevent following redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response status code is 200 (OK), indicating a successful request
    if response.status_code == 200:
        # Parse the JSON response and extract the number of subscribers
        data = response.json().get("data")
        subscribers = data.get("subscribers")
        return subscribers
    else:
        # If the response status code is not 200, return 0
        return 0
