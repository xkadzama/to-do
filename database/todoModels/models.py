from database.engine import db


class Task(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String(100), nullable=False)

    def __repr__(self):
        return f'<Task {self.id}, {self.title}'

