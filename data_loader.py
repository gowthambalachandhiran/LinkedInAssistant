# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:01:20 2025

@author: gowtham.balachan
"""

import pandas as pd
from typing import Tuple

class DataLoader:
    """Class responsible for loading and validating input data"""
    
    @staticmethod
    def load_data(twitter_file: str, reddit_file: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Load and validate data from CSV files
        
        Args:
            twitter_file: Path to Twitter data CSV file
            reddit_file: Path to Reddit data CSV file
            
        Returns:
            Tuple containing Twitter and Reddit DataFrames
            
        Raises:
            FileNotFoundError: If input files are not found
            ValueError: If required columns are missing
            pd.errors.EmptyDataError: If input files are empty
        """
        try:
            # Load CSV files
            twitter_df = pd.read_csv(twitter_file, encoding='ISO-8859-1')
            reddit_df = pd.read_csv(reddit_file, encoding='ISO-8859-1')
            
            # Validate Twitter DataFrame columns
            required_twitter_cols = ['tweettext', 'author', 'date']
            if not all(col in twitter_df.columns for col in required_twitter_cols):
                raise ValueError(f"Twitter CSV must contain columns: {required_twitter_cols}")
                
            # Validate Reddit DataFrame columns
            required_reddit_cols = ['subreddit', 'content', 'created_utc']
            if not all(col in reddit_df.columns for col in required_reddit_cols):
                raise ValueError(f"Reddit CSV must contain columns: {required_reddit_cols}")
            
            return twitter_df, reddit_df
            
        except FileNotFoundError as e:
            print(f"Error: Could not find input file - {str(e)}")
            raise
        except pd.errors.EmptyDataError:
            print("Error: One or both input files are empty")
            raise
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            raise