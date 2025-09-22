from flask import Blueprint, request, jsonify
from services.research_oracle import ResearchOracle
from services.trend_predictor import TrendPredictor
from services.paper_evolution import PaperEvolution

oracle_bp = Blueprint('oracle', __name__)
oracle = ResearchOracle()
trend_predictor = TrendPredictor()
paper_evolution = PaperEvolution()

@oracle_bp.route('/divine', methods=['POST'])
def divine_future():
    """Consult the Research Oracle"""
    data = request.get_json()
    query = data.get('query')
    
    if not query:
        return jsonify({'error': 'Query required'}), 400
    
    try:
        prophecy = oracle.divine_research_future(query)
        return jsonify({'success': True, 'prophecy': prophecy})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@oracle_bp.route('/predict-trends', methods=['POST'])
def predict_trends():
    """Predict research trends"""
    data = request.get_json()
    field = data.get('field')
    timeframe = data.get('timeframe', '2024-2025')
    
    if not field:
        return jsonify({'error': 'Field required'}), 400
    
    try:
        trends = trend_predictor.predict_research_trends(field, timeframe)
        future_concepts = trend_predictor.generate_future_paper_concepts(field)
        
        return jsonify({
            'success': True,
            'trends': trends,
            'future_concepts': future_concepts
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@oracle_bp.route('/evolution-map', methods=['POST'])
def create_evolution_map():
    """Create research evolution map"""
    data = request.get_json()
    topic = data.get('topic')
    
    if not topic:
        return jsonify({'error': 'Topic required'}), 400
    
    try:
        timeline = paper_evolution.create_research_timeline(topic)
        ecosystem = paper_evolution.generate_research_ecosystem_map(topic)
        mutations = paper_evolution.generate_research_mutation_paths(topic)
        
        return jsonify({
            'success': True,
            'timeline': timeline,
            'ecosystem': ecosystem,
            'mutations': mutations
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@oracle_bp.route('/ultimate-vision', methods=['POST'])
def generate_ultimate_vision():
    """Generate ultimate research vision"""
    data = request.get_json()
    field = data.get('field')
    
    if not field:
        return jsonify({'error': 'Field required'}), 400
    
    try:
        vision = oracle.generate_ultimate_research_vision(field)
        mandala = oracle.create_research_mandala(field)
        
        return jsonify({
            'success': True,
            'ultimate_vision': vision,
            'research_mandala': mandala
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@oracle_bp.route('/synchronicity', methods=['POST'])
def predict_synchronicity():
    """Predict research synchronicities"""
    data = request.get_json()
    topic1 = data.get('topic1')
    topic2 = data.get('topic2')
    
    if not topic1 or not topic2:
        return jsonify({'error': 'Both topics required'}), 400
    
    try:
        sync = oracle.predict_research_synchronicities(topic1, topic2)
        fusion = trend_predictor.generate_research_fusion_ideas(topic1, topic2)
        
        return jsonify({
            'success': True,
            'synchronicity': sync,
            'fusion_ideas': fusion
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500