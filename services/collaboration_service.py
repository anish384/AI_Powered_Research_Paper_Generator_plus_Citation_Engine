import google.generativeai as genai
from config import Config
import json
from datetime import datetime

class CollaborationService:
    def __init__(self):
        genai.configure(api_key=Config.GEMINI_API_KEY)
    
    def generate_peer_review_checklist(self, paper_type, field):
        """Generate comprehensive peer review checklist"""
        prompt = f"""
        Create a detailed peer review checklist for a {paper_type} in {field}:
        
        Include sections for:
        1. Content quality and originality
        2. Methodology rigor
        3. Literature review completeness
        4. Data analysis and interpretation
        5. Writing clarity and structure
        6. Ethical considerations
        7. Reproducibility factors
        8. Significance and impact
        
        Provide specific criteria and rating scales.
        """
        
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    
    def suggest_collaborators(self, research_topic, expertise_needed):
        """Suggest collaboration opportunities"""
        prompt = f"""
        For research on "{research_topic}" needing expertise in "{expertise_needed}"
        
        Suggest:
        1. Types of collaborators needed
        2. Complementary research areas
        3. Institutional partnerships
        4. International collaboration opportunities
        5. Industry partnerships
        6. Collaboration frameworks
        7. Resource sharing possibilities
        
        Include specific roles and contributions.
        """
        
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    
    def generate_conference_abstract(self, paper_content, conference_type):
        """Generate conference-specific abstracts"""
        prompt = f"""
        Based on this research: "{paper_content[:1000]}..."
        
        Create a {conference_type} conference abstract including:
        1. Compelling hook
        2. Research problem and significance
        3. Methodology overview
        4. Key findings
        5. Implications and impact
        6. Call to action
        
        Optimize for {conference_type} audience and format requirements.
        """
        
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    
    def generate_funding_proposal_outline(self, research_idea, funding_type):
        """Generate funding proposal structure"""
        prompt = f"""
        For research idea: "{research_idea}" seeking {funding_type} funding
        
        Create proposal outline with:
        1. Executive summary structure
        2. Problem statement framework
        3. Literature review approach
        4. Methodology and timeline
        5. Budget considerations
        6. Impact and dissemination plan
        7. Team qualifications
        8. Risk assessment
        
        Include specific sections and word count suggestions.
        """
        
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text