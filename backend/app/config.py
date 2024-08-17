import os

class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost/your_db_name')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Elasticsearch configuration
    ELASTICSEARCH_URL = os.getenv('ELASTICSEARCH_URL', 'http://localhost:9200')
    
    # Other configurations
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    DEBUG = os.getenv('FLASK_DEBUG', False)

config = Config()

