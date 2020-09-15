from app import db


class UserModel(db.Model):
    __tablename__ = 'users_table'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40))
    password = db.Column(db.String(40))

    def __init__(self, user_email, user_password):
        self.user_email = user_email
        self.user_password = user_password

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
