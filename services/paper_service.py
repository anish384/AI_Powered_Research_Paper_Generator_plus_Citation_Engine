from .ai_service import AIService
from .citation_service import CitationService
from .innovation_service import InnovationService
from .collaboration_service import CollaborationService
from .analytics_service import AnalyticsService
import json
import re

class PaperService:
    def __init__(self):
        self.ai_service = AIService()
        self.citation_service = CitationService()
        self.innovation_service = InnovationService()
        self.collaboration_service = CollaborationService()
        self.analytics_service = AnalyticsService()
    
    def generate_paper(self, topic, paper_type='research', length='medium', 
                      citation_style='apa', include_references=True):
        """Generate complete research paper"""
        
        result = {
            'success': False,
            'paper': {},
            'citations': [],
            'references': [],
            'outline': '',
            'word_count': 0
        }
        
        try:
            # Generate outline first
            outline = self.ai_service.generate_outline(topic, paper_type)
            result['outline'] = outline
            
            # Generate main content with citations
            if include_references:
                content = self.ai_service.generate_paper_with_citations(
                    topic, paper_type, length, citation_style
                )
            else:
                content = self.ai_service.generate_paper_content(
                    topic, paper_type, length, outline
                )
            
            # Extract title from content or generate one
            title = self._extract_title(content) or f"{paper_type.title()} on {topic}"
            
            # Get citations info if references were included
            citations = []
            references = []
            
            if include_references:
                citations = self.search_citations(topic, max_results=10)
                references = self._format_references(citations, citation_style)
            
            # Calculate word count
            word_count = len(content.split())
            
            result.update({
                'success': True,
                'paper': {
                    'title': title,
                    'content': content,
                    'topic': topic,
                    'type': paper_type,
                    'length': length,
                    'citation_style': citation_style
                },
                'citations': citations,
                'references': references,
                'word_count': word_count
            })
            
        except Exception as e:
            result['error'] = str(e)
        
        return result
    
    def search_citations(self, query, max_results=5):
        """Search for citations related to topic"""
        return self.citation_service.search_papers(query, max_results)
    
    def _extract_title(self, content):
        """Extract title from content"""
        lines = content.split('\n')
        for line in lines[:5]:  # Check first 5 lines
            line = line.strip()
            if line and not line.startswith('#') and len(line) < 100:
                return line
        return None
    
    def _insert_citations(self, content, citations):
        """Insert relevant citations into content"""
        if not citations:
            return content
        
        # Simple citation insertion based on keywords
        citation_patterns = [
            (r'(research shows|studies indicate|according to)', citations[:2]),
            (r'(recent findings|evidence suggests|data indicates)', citations[2:4]),
            (r'(scholars argue|experts believe|literature suggests)', citations[4:6])
        ]
        
        for i, (pattern, cites) in enumerate(citation_patterns):
            if cites:
                cite = cites[0] if cites else citations[0]
                authors = cite.get('authors', ['Unknown'])
                year = cite.get('year', 'n.d.')
                author_name = authors[0].split()[-1] if authors and authors[0] else 'Unknown'
                
                citation_text = f"({author_name}, {year})"
                content = re.sub(pattern, f"\\1 {citation_text}", content, count=1)
        
        return content
    
    def _format_references(self, citations, style):
        """Format citations as references"""
        references = []
        for citation in citations:
            formatted = self.citation_service.format_citation(citation, style)
            if formatted:
                references.append(formatted)
        return references
    
    def enhance_paper_citations(self, content, topic, citation_style='apa'):
        """Enhance existing paper content with real citations"""
        try:
            enhanced_content = self.ai_service.enhance_citations_in_content(
                content, topic, citation_style
            )
            return {
                'success': True,
                'content': enhanced_content,
                'word_count': len(enhanced_content.split())
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'content': content
            }
    
    def generate_enhanced_paper(self, topic, paper_type='research', length='medium'):
        """Generate paper with innovative features"""
        try:
            # Generate main paper
            paper_result = self.generate_paper(topic, paper_type, length)
            
            if not paper_result['success']:
                return paper_result
            
            content = paper_result['paper']['content']
            
            # Add innovative features
            research_gaps = self.innovation_service.generate_research_gaps(topic)
            methodology = self.innovation_service.generate_methodology_suggestions(f"Research on {topic}", "academic")
            impact_assessment = self.innovation_service.generate_impact_assessment(topic, "preliminary findings")
            
            # Analytics
            quality_score = self.analytics_service.generate_quality_score(content)
            suggestions = self.analytics_service.generate_improvement_suggestions(content)
            
            # Collaboration features
            peer_review_checklist = self.collaboration_service.generate_peer_review_checklist(paper_type, "general")
            
            paper_result.update({
                'research_gaps': research_gaps,
                'methodology_suggestions': methodology,
                'impact_assessment': impact_assessment,
                'quality_score': quality_score,
                'improvement_suggestions': suggestions,
                'peer_review_checklist': peer_review_checklist
            })
            
            return paper_result
            
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def analyze_paper_quality(self, content):
        """Comprehensive paper quality analysis"""
        try:
            readability = self.analytics_service.analyze_readability(content)
            argument_structure = self.analytics_service.analyze_argument_structure(content)
            quality_score = self.analytics_service.generate_quality_score(content)
            suggestions = self.analytics_service.generate_improvement_suggestions(content)
            
            return {
                'success': True,
                'readability': readability,
                'argument_structure': argument_structure,
                'quality_score': quality_score,
                'suggestions': suggestions
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def generate_research_proposal(self, research_idea, funding_type='academic'):
        """Generate comprehensive research proposal"""
        try:
            proposal_outline = self.collaboration_service.generate_funding_proposal_outline(research_idea, funding_type)
            methodology = self.innovation_service.generate_methodology_suggestions(research_idea, "research")
            impact_assessment = self.innovation_service.generate_impact_assessment(research_idea, "proposed research")
            
            return {
                'success': True,
                'proposal_outline': proposal_outline,
                'methodology': methodology,
                'impact_assessment': impact_assessment
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
