# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:02:20 2025

@author: gowtham.balachan
"""

import os
from dotenv import load_dotenv
from data_loader import DataLoader
from llm_setup import LLMSetup
from content_processor import AIContentProcessor
from crew_manager import CrewManager
from article_generator import ArticleGenerator

def main():
    """Main execution function"""
    try:
        # Load environment variables
        load_dotenv()
        
        # Check for required environment variables
        if not os.getenv("GEMINI_API_KEY"):
            raise EnvironmentError("GEMINI_API_KEY not found in environment variables")
        
        # Initialize LLM
        print("Initializing LLM...")
        llm = LLMSetup.setup_llm()
        
        # Define input files
        twitter_file = "twitter_data.csv"
        reddit_file = "reddit_data.csv"
        
        # Load and validate data
        print("Loading data from CSV files...")
        twitter_df, reddit_df = DataLoader.load_data(twitter_file, reddit_file)
        
        print(f"Loaded {len(twitter_df)} tweets and {len(reddit_df)} Reddit posts")
        
        # Initialize components
        processor = AIContentProcessor(llm)
        crew_manager = CrewManager()
        article_generator = ArticleGenerator(processor, crew_manager)
        
        # Generate article
        print("Generating LinkedIn article...")
        article_text, filename = article_generator.generate_article(twitter_df, reddit_df, llm)
        
        # Print results
        print(f"\nArticle successfully generated and saved to: {filename}")
        print("\nArticle Preview:")
        print("="*50)
        preview_length = 500
        print(article_text[:preview_length] + "..." if len(article_text) > preview_length else article_text)
        print("="*50)
        
        return filename
        
    except Exception as e:
        print(f"Fatal error in main execution: {str(e)}")
        raise

if __name__ == "__main__":
    main()