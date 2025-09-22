import google.generativeai as genai
from config import Config
import json
import re
from datetime import datetime

class InnovationService:
    def __init__(self):
        genai.configure(api_key=Config.GEMINI_API_KEY)
    
    def generate_research_gaps(self, topic):
        """Identify research gaps and future directions"""
        prompt = f"""
        Analyze the current state of research on "{topic}" and identify:
        1. Key research gaps that need addressing
        2. Emerging trends and opportunities
        3. Methodological limitations in current studies
        4. Future research directions
        5. Interdisciplinary connections
        
        Format as structured sections with specific, actionable insights.
        """
        
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    
    def generate_counterarguments(self, main_argument, topic):
        """Generate balanced counterarguments and rebuttals"""
        prompt = f"""
        For the argument: "{main_argument}" in the context of "{topic}"
        
        Provide:
        1. Three strong counterarguments with evidence
        2. Potential rebuttals to each counterargument
        3. Areas of nuance and complexity
        4. Synthesis opportunities
        
        Maintain academic objectivity and intellectual rigor.
        """
        
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    
    def generate_methodology_suggestions(self, research_question, field):
        """Suggest innovative research methodologies"""
        prompt = f"""
        For research question: "{research_question}" in {field}
        
        Suggest:
        1. Traditional methodological approaches
        2. Innovative/emerging methodologies
        3. Mixed-methods approaches
        4. Digital/computational methods
        5. Ethical considerations
        6. Potential limitations and mitigation strategies
        
        Include specific tools, techniques, and frameworks.
        """
        
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    
    def generate_visual_abstracts(self, abstract_text):
        """Create visual abstract descriptions"""
        prompt = f"""
        Based on this abstract: "{abstract_text}"
        
        Create descriptions for:
        1. Key concept flowchart
        2. Data visualization suggestions
        3. Infographic elements
        4. Process diagrams
        5. Timeline representations
        
        Provide specific visual elements and layout suggestions.
        """
        
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    
    def generate_impact_assessment(self, research_topic, findings):
        """Assess potential research impact"""
        prompt = f"""
        For research on "{research_topic}" with findings: "{findings}"
        
        Analyze:
        1. Academic impact potential
        2. Industry/practical applications
        3. Policy implications
        4. Social impact
        5. Economic considerations
        6. Long-term significance
        7. Stakeholder benefits
        
        Provide specific examples and metrics where possible.
        """
        
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text