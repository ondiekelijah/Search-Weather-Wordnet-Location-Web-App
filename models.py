from app import db

class Answers(db.Model):
    __tablename__ = "answers"
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    answer = db.Column(db.Text)
    category = db.Column(db.Text)

    def __repr__(self):
        return "<Answers %r>" % self.question
