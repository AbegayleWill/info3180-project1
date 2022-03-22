
from . import db

class Property(db.Model):

   
    __tablename__ = 'properties' 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text())
    bedrooms = db.Column(db.String(10))
    bathrooms = db.Column(db.String(10))
    price = db.Column(db.String(30))
    p_type = db.Column(db.String(20))
    location = db.Column(db.String(200), unique=False)
    photo = db.Column(db.String(150))

    
    def __init__(self, title, description, bedrooms, bathrooms, price, p_type, location, photo):
        self.title = title
        self.description = description
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.price = price
        self.p_type = p_type
        self.location = location
        self.photo = photo
    


    def __repr__(self):
        return '<Property %r>' % self.title

    def get_id(self):
        return str(self.id)

