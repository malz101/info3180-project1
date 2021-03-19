from . import db

class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    title = db.Column(db.String(80))
    no_of_rooms = db.Column(db.String(11))
    no_of_bathrooms = db.Column(db.String(11))
    location = db.Column(db.String(255))
    price = db.Column(db.String(20))
    type_ = db.Column(db.Enum('House','Apartment', name='PropertyType'))
    description = db.Column(db.String(1000))
    photo = db.Column(db.UnicodeText())

    def __init__(self, title,  description, no_of_rooms, no_of_bathrooms,\
                    price, type_, location, photo):
        self.title = title
        self.no_of_rooms = no_of_rooms
        self.no_of_bathrooms = no_of_bathrooms
        self.location = location
        self.price = price
        self.type_ = type_
        self.description = description
        self.photo = photo
    
    def __repr__(self):
        return '<Property %r %s %s %s>' % (self.id, self.title, self.no_of_rooms, self.type_)

    # @staticmethod
    # def getPropertyType(self,type_):
    #     """returns a string containing the correct property type based in input"""
    #     property_types = {"house": "House", "apartment": "Apartment"}
    #     try:
    #         return property_types[type_]
    #     except KeyError:
    #         return None
            