import requests
import json
import re
from datetime import datetime

class CitationService:
    def __init__(self):
        self.crossref_base_url = "https://api.crossref.org/works"
        self.arxiv_base_url = "http://export.arxiv.org/api/query"
    
    def search_papers(self, query, max_results=10):
        """Search for academic papers using CrossRef API"""
        try:
            params = {
                'query': query,
                'rows': max_results,
                'sort': 'relevance'
            }
            
            response = requests.get(self.crossref_base_url, params=params)
            response.raise_for_status()
            
            data = response.json()
            papers = []
            
            for item in data.get('message', {}).get('items', []):
                paper = self._parse_crossref_item(item)
                if paper:
                    papers.append(paper)
            
            return papers
        except Exception as e:
            print(f"Error searching papers: {e}")
            return []
    
    def _parse_crossref_item(self, item):
        """Parse CrossRef API response item"""
        try:
            title = item.get('title', ['Unknown Title'])[0] if item.get('title') else 'Unknown Title'
            
            authors = []
            if 'author' in item:
                for author in item['author']:
                    given = author.get('given', '')
                    family = author.get('family', '')
                    if given and family:
                        authors.append(f"{given} {family}")
            
            year = None
            if 'published-print' in item:
                year = item['published-print']['date-parts'][0][0]
            elif 'published-online' in item:
                year = item['published-online']['date-parts'][0][0]
            
            journal = item.get('container-title', [''])[0] if item.get('container-title') else ''
            doi = item.get('DOI', '')
            
            return {
                'title': title,
                'authors': authors,
                'year': year,
                'journal': journal,
                'doi': doi,
                'url': f"https://doi.org/{doi}" if doi else ''
            }
        except Exception as e:
            print(f"Error parsing paper: {e}")
            return None
    
    def format_citation(self, paper, style='apa'):
        """Format citation in specified style"""
        if not paper:
            return ""
        
        if style.lower() == 'apa':
            return self._format_apa(paper)
        elif style.lower() == 'mla':
            return self._format_mla(paper)
        elif style.lower() == 'chicago':
            return self._format_chicago(paper)
        else:
            return self._format_apa(paper)
    
    def _format_apa(self, paper):
        """Format citation in APA style"""
        authors = paper.get('authors', [])
        if not authors:
            author_str = "Unknown Author"
        elif len(authors) == 1:
            author_str = authors[0]
        elif len(authors) == 2:
            author_str = f"{authors[0]} & {authors[1]}"
        else:
            author_str = f"{authors[0]} et al."
        
        year = paper.get('year', 'n.d.')
        title = paper.get('title', 'Untitled')
        journal = paper.get('journal', '')
        
        citation = f"{author_str} ({year}). {title}."
        if journal:
            citation += f" *{journal}*."
        
        if paper.get('doi'):
            citation += f" https://doi.org/{paper['doi']}"
        
        return citation
    
    def _format_mla(self, paper):
        """Format citation in MLA style"""
        authors = paper.get('authors', [])
        if authors:
            author_str = authors[0]
        else:
            author_str = "Unknown Author"
        
        title = paper.get('title', 'Untitled')
        journal = paper.get('journal', '')
        year = paper.get('year', '')
        
        citation = f'{author_str}. "{title}."'
        if journal:
            citation += f" *{journal}*"
        if year:
            citation += f", {year}"
        citation += "."
        
        return citation
    
    def _format_chicago(self, paper):
        """Format citation in Chicago style"""
        authors = paper.get('authors', [])
        if authors:
            author_str = authors[0]
        else:
            author_str = "Unknown Author"
        
        title = paper.get('title', 'Untitled')
        journal = paper.get('journal', '')
        year = paper.get('year', '')
        
        citation = f'{author_str}. "{title}."'
        if journal:
            citation += f" *{journal}*"
        if year:
            citation += f" ({year})"
        citation += "."
        
        return citation
 
