# Flask app initialization
from flask import Flask
from flask_caching import Cache

# Initialize cache
cache = Cache(config={
    'CACHE_TYPE': 'SimpleCache',
    'CACHE_DEFAULT_TIMEOUT': 300  # 5 minutes cache
})

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    
    # Initialize extensions
    cache.init_app(app)
    
    # Register blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    return app