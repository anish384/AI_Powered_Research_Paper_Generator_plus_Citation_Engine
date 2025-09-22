import google.generativeai as genai
from config import Config
import json
import re
from datetime import datetime, timedelta

class TrendPredictor:
    def __init__(self):
        genai.configure(api_key=Config.GEMINI_API_KEY)
    
    def predict_research_trends(self, field, timeframe="2024-2025"):
        """Predict emerging research trends"""
        prompt = f"""
        Analyze and predict research trends in {field} for {timeframe}:
        
        1. Emerging Technologies Impact
        2. Interdisciplinary Convergence Points
        3. Funding Pattern Shifts
        4. Methodological Innovations
        5. Societal Need Drivers
        6. Publication Trend Predictions
        7. Career Opportunity Areas
        
        Provide specific, actionable predictions with confidence levels.
        """
        
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    
    def generate_future_paper_concepts(self, current_topic):
        """Generate next-generation paper concepts"""
        prompt = f"""
        Based on current research in "{current_topic}", generate 5 innovative paper concepts for the next 2-3 years:
        
        For each concept provide:
        - Revolutionary angle/approach
        - Potential breakthrough implications
        - Required interdisciplinary collaboration
        - Timeline feasibility
        - Impact potential score (1-10)
        
        Focus on unexplored intersections and emerging paradigms.
        """
        
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    
    def analyze_research_evolution(self, topic):
        """Track how research topic has evolved"""
        prompt = f"""
        Trace the evolution of "{topic}" research:
        
        1. Historical milestones (past 10 years)
        2. Paradigm shifts and breakthroughs
        3. Current state analysis
        4. Emerging sub-fields
        5. Technology integration points
        6. Future trajectory predictions
        7. Potential disruption factors
        
        Create a research evolution timeline with key insights.
        """
        
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    
    def generate_research_fusion_ideas(self, field1, field2):
        """Generate fusion research ideas between two fields"""
        prompt = f"""
        Create innovative research fusion concepts between {field1} and {field2}:
        
        1. Novel intersection points
        2. Hybrid methodologies
        3. Cross-pollination opportunities
        4. Breakthrough potential areas
        5. Implementation challenges
        6. Success probability assessment
        7. Resource requirements
        
        Focus on unexplored combinations with high impact potential.
        """
        
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    
    def predict_citation_potential(self, paper_abstract):
        """Predict citation potential of research"""
        prompt = f"""
        Analyze this abstract and predict citation potential: "{paper_abstract}"
        
        Assess:
        1. Novelty factor (1-10)
        2. Practical applicability (1-10)
        3. Interdisciplinary appeal (1-10)
        4. Methodology innovation (1-10)
        5. Problem significance (1-10)
        6. Expected citation range (low/medium/high)
        7. Peak citation timeline
        8. Longevity prediction
        
        Provide detailed reasoning for each score.
        """
        
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text