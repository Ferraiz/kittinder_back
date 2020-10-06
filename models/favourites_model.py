from db import db


class FavouritesModel(db.Model):
    __tablename__ = 'favourites_table'

    id = db.Column(db.Integer, primary_key=True)
    kitty_name = db.Column(db.String(30))
    photo = db.Column(db.String(120))
    url = db.Column(db.String(180))
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users_table.id'), nullable=False)

    def __init__(self, kitty_name, user_id, photo=None, url=None):
        self.kitty_name = kitty_name
        self.photo = photo
        self.url = url
        self.user_id = user_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_user(cls, user_id):
        return cls.query.filter_by(user_id=user_id).all()

    def serialize_favourite(self):
        return {'kitty id': self.id, 'kitty name': self.kitty_name, 'kitty photo': self.photo, 'kitty url': self.url}
