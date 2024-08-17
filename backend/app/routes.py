from flask import Blueprint, request, jsonify
from .utils.data_ingestion import ingest_blog  # Implement similar functions for research papers and code bases
from .utils.elastic_utils import search_documents

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the AI News API!"})

@main_bp.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    results = search_documents('blogs', {
        'query': {
            'multi_match': {
                'query': query,
                'fields': ['title', 'content', 'summary']
            }
        }
    })
    return jsonify(results)

@main_bp.route('/ingest/blog', methods=['POST'])
def ingest_blog_endpoint():
    data = request.get_json()
    ingest_blog(data)
    return jsonify({"message": "Blog ingested successfully!"}), 201
