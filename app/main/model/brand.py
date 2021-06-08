from .. import db


class Brand(db.Model):
    __tablename__ = "brand"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(155), unique=True)
    is_active = db.Column(db.Boolean)

    product = db.relationship('Product', backref='Brand.product', lazy='dynamic')

    def __repr__(self):
        return "<Brand '{}'>".format(self.name)