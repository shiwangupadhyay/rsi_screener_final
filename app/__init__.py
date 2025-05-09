# Flask app initialization
from flask import Flask
from flask_caching import Cache

# Initialize extensions
cache = Cache(config={
    'CACHE_TYPE': 'SimpleCache',  # Use simple in-memory cache for development
    'CACHE_DEFAULT_TIMEOUT': 300  # Default cache timeout in seconds
})

def create_app():
    """Create and configure the Flask application"""
    app = Flask(__name__)
    
    # Configure the app
    app.config.from_object('config')
    
    # Initialize extensions with app
    cache.init_app(app)
    
    # Register blueprints
    from app.routes import main
    app.register_blueprint(main)
    
    return app