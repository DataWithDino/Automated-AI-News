from ..models import db, Blog, ResearchPaper, CodeBase
from .elastic_utils import index_document
from .nlp import summarize_text  # Assuming you have an NLP utility for summarization

def ingest_blog(data):
    title = data['title']
    author = data['author']
    published_date = data['published_date']
    content = data['content']
    
    summary = summarize_text(content)
    
    blog = Blog(title=title, author=author, published_date=published_date, content=content, summary=summary)
    
    db.session.add(blog)
    db.session.commit()
    
    body = {
        'title': blog.title,
        'author': blog.author,
        'published_date': blog.published_date,
        'content': blog.content,
        'summary': blog.summary
    }
    index_document('blogs', '_doc', blog.id, body)

# Similarly, implement ingest functions for ResearchPaper and CodeBase
