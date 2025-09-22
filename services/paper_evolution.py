import google.generativeai as genai
from config import Config
import json

class PaperEvolution:
    def __init__(self):
        genai.configure(api_key=Config.GEMINI_API_KEY)
    
    def generate_paper_versions(self, base_paper, target_audiences):
        """Generate multiple versions for different audiences"""
        versions = {}
        
        for audience in target_audiences:
            prompt = f"""
            Adapt this paper for {audience} audience: "{base_paper[:500]}..."
            
            Adjustments needed:
            - Language complexity level
            - Technical depth
            - Examples and analogies
            - Focus areas
            - Conclusion emphasis
            
            Maintain core research integrity while optimizing for audience.
            """
            
            model = genai.GenerativeModel("models/gemini-1.5-flash")
            response = model.generate_content(prompt)
            versions[audience] = response.text
        
        return versions
    
    def create_research_timeline(self, topic):
        """Create interactive research timeline"""
        prompt = f"""
        Create a comprehensive research timeline for "{topic}":
        
        Format as JSON with:
        - year: timeline year
        - milestone: key development
        - impact_level: 1-5 scale
        - researchers: key contributors
        - breakthrough_type: theoretical/practical/methodological
        - future_implications: what this enabled
        
        Cover past 15 years and predict next 5 years.
        """
        
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    
    def generate_research_ecosystem_map(self, central_topic):
        """Map research ecosystem around topic"""
        prompt = f"""
        Create ecosystem map for "{central_topic}" research:
        
        Include:
        1. Core research areas (inner circle)
        2. Adjacent fields (middle circle)  
        3. Distant but connected areas (outer circle)
        4. Collaboration strength indicators
        5. Knowledge flow directions
        6. Emerging connection points
        7. Potential new pathways
        
        Format as structured relationship data.
        """
        
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    
    def simulate_paper_impact_scenarios(self, paper_concept):
        """Simulate different impact scenarios"""
        scenarios = ['conservative', 'moderate', 'breakthrough']
        results = {}
        
        for scenario in scenarios:
            prompt = f"""
            Simulate {scenario} impact scenario for: "{paper_concept}"
            
            Predict:
            - Citation trajectory (5-year)
            - Industry adoption timeline
            - Academic influence spread
            - Policy impact potential
            - Technology integration
            - Follow-up research spawned
            - Career impact for authors
            
            Provide specific metrics and timelines.
            """
            
            model = genai.GenerativeModel("models/gemini-1.5-flash")
            response = model.generate_content(prompt)
            results[scenario] = response.text
        
        return results
    
    def generate_research_mutation_paths(self, original_idea):
        """Generate how research idea could mutate/evolve"""
        prompt = f"""
        Show evolution paths for research idea: "{original_idea}"
        
        Generate 5 mutation paths:
        1. Technology-driven evolution
        2. Interdisciplinary fusion path
        3. Scale transformation (micro to macro)
        4. Application domain shift
        5. Methodology revolution path
        
        For each path show:
        - 3-step evolution sequence
        - Required catalysts
        - Potential obstacles
        - Timeline estimates
        - Impact amplification factors
        """
        
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text