from flask import Blueprint, request, jsonify
import logging
import time

api_bp = Blueprint('api', __name__)

@api_bp.route('/generate-paper', methods=['POST'])
def generate_paper():
    try:
        data = request.get_json()
        
        # Log the received data for debugging
        logging.info(f"Received paper generation request: {data}")
        
        # Validate required fields
        if not data.get('topic'):
            return jsonify({'error': 'Research topic is required'}), 400
            
        # Simulate processing time
        time.sleep(2)
        
        # Return a mock response for now
        response = {
            'status': 'success',
            'paper_id': 'mock_paper_123',
            'title': f"Research on {data['topic']}",
            'content': f"This is a mock research paper about {data['topic']}. "
                     f"The paper is of type {data.get('paper_type', 'research')} "
                     f"and has a length of {data.get('length', 'medium')}.",
            'citations': [
                {
                    'id': 'cite1',
                    'text': f'Author, A. (2023). Sample citation for {data["topic"]}. Journal of Research, 1(1), 1-10.',
                    'url': 'https://example.com'
                }
            ]
        }
        
        return jsonify(response)
        
    except Exception as e:
        logging.error(f"Error generating paper: {str(e)}")
        return jsonify({'error': str(e)}), 500
