from db import db


class FavouritesModel(db.Model):
    __tablename__ = 'favourites_table'

    id = db.Column(db.Integer, primary_key=True)
    kitty_name = db.Column(db.String(30))
    image = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users_table.id'), nullable=False)

    def __init__(self, kitty_name, image, user_id):
        self.kitty_name = kitty_name
        self.image = image
        self.user_id = user_id

    def save(self):
        db.session.add(self)
        db.session.commit()
