# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:07:58 2025

@author: gowtham.balachan
"""

import praw
import pandas as pd
from datetime import datetime, timezone
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Reddit API credentials from environment variables
client_id = os.getenv('REDDIT_CLIENT_ID')
client_secret = os.getenv('REDDIT_CLIENT_SECRET')
user_agent = os.getenv('REDDIT_USER_AGENT')

# Validate credentials
if not all([client_id, client_secret, user_agent]):
    raise ValueError("Missing Reddit API credentials in environment variables")

# Initialize Reddit client
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

# Specify the subreddit and number of posts to fetch
subreddits = [
    'MachineLearning', 'technology', 'singularity',
    'ArtificialInteligence', 'compsci', 'DarkFuturology'
]
num_posts = 50  # Number of posts to fetch per subreddit

# Get today's start and end timestamps
today = datetime.now(timezone.utc).date()
start_of_today = datetime.combine(today, datetime.min.time(), tzinfo=timezone.utc).timestamp()
end_of_today = datetime.combine(today, datetime.max.time(), tzinfo=timezone.utc).timestamp()

# Fetch data
posts = []
processed_subreddits = []

try:
    for subreddit in subreddits:
        print(f"Processing subreddit: {subreddit}")
        for post in reddit.subreddit(subreddit).new(limit=num_posts):
            if start_of_today <= post.created_utc <= end_of_today:
                print(f"Found post for: {subreddit}")
                posts.append({
                    'subreddit': subreddit,
                    'title': post.title,
                    'author': post.author.name if post.author else 'Deleted',
                    'upvotes': post.score,
                    'comments': post.num_comments,
                    'created_utc': post.created_utc,
                    'url': post.url,
                    'content': post.selftext
                })
        processed_subreddits.append(subreddit)

except Exception as e:
    print(f"Error occurred: {e}")
    print(f"Subreddits processed before error: {processed_subreddits}")

# Create a DataFrame
df = pd.DataFrame(posts)

# Convert created_utc to datetime and save to CSV
if not df.empty:
    df['created_utc'] = pd.to_datetime(df['created_utc'], unit='s')
    output_file = 'reddit_data.csv'
    df.to_csv(output_file, index=False)
    print(f"DataFrame created with {len(df)} posts and saved to '{output_file}'")
else:
    print("No posts found for today.")

print(f"Processed Subreddits: {processed_subreddits}")
print(df.head())