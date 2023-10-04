
from flask import Flask, make_response, jsonify, request, session
from flask_migrate import Migrate
from flask_restful import Api, Resource
from datetime import datetime

from models import db, User, Product, Review

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
        
        user = User.query.filter(User.email == email).first()
        
        if user:
            return {'message': 'User already exists'}
        else:
            new_user = User(username=username, password=password, email=email)
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
            return jsonify({'message': '401: Not Authorized'}), 401

api.add_resource(CheckSession, '/check_session')


class Reviews(Resource):
    def get(self):
        reviews = Review.query.all()
        
        serialized_reviews = [review.to_dict() for review in reviews]
        return make_response(jsonify(serialized_reviews), 200)
    
    def post(self):
        if not session['user_id']:
            return {'error': 'Unauthorized'}, 401
        
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

class ProductById(Resource):
    def get(self, id):
        product = Product.query.get(id)
        
        if  product:
            return jsonify(product.to_dict())
        else:
            return {'error': 'Product not found'}

api.add_resource(ProductById,'/products/<int:id>')



if __name__ == '__main__':
    app.run(port=5555, debug=True)
