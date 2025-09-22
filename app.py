from flask import Flask
from flask_cors import CORS
from config import Config
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize CORS
    CORS(app)
    
    # Register Blueprints
    from blueprints.main import main_bp
    from blueprints.api import api_bp
    from blueprints.paper import paper_bp
    from blueprints.api.innovation_routes import innovation_bp
    
    @app.route('/oracle')
    def oracle_page():
        from flask import render_template
        return render_template('oracle.html')
    
    @app.route('/innovation')
    def innovation_page():
        from flask import render_template
        return render_template('innovation.html')
    
    @app.route('/trends')
    def trends_page():
        from flask import render_template
        return render_template('trends.html')
    
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(paper_bp, url_prefix='/paper')
    app.register_blueprint(innovation_bp, url_prefix='/api/innovation')
    
    from blueprints.api.oracle_routes import oracle_bp
    app.register_blueprint(oracle_bp, url_prefix='/api/oracle')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)

