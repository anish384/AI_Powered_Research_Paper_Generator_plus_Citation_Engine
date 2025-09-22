import google.generativeai as genai
from config import Config
from .citation_service import CitationService
import re

class AIService:
    def __init__(self):
        genai.configure(api_key=Config.GEMINI_API_KEY)
        self.citation_service = CitationService()
    
    def generate_paper_content(self, topic, paper_type, length, outline=None):
        """Generate paper content using OpenAI"""
        
        length_words = {
            'short': '800-1200 words',
            'medium': '1500-2500 words',
            'long': '3000-5000 words',
            'extended': '5000+ words'
        }
        
        paper_prompts = {
            'research': "Write a comprehensive research paper",
            'review': "Write a detailed literature review",
            'essay': "Write an academic essay",
            'thesis': "Write a thesis chapter",
            'report': "Write a technical report"
        }
        
        prompt = f"""
        {paper_prompts.get(paper_type, 'Write a research paper')} on the topic: {topic}
        
        Requirements:
        - Length: {length_words.get(length, '1500-2500 words')}
        - Include proper academic structure with introduction, body, and conclusion
        - Use formal academic writing style
        - Include placeholder citations in the format [Author, Year]
        - Ensure logical flow and coherent arguments
        - Include specific examples and evidence where relevant
        
        Structure the paper with clear headings and subheadings.
        Make it comprehensive, well-researched, and academically rigorous.
        """
        
        try:
            model = genai.GenerativeModel("models/gemini-1.5-flash")
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating content: {str(e)}"
    
    def generate_outline(self, topic, paper_type):
        """Generate paper outline"""
        prompt = f"""
        Create a detailed outline for a {paper_type} on the topic: {topic}
        
        Include:
        - Main sections and subsections
        - Key points to cover in each section
        - Logical flow of arguments
        - Suggested research areas
        
        Format as a structured outline with Roman numerals, letters, and numbers.
        """
        
        try:
            model = genai.GenerativeModel("models/gemini-1.5-flash")
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating outline: {str(e)}"
    
    def generate_with_gemini(self, prompt, model_name="models/gemini-1.5-flash"):
        """Generate content using Google Gemini API"""
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error with Gemini API: {str(e)}"
    
    def enhance_paper_from_source(self, topic, source_content, paper_type="research"):
        """Generate enhanced paper content using source material"""
        prompt = f"""
        Create a comprehensive {paper_type} paper on "{topic}" using the following source material as reference:
        
        Source Content:
        {source_content}
        
        Requirements:
        - Expand on the concepts from the source material
        - Add proper academic structure and flow
        - Include critical analysis and synthesis
        - Maintain academic writing standards
        - Add placeholder citations where appropriate
        - Ensure originality while building on the source ideas
        """
        
        return self.generate_with_gemini(prompt)
    
    def generate_research_gaps_api(self, topic):
        """API endpoint for research gaps"""
        try:
            from .innovation_service import InnovationService
            innovation = InnovationService()
            gaps = innovation.generate_research_gaps(topic)
            return {'success': True, 'research_gaps': gaps}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def generate_paper_with_citations(self, topic, paper_type, length, citation_style='apa'):
        """Generate paper with real citations and bibliography"""
        # Search for relevant papers
        papers = self.citation_service.search_papers(topic, max_results=15)
        
        if not papers:
            return self.generate_paper_content(topic, paper_type, length)
        
        # Create citations list for the prompt
        citations_info = []
        for i, paper in enumerate(papers[:10], 1):
            citation = self.citation_service.format_citation(paper, citation_style)
            citations_info.append(f"[{i}] {citation}")
        
        length_words = {
            'short': '800-1200 words',
            'medium': '1500-2500 words', 
            'long': '3000-5000 words',
            'extended': '5000+ words'
        }
        
        paper_prompts = {
            'research': "Write a comprehensive research paper",
            'review': "Write a detailed literature review",
            'essay': "Write an academic essay",
            'thesis': "Write a thesis chapter",
            'report': "Write a technical report"
        }
        
        prompt = f"""
        {paper_prompts.get(paper_type, 'Write a research paper')} on the topic: {topic}
        
        Use these real academic sources and cite them appropriately:
        {chr(10).join(citations_info)}
        
        Requirements:
        - Length: {length_words.get(length, '1500-2500 words')}
        - Include proper academic structure with introduction, body, and conclusion
        - Use formal academic writing style
        - Cite the provided sources using [1], [2], etc. format throughout the text
        - Include a complete bibliography at the end in {citation_style.upper()} format
        - Ensure logical flow and coherent arguments
        - Reference specific findings and concepts from the provided sources
        
        Structure the paper with clear headings and subheadings.
        Make it comprehensive, well-researched, and academically rigorous.
        End with a "References" section listing all cited sources.
        """
        
        try:
            model = genai.GenerativeModel("models/gemini-1.5-flash")
            response = model.generate_content(prompt)
            content = response.text
            
            # Add bibliography if not present
            if "References" not in content and "Bibliography" not in content:
                content += "\n\n## References\n\n"
                for citation in citations_info:
                    content += f"{citation}\n\n"
            
            return content
        except Exception as e:
            return f"Error generating content with citations: {str(e)}"
    
    def enhance_citations_in_content(self, content, topic, citation_style='apa'):
        """Add real citations to existing content"""
        papers = self.citation_service.search_papers(topic, max_results=10)
        
        if not papers:
            return content
        
        # Find placeholder citations and replace with real ones
        placeholder_pattern = r'\[([^\]]+, \d{4})\]'
        placeholders = re.findall(placeholder_pattern, content)
        
        citations_info = []
        for i, paper in enumerate(papers[:len(placeholders) if placeholders else 8], 1):
            citation = self.citation_service.format_citation(paper, citation_style)
            citations_info.append(f"[{i}] {citation}")
        
        # Replace placeholders with numbered citations
        citation_counter = 1
        def replace_citation(match):
            nonlocal citation_counter
            if citation_counter <= len(citations_info):
                result = f"[{citation_counter}]"
                citation_counter += 1
                return result
            return match.group(0)
        
        enhanced_content = re.sub(placeholder_pattern, replace_citation, content)
        
        # Add bibliography
        if citations_info:
            enhanced_content += "\n\n## References\n\n"
            for citation in citations_info:
                enhanced_content += f"{citation}\n\n"
        
        return enhanced_content