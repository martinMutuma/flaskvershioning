from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    questions = db.relationship('Question', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        if self.email and not self.query.filter_by(email=self.email).first():
            self.set_password(self.password)
            db.session.add(self)
            db.session.commit()
            return True
        else:
            return False

    def serialize(self):
        '''return an object as dictionary'''
        return dict(
            username=self.username,
            email=self.email,
        )
