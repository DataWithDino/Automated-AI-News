from . import db

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    published_date = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Text)

class ResearchPaper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    authors = db.Column(db.String(255), nullable=False)
    published_date = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Text)

class CodeBase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    repo_name = db.Column(db.String(255), nullable=False)
    repo_url = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    code_snippets = db.Column(db.Text)
    summary = db.Column(db.Text)
