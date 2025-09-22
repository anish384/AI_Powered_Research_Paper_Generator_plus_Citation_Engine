import re
import os
from datetime import datetime

class LatexService:
    def __init__(self):
        self.template_dir = 'latex_templates'
    
    def generate_latex(self, content, title, author="Research Assistant"):
        """Generate LaTeX document from content"""
        
        # Clean and format content
        formatted_content = self._format_content_for_latex(content)
        
        # Load template
        template = self._load_template()
        
        # Replace placeholders
        latex_content = template.replace('{{TITLE}}', self._escape_latex(title))
        latex_content = latex_content.replace('{{AUTHOR}}', self._escape_latex(author))
        latex_content = latex_content.replace('{{DATE}}', datetime.now().strftime('%B %d, %Y'))
        latex_content = latex_content.replace('{{CONTENT}}', formatted_content)
        
        return latex_content
    
    def _load_template(self):
        """Load LaTeX template"""
        template = r"""
\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{natbib}
\usepackage{url}
\usepackage{hyperref}
\usepackage{geometry}
\usepackage{setspace}

\geometry{margin=1in}
\doublespacing

\title{{{TITLE}}}
\author{{{AUTHOR}}}
\date{{{DATE}}}

\begin{document}

\maketitle

\begin{abstract}
This research paper was generated using an AI-powered research assistant. The content provides a comprehensive analysis of the given topic with proper academic structure and formatting.
\end{abstract}

{{CONTENT}}

\end{document}
"""
        return template
    
    def _format_content_for_latex(self, content):
        """Format content for LaTeX"""
        if not content:
            return ""
        
        # Replace markdown-style headers with LaTeX sections
        content = re.sub(r'^# (.*?)$', r'\\section{\1}', content, flags=re.MULTILINE)
        content = re.sub(r'^## (.*?)$', r'\\subsection{\1}', content, flags=re.MULTILINE)
        content = re.sub(r'^### (.*?)$', r'\\subsubsection{\1}', content, flags=re.MULTILINE)
        
        # Handle bold and italic text
        content = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', content)
        content = re.sub(r'\*(.*?)\*', r'\\textit{\1}', content)
        
        # Handle citations
        content = re.sub(r'\[([^\]]+), (\d{4})\]', r'\\citep{\1\2}', content)
        
        # Escape special LaTeX characters
        content = self._escape_latex(content)
        
        # Handle paragraphs (double newlines)
        content = re.sub(r'\n\s*\n', r'\n\n', content)
        
        return content
    
    def _escape_latex(self, text):
        """Escape special LaTeX characters"""
        if not text:
            return ""
        
        # Escape special characters
        special_chars = {
            '&': r'\&',
            '%': r'\%',
            '$': r'\$',
            '#': r'\#',
            '^': r'\textasciicircum{}',
            '_': r'\_',
            '{': r'\{',
            '}': r'\}',
            '~': r'\textasciitilde{}',
            '\\': r'\textbackslash{}'
        }
        
        for char, replacement in special_chars.items():
            text = text.replace(char, replacement)
        
        return text
