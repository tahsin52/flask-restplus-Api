from .. import db


class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(155), unique=True, nullable=False)
    barcode = db.Column(db.String(155), unique=True)
    model = db.Column(db.String(155))
    stock = db.Column(db.Integer)
    sku = db.Column(db.String(155), unique=True)
    list_price = db.Column(db.Float)
    sale_price = db.Column(db.Float)
    description = db.Column(db.String(500))
    currency = db.Column(db.Enum("TRY", "USD", "EURO"))
    status = db.Column(db.String(155))
    tax = db.Column(db.Float)

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'))


    def __repr__(self):
        return "<Product '{}'>".format(self.title)