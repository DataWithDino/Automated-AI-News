from elasticsearch import Elasticsearch
from ..config import config

# Initialize Elasticsearch client
es = Elasticsearch([config.ELASTICSEARCH_URL])

def index_document(index_name, doc_type, doc_id, body):
    es.index(index=index_name, doc_type=doc_type, id=doc_id, body=body)

def search_documents(index_name, query):
    return es.search(index=index_name, body=query)
