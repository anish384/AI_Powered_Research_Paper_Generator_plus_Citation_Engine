from flask import Blueprint, request, jsonify
from services.paper_service import PaperService

innovation_bp = Blueprint('innovation', __name__)
paper_service = PaperService()

@innovation_bp.route('/enhanced-paper', methods=['POST'])
def generate_enhanced_paper():
    """Generate paper with innovative features"""
    try:
        data = request.get_json()
        topic = data.get('topic')
        paper_type = data.get('paper_type', 'research')
        length = data.get('length', 'medium')
        
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400
        
        result = paper_service.generate_enhanced_paper(topic, paper_type, length)
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@innovation_bp.route('/analyze-quality', methods=['POST'])
def analyze_quality():
    """Analyze paper quality"""
    try:
        data = request.get_json()
        content = data.get('content')
        
        if not content:
            return jsonify({'error': 'Content is required'}), 400
        
        result = paper_service.analyze_paper_quality(content)
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@innovation_bp.route('/research-proposal', methods=['POST'])
def generate_proposal():
    """Generate research proposal"""
    try:
        data = request.get_json()
        research_idea = data.get('research_idea')
        funding_type = data.get('funding_type', 'academic')
        
        if not research_idea:
            return jsonify({'error': 'Research idea is required'}), 400
        
        result = paper_service.generate_research_proposal(research_idea, funding_type)
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@innovation_bp.route('/counterarguments', methods=['POST'])
def generate_counterarguments():
    """Generate counterarguments"""
    try:
        data = request.get_json()
        main_argument = data.get('main_argument')
        topic = data.get('topic')
        
        if not main_argument or not topic:
            return jsonify({'error': 'Main argument and topic are required'}), 400
        
        result = paper_service.innovation_service.generate_counterarguments(main_argument, topic)
        return jsonify({'success': True, 'counterarguments': result})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@innovation_bp.route('/research-gaps', methods=['POST'])
def find_research_gaps():
    """Find research gaps"""
    try:
        data = request.get_json()
        topic = data.get('topic')
        
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400
        
        result = paper_service.innovation_service.generate_research_gaps(topic)
        return jsonify({'success': True, 'research_gaps': result})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500