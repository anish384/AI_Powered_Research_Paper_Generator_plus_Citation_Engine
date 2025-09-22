from flask import render_template, request, jsonify
from . import paper_bp
from services.paper_service import PaperService

@paper_bp.route('/templates')
def templates():
    """Show available paper templates"""
    templates = [
        {'id': 'research', 'name': 'Research Paper', 'description': 'Academic research paper with methodology'},
        {'id': 'review', 'name': 'Literature Review', 'description': 'Comprehensive literature review'},
        {'id': 'essay', 'name': 'Academic Essay', 'description': 'Structured academic essay'},
        {'id': 'thesis', 'name': 'Thesis Chapter', 'description': 'Thesis or dissertation chapter'},
        {'id': 'report', 'name': 'Technical Report', 'description': 'Technical analysis report'}
    ]
    return jsonify({'templates': templates})

@paper_bp.route('/citation-styles')
def citation_styles():
    """Show available citation styles"""
    styles = [
        {'id': 'apa', 'name': 'APA 7th Edition', 'description': 'American Psychological Association'},
        {'id': 'mla', 'name': 'MLA 8th Edition', 'description': 'Modern Language Association'},
        {'id': 'chicago', 'name': 'Chicago Style', 'description': 'Chicago Manual of Style'},
        {'id': 'ieee', 'name': 'IEEE Style', 'description': 'Institute of Electrical and Electronics Engineers'},
        {'id': 'harvard', 'name': 'Harvard Style', 'description': 'Harvard Referencing System'}
    ]
    return jsonify({'citation_styles': styles})
