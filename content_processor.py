# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 13:38:02 2025

@author: gowtham.balachan
"""

from typing import List, Dict
import pandas as pd

class AIContentProcessor:
    """Class responsible for processing and filtering AI-related content from different platforms"""
    
    def __init__(self, llm):
        """
        Initialize the content processor
        
        Args:
            llm: Language model instance for content processing
        """
        self.llm = llm
        
    def filter_ai_content(self, twitter_df: pd.DataFrame, reddit_df: pd.DataFrame) -> Dict:
        """
        Filter and combine AI-related content from both Twitter and Reddit
        
        Args:
            twitter_df: DataFrame containing Twitter data
            reddit_df: DataFrame containing Reddit data
            
        Returns:
            Dictionary containing filtered content from both platforms
        """
        # Process Twitter content
        twitter_content = []
        for _, row in twitter_df.iterrows():
            content_data = {
                'text': row['tweettext'],
                'author': row['author'],
                'date': row['date'],
                'platform': 'Twitter',
                'url': f"https://twitter.com/{row['author']}/status/{row['id']}" if 'id' in row else None
            }
            twitter_content.append(content_data)
            
        # Process Reddit content
        reddit_content = []
        for _, row in reddit_df.iterrows():
            content_data = {
                'text': row['content'],
                'subreddit': row['subreddit'],
                'date': row['created_utc'],
                'platform': 'Reddit',
            }
            reddit_content.append(content_data)
            
        return {
            'twitter': twitter_content,
            'reddit': reddit_content
        }