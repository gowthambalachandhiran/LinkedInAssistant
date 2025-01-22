# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:00:41 2025

@author: gowtham.balachan
"""

from datetime import datetime
from typing import Tuple
import pandas as pd

class ArticleGenerator:
    """Class responsible for generating LinkedIn articles from processed content"""
    
    def __init__(self, processor, crew_manager):
        """
        Initialize the article generator
        
        Args:
            processor: Instance of AIContentProcessor
            crew_manager: Instance of CrewManager
        """
        self.processor = processor
        self.crew_manager = crew_manager
    
    def generate_article(self, twitter_df: pd.DataFrame, reddit_df: pd.DataFrame, llm) -> Tuple[str, str]:
        """
        Generate LinkedIn article from social media content
        
        Args:
            twitter_df: DataFrame containing Twitter data
            reddit_df: DataFrame containing Reddit data
            llm: Language model instance
            
        Returns:
            Tuple containing article text and filename
        """
        # Filter and combine content
        filtered_content = self.processor.filter_ai_content(twitter_df, reddit_df)
        
        # Create and run the crew
        crew = self.crew_manager.create_ai_news_crew(llm, filtered_content)
        result = crew.kickoff()
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"ai_linkedin_article_{timestamp}.md"
        
        # Save the article
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(result))
        
        return str(result), filename