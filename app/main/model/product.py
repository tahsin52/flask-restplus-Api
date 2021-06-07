from .. import db


class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(155), unique=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))



    def __repr__(self):
        return "<Product '{}'>".format(self.title)