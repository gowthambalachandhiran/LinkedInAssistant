# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:08:24 2025

@author: gowtham.balachan
"""

import requests
import pandas as pd
from datetime import date
import time
import os
from dotenv import load_dotenv
from typing import List, Dict, Optional

# Load environment variables
load_dotenv()

# Get Twitter API credentials from environment variables
BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

# Validate credentials
if not BEARER_TOKEN:
    raise ValueError("Missing Twitter Bearer Token in environment variables")

def search_tweets(query: str, retries: int = 4, sleep_time: int = 30) -> Optional[List[Dict]]:
    """
    Searches for tweets using the Twitter API v2 with recursive rate limit handling.
    
    Args:
        query: The search query string
        retries: Number of retries for rate limit handling
        sleep_time: Time to sleep in seconds when rate limit is hit
    
    Returns:
        List of tweet data dictionaries or None if all retries are exhausted
    """
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    url = "https://api.twitter.com/2/tweets/search/recent"
    
    params = {
        "query": query,
        "tweet.fields": "created_at,text,author_id"
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 429 and retries > 0:  # Rate limit error
            print(f"Rate limit exceeded. Retrying in {sleep_time} seconds... (Retries remaining: {retries})")
            time.sleep(sleep_time)
            return search_tweets(query, retries - 1, sleep_time)
        else:
            print(f"HTTP error occurred for @{query.split(':')[1]}: {http_err}")
            return None
            
    except requests.exceptions.RequestException as err:
        print(f"Error occurred for @{query.split(':')[1]}: {err}")
        return None

    return response.json().get('data', [])

def fetch_tweets(handles: List[str]) -> pd.DataFrame:
    """
    Fetches tweets from specified Twitter handles for the current day.
    
    Args:
        handles: List of Twitter handles to query
    
    Returns:
        DataFrame containing today's tweets
    """
    today = date.today().strftime("%Y-%m-%d")
    all_tweets = []

    for handle in handles:
        print(f"Fetching tweets for @{handle}...")
        tweets = search_tweets(f"from:{handle}")
        
        if tweets is not None:
            for tweet in tweets:
                tweet_date = tweet['created_at'][:10]
                if tweet_date == today:
                    all_tweets.append({
                        "tweettext": tweet['text'],
                        "author": handle,
                        "date": tweet['created_at']
                    })
        else:
            print(f"Skipping @{handle} due to errors.")

    return pd.DataFrame(all_tweets)

def main():
    # List of Twitter handles to query
    handles = [
        'svpino', 'OpenAI', 'AndrewYNg', 'karpathy', 'drfeifei',
        'huggingface', 'ylecun', 'fchollet', 'KirkDBorne'
    ]

    # Fetch and process tweets
    tweets_df = fetch_tweets(handles)

    # Display the results
    if not tweets_df.empty:
        print("\nFetched Tweets:")
        print(tweets_df)
        
        # Save to CSV
        output_file = "todays_tweets.csv"
        tweets_df.to_csv(output_file, index=False)
        print(f"\nTweets saved to {output_file}")
    else:
        print("\nNo tweets found for today.")

if __name__ == "__main__":
    main()