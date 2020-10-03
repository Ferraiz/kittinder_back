from db import db


class FavouritesModel(db.Model):
    __tablename__ = 'favourites_table'

    id = db.Column(db.Integer, primary_key=True)
    kitty_name = db.Column(db.String(30))
    photo = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users_table.id'), nullable=False)

    def __init__(self, name, photo, user_id):
        self.name = name
        self.photo = photo
        self.user_id = user_id
