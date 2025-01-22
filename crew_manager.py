# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 13:59:59 2025

@author: gowtham.balachan
"""

from crewai import Agent, Task, Crew

class CrewManager:
    """Class responsible for creating and managing AI news analysis crew"""
    
    @staticmethod
    def create_ai_news_crew(llm, filtered_content: dict) -> Crew:
        """
        Create a crew of agents for content analysis and article generation
        
        Args:
            llm: Language model instance
            filtered_content: Dictionary containing filtered content from different platforms
            
        Returns:
            Configured Crew instance
        """
        # Create Content Analyzer Agent
        analyzer = Agent(
            role='AI News Analyzer',
            goal='Identify and analyze significant AI developments and news from social media content',
            backstory="""Expert in AI technology with deep understanding of the field. 
                        Skilled at identifying genuine AI developments while filtering out 
                        speculation and controversial content.""",
            llm=llm,
            verbose=True
        )
        
        # Create Article Writer Agent
        writer = Agent(
            role='LinkedIn Article Writer',
            goal='Create professional, well-referenced LinkedIn articles about AI developments',
            backstory="""Professional tech writer specializing in AI content. 
                        Skilled at creating engaging, factual articles with proper attribution 
                        and clear references.""",
            llm=llm,
            verbose=True
        )
        
        # Create Analysis Task
        analysis_task = Task(
            description=f"""
            Analyze the provided social media content and:
            1. Identify significant AI developments and news
            2. Filter out controversial or speculative content
            3. Group related information by topics
            4. Verify information across multiple sources when available
            
            Content to analyze: {filtered_content}
            
            Focus on:
            - New AI technology releases
            - Research breakthroughs
            - Industry updates
            - Educational resources
            - Development tools and frameworks
            
            Exclude:
            - Controversial AI discussions
            - Unverified claims
            - Personal opinions without backing
            - Political content
            """,
            agent=analyzer,
            expected_output="""Structured analysis of AI developments including:
                - Key trends and announcements
                - Verified developments
                - Sources and references
                - Grouped themes and topics
                - References"""
        )
        
        # Create Writing Task
        writing_task = Task(
            description="""
            Create a professional LinkedIn article that:
            1. Presents key AI developments and news clearly
            2. Includes proper attribution with links to sources
            3. Maintains professional tone
            4. Organizes information logically
            5. Adds valuable context when needed
            
            Format:
            - Title: Clear and specific to the main developments
            - Introduction: Overview of key points
            - Body: Organized by topics/developments
            - Each point includes source reference
            - Conclusion: Summary of implications
            
            Length: 400-600 words
            """,
            agent=writer,
            expected_output="""A professional LinkedIn article with:
                - Clear title
                - Structured sections
                - Source attributions
                - Key AI developments
                - Professional tone""",
            context=[analysis_task]
        )
        
        # Create and return the crew
        return Crew(
            agents=[analyzer, writer],
            tasks=[analysis_task, writing_task],
            process="sequential",
            verbose=True
        )