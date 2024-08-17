from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import config

# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Load configurations
    app.config.from_object(config)
    
    # Initialize plugins
    db.init_app(app)
    
    # Import and register blueprints
    from .routes import main_bp
    app.register_blueprint(main_bp)
    
    return app
