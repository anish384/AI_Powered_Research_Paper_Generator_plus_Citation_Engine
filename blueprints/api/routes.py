from flask import request, jsonify, send_file
from . import api_bp
from services.paper_service import PaperService
from services.latex_service import LatexService
import json
import io

paper_service = PaperService()
latex_service = LatexService()

@api_bp.route('/generate-paper', methods=['POST'])
def generate_paper():
    try:
        data = request.get_json()
        
        topic = data.get('topic')
        paper_type = data.get('paper_type', 'research')
        length = data.get('length', 'medium')
        citation_style = data.get('citation_style', 'apa')
        include_references = data.get('include_references', True)
        
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400
        
        # Generate paper
        result = paper_service.generate_paper(
            topic=topic,
            paper_type=paper_type,
            length=length,
            citation_style=citation_style,
            include_references=include_references
        )
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/generate-latex', methods=['POST'])
def generate_latex():
    try:
        data = request.get_json()
        paper_content = data.get('paper_content')
        title = data.get('title')
        author = data.get('author', 'Research Assistant')
        
        if not paper_content:
            return jsonify({'error': 'Paper content is required'}), 400
        
        latex_content = latex_service.generate_latex(
            content=paper_content,
            title=title,
            author=author
        )
        
        return jsonify({'latex_content': latex_content})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/download-latex', methods=['POST'])
def download_latex():
    try:
        data = request.get_json()
        latex_content = data.get('latex_content')
        filename = data.get('filename', 'research_paper.tex')
        
        if not latex_content:
            return jsonify({'error': 'LaTeX content is required'}), 400
        
        # Create a file-like object
        latex_file = io.BytesIO()
        latex_file.write(latex_content.encode('utf-8'))
        latex_file.seek(0)
        
        return send_file(
            latex_file,
            as_attachment=True,
            download_name=filename,
            mimetype='text/plain'
        )
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/search-citations', methods=['POST'])
def search_citations():
    try:
        data = request.get_json()
        query = data.get('query')
        max_results = data.get('max_results', 5)
        
        if not query:
            return jsonify({'error': 'Query is required'}), 400
        
        citations = paper_service.search_citations(query, max_results)
        return jsonify({'citations': citations})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/analyze-topic', methods=['POST'])
def analyze_topic():
    """Analyze topic and provide insights"""
    try:
        data = request.get_json()
        topic = data.get('topic')
        
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400
        
        # Mock analysis - in real app, use AI
        analysis = {
            'scope': 'Well-defined topic with good research potential',
            'sections': [
                'Introduction and Background',
                'Literature Review',
                'Current State of Research',
                'Key Findings and Analysis',
                'Future Directions',
                'Conclusion'
            ],
            'estimated_length': '2500-4000 words',
            'difficulty': 'Intermediate',
            'research_areas': [
                'Primary research',
                'Case studies',
                'Statistical analysis',
                'Expert interviews'
            ]
        }
        
        return jsonify(analysis)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/save-draft', methods=['POST'])
def save_draft():
    """Save paper draft"""
    try:
        data = request.get_json()
        draft_id = data.get('id') or f"draft_{int(time.time())}"
        
        # In a real app, save to database
        # For now, just return success
        return jsonify({
            'success': True,
            'draft_id': draft_id,
            'message': 'Draft saved successfully'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/export-pdf', methods=['POST'])
def export_pdf():
    """Export paper to PDF (placeholder)"""
    try:
        data = request.get_json()
        content = data.get('content')
        title = data.get('title', 'Research Paper')
        
        # Placeholder - would integrate with PDF generation service
        return jsonify({
            'success': True,
            'message': 'PDF export feature coming soon!',
            'download_url': None
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
