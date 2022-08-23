from app import db
from app.routes import app
from app.models import Book

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Book=Book)

# from app import db
# from app.models import Book

# db.create_all()

# book = Book(author="Ezz", title="Cleaner Python", price=0.0)
# db.session.add(book)
# db.session.commit()

# book2 = Book(author="Ahmed", title="Python", price=10.99)
# db.session.add(book2)
# db.session.commit()