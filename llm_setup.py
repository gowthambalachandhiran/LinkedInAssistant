# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:01:53 2025

@author: gowtham.balachan
"""

from crewai import LLM

class LLMSetup:
    """Class responsible for LLM initialization and configuration"""
    
    @staticmethod
    def setup_llm() -> LLM:
        """
        Initialize LLM using CrewAI's LLM wrapper
        
        Returns:
            Configured LLM instance
            
        Raises:
            Exception: If LLM initialization fails
        """
        try:
            return LLM(
                model="gemini/gemini-pro",
                temperature=0.7
            )
        except Exception as e:
            print(f"Error initializing LLM: {str(e)}")
            raise