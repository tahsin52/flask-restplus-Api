from .. import db


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(155), unique=True)
    parent_id = db.Column(db.Integer)

    product = db.relationship('Product', backref='product', lazy='dynamic')

    def __repr__(self):
        return "<Category '{}'>".format(self.name)