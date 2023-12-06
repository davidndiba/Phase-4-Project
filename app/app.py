
from flask import Flask, make_response, jsonify, request, session
from flask_migrate import Migrate
from flask_restful import Api, Resource
from datetime import datetime, time as python_time

from models import db, User, Product, Review, HairService, MakeupService, NailService, Appointment

app = Flask(__name__)
app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

class Login(Resource):
    def post(self):
        username = request.get_json().get('username')
        password = request.get_json().get('password')
        user = User.query.filter((User.username == username) & (User.password == password)).first()
        
        if user:
            session['user_id'] = user.id
            return make_response(jsonify(user.to_dict()), 201)
        else:
            return {'error': 'user does not exist'}

api.add_resource(Login,'/login')

class Logout(Resource):
    def delete(self):
        session['user_id'] = None
        return {} , 204

api.add_resource(Logout,'/logout')

class Sign_Up(Resource):
    def post(self):
        data = request.get_json()
        
        username = data['username']
        password = data['password']
        email = data['email']
        phone_number = data['phone_number']
        
        user = User.query.filter(User.email == email).first()
        
        if user:
            return {'message': 'User already exists'}
        else:
            new_user = User(username=username, password=password, email=email, phone_number=phone_number)
            db.session.add(new_user)
            db.session.commit()
            
            session['user_id'] = new_user.id
            return make_response(jsonify(new_user.to_dict()), 201)

        
api.add_resource(Sign_Up,'/signup')
class CheckSession(Resource):
    def get(self):
        user = User.query.filter(User.id == session.get('user_id')).first()
        if user:
            return jsonify(user.to_dict())
        else:
            return {'message': '401: Not Authorized'}

api.add_resource(CheckSession, '/check_session')


class Reviews(Resource):
    def get(self):
        reviews = Review.query.all()
        
        serialized_reviews = [review.to_dict() for review in reviews]
        return make_response(jsonify(serialized_reviews), 200)
    
    def post(self):
        if 'user_id' not in session or not session['user_id']:
            return {'error': 'You have to be signed it to add a review'}, 401
        
        data = request.get_json()
        
        review_text = data['review_text']
        rating = data['rating']
        
        review = Review(review_text=review_text, rating=rating, created_at=datetime.utcnow(),user_id=session['user_id'])
        db.session.add(review)
        db.session.commit()
        
        return make_response(jsonify(review.to_dict()), 201)
 
    
api.add_resource(Reviews,'/reviews')

class Products(Resource):
    def get(self):
        products = Product.query.all()
        
        serialized_products = [product.to_dict() for product in products]
        return make_response(jsonify(serialized_products), 200)
    
api.add_resource(Products, '/products')   

class NailResource(Resource):
    def get(self):
        services = NailService.query.all()
        
        serialized_services = [product.to_dict() for product in services]
        return make_response(jsonify(serialized_services), 200)
    
api.add_resource(NailResource, '/nails_services')     

class HairResource(Resource):
    def get(self):
        services = HairService.query.all()
        
        serialized_services = [product.to_dict() for product in services]
        return make_response(jsonify(serialized_services), 200)
    
api.add_resource(HairResource, '/hair_services')    

class MakeupResource(Resource):
    def get(self):
        services = MakeupService.query.all()
        
        serialized_services = [product.to_dict() for product in services]
        return make_response(jsonify(serialized_services), 200)
    
api.add_resource(MakeupResource, '/makeup_services')    

class ProductById(Resource):
    def get(self, id):
        product = Product.query.get(id)
        
        if  product:
            return jsonify(product.to_dict())
        else:
            return {'error': 'Product not found'}

api.add_resource(ProductById,'/products/<int:id>')

@app.route('/api/cart', methods=['GET'])
def get_cart():
    if 'user_id' not in session or not session['user_id']:
        return jsonify({"error": "User not authenticated"}), 401

    user_id = session['user_id']
    cart_items = CartItem.query.filter_by(user_id=user_id).all()
    serialized_cart = [item.to_dict() for item in cart_items]
    
    return jsonify(serialized_cart)

# # Add a new route to add items to the cart
# @app.route('/api/cart/add', methods=['POST'])
# def add_to_cart():
#     if 'user_id' not in session or not session['user_id']:
#         return jsonify({"error": "User not authenticated"}), 401

#     data = request.json
#     product_id = data.get('productId')
#     quantity = data.get('quantity', 1)  # Assuming a default quantity of 1 if not provided

#     # Check if the product is already in the cart for the user
#     existing_item = CartItem.query.filter_by(user_id=session['user_id'], product_id=product_id).first()

#     if existing_item:
#         # If the item exists, update the quantity
#         existing_item.quantity += quantity
#     else:
#         # If the item doesn't exist, create a new CartItem
#         new_item = CartItem(user_id=session['user_id'], product_id=product_id, quantity=quantity)
#         db.session.add(new_item)

#     db.session.commit()
#     return jsonify({"message": "Item added to cart successfully"})

class Appointments(Resource):
    def get(self):
        appointments = Appointment.query.all()
        
        serialized_appointments = [appintment.to_dict() for appintment in appointments]
        return make_response(jsonify(serialized_appointments), 200)
    
    def post(self):
        if 'user_id' not in session or not session['user_id']:
            return {'error': 'You have to be signed it to schedule an appointment'}, 401
        
        data = request.get_json()
        
        date = datetime.strptime(data['date'], '%Y-%m-%d').date()
        
        time_parts = data['time'].split(':')
        time = python_time(int(time_parts[0]), int(time_parts[1]))
        extra_information = data['extra_information']
        service = data['service']
        
        appointment = Appointment(date=date, time=time, extra_information=extra_information,service=service, user_id=session['user_id'])
        db.session.add(appointment)
        db.session.commit()
        
        return make_response(jsonify(appointment.to_dict()), 201)

api.add_resource(Appointments, '/appointments')

class MyAppointments(Resource):
    def get(self, id):
        user = User.query.get(id)
        
        user_serialized = user.to_dict()
        
        if user:
            return jsonify(user_serialized)
        
api.add_resource(MyAppointments, '/my_appointments/<int:id>')     



if __name__ == '__main__':
    app.run(port=5555, debug=True)
