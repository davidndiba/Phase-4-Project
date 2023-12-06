from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.Integer)

    
    reviews = db.relationship('Review', back_populates='user')
    appointments = db.relationship('Appointment', back_populates='user')
    # cart_items = db.relationship('CartItem', back_populates='user')
    Product = db.relationship("Product", back_populates="user")
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'phone_number': self.phone_number,
            'appointments': [appointment.to_dict() for appointment in self.appointments],
            'reviews': [review.to_dict() for review in self.reviews],
            'product': [Product.to_dict() for product in self.Product],
        }
    
class Review(db.Model):
    __tablename__ = 'reviews'
    
    id = db.Column(db.Integer, primary_key=True)
    review_text = db.Column(db.String)
    rating = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', name='fk_review_user_id'),
        nullable=False
    )
    
    user = db.relationship('User', back_populates='reviews')
    
    def to_dict(self):
        result = {
            'id': self.id,
            'review_text': self.review_text,
            'rating': self.rating,
            'user_id': self.user_id,
        }

        if self.created_at:
            result['created_at'] = self.created_at.isoformat()

        return result  
    
class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String) 
    description = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    def to_dict(self):
        result =  {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'image': self.image,
            'description': self.description,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
        
        if self.created_at:
            result['created_at'] = self.created_at.isoformat()

        if self.updated_at:
            result['updated_at'] = self.updated_at.isoformat()

        return result
        
class HairService(db.Model):
    __tablename__ = 'hair_services'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    image = db.Column(db.String)
    price = db.Column(db.Float) 
            
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'image': self.image,
            'price': self.price
            
        }
        
class NailService(db.Model):
    __tablename__ = 'nail_services'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    image = db.Column(db.String)
    price = db.Column(db.Float) 
            
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'image': self.image,
            'price': self.price
            
            
        }

class MakeupService(db.Model):
    __tablename__ = 'makeup_services'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    image = db.Column(db.String)
    price = db.Column(db.Float) 
            
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'image': self.image,
            'price': self.price
        }                

class Appointment(db.Model):
    __tablename__ = 'appointments'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    service = db.Column(db.String)
    extra_information = db.Column(db.String)
    
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', name='fk_appointment_user_id'),
        nullable=False
    )
    
    user = db.relationship('User', back_populates='appointments')
    
    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date.isoformat(),
            'time': self.time.strftime('%H:%M'),
            'service': self.service,
            'extra_information': self.extra_information,
            'user_id': self.user_id,
        }
        
# class CartItem(db.Model):
#     __tablename__ = 'cart_items'
    
#     id = db.Column(db.Integer, primary_key=True)
#     quantity = db.Column(db.Integer, default=1)
#     price = db.Column(db.Float, nullable=False)  
    
#     user_id = db.Column(
#         db.Integer,
#         db.ForeignKey('users.id', name='fk_cart_item_user_id'),
#         nullable=False
#     )
    
#     product_id = db.Column(
#         db.Integer,
#         db.ForeignKey('products.id', name='fk_cart_item_product_id'),
#         nullable=False
#     )
    
#     user = db.relationship('User', back_populates='cart_items')
#     product = db.relationship('Product', back_populates='cart_items')
    
#     def to_dict(self):
#         return {
#             'id': self.id,
#             'quantity': self.quantity,
#             'price': self.price,  
#             'user_id': self.user_id,
#             'product_id': self.product_id,
#         }
