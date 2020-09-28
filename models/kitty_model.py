from db import db


class KittyModel(db.Model):
    __tablename__ = 'kitties_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    photo = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users_table.id'), nullable=False)

    def __init__(self, name, photo, user_id):
        self.name = name
        self.photo = photo
        self.user_id = user_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_user(cls, user_id):
        return cls.query.filter_by(user_id=user_id).all()

    def serialize_kitty(self):
        return {'kitty id': self.id, 'kitty name': self.name, 'kitty photo': self.photo}

    @classmethod
    def get_all_kitties(cls):
        return cls.query.all()
