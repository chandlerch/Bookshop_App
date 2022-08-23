import os
from . import create_app
from models import Book
from flask import jsonify

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

@app.route("/book/list", methods=["GET"])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_json() for book in books])

@app.route("/book/<int:isbn>", methods=["GET"])
def get_book(isbn):
    book = Book.query.get(isbn)
    if book is None:
        abort(404)
    return jsonify(book.to_json())