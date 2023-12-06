from app import app
from models import db, User, Product, Review, HairService, NailService, MakeupService, Appointment
from datetime import datetime, time



with app.app_context():
    Product.query.delete()
    User.query.delete()
    Review.query.delete()
    HairService.query.delete()
    NailService.query.delete()
    MakeupService.query.delete()
    Appointment.query.delete()
    # CartItem.quantity.delete()
    
    
    product1 = Product(
        name='Lip gloss',
        description='Rich gloss. It can be worn alone or on top of a nude or any other lipstick',
        image='https://images.unsplash.com/photo-1631214524115-9942bf927d4a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1374&q=80',
        price=12.99,
    )

    product2 = Product(
        name='Eyeshadow Palette',
        description='A versatile eyeshadow palette with various shades for different eye looks',
        image='https://images.unsplash.com/photo-1614739846939-d50eefc99efc?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=800&h=800&q=80',
        price=24.99,
    )

    product3 = Product(
        name='Mascara',
        description='Lengthening and volumizing mascara for bold, beautiful lashes',
        image='https://images.unsplash.com/photo-1631214499943-07647378b067?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1325&q=80',
        price=9.99,
    )

    product4 = Product(
        name='Foundation',
        description='A high-coverage foundation for a flawless complexion',
        image='https://images.unsplash.com/photo-1627885793933-584e53987c14?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1336&q=80',
        price=19.99,
    )
    
    
    user1 = User(
        username='Moses Chengo',
        email='moses@example.com',
        password='password123',
        phone_number = '0799863031'
    )

    user2 = User(
        username='Jane Smith',
        email='jane@example.com',
        password='secret',
        phone_number = '0790902345'
        
    )
    
    


    db.session.add_all([user1, user2])
    
    review1 = Review(review_text='They are awesome!', user=user1, rating=4)
    review2 = Review(review_text='The best beauty products i have ever seen!', user=user2, rating=5)
        
    hair_service1 = HairService(title='WASH & BLOW DRY', description="Our professional wash and blow dry service is tailored to each and every guests individual needs. Freshen up your look with our amazing step by step wash and blow dry procedure", price=2500.0, image='https://phoinabeauty.com/wp-content/uploads/2022/03/phoina-service-01-1.jpg')
    
    hair_service2 = HairService(title='HAIR RELAXING & TREATMENT', description='Relaxed hair requires great expertise and at Phoina Beauty we deliver an exceptional service while maintaining quality standards by using quality products.', price=6000.00, image='https://phoinabeauty.com/wp-content/uploads/2022/03/phoina-service-02-2.jpg')
    
    hair_service3 = HairService(title='WEAVING AND WIG INSTALLATION', description='Our Hair Studio can reinvent your look instantly with our expert quality weaves and handmade wig services. Change things up with a bold colour.', price=3000.0, image='https://phoinabeauty.com/wp-content/uploads/2022/03/phoina-service-03.jpg')
    
    hair_service4 = HairService(title='WIG WASHING AND REVAMPING', description='We specialize on human hair extensions including wig care and taking old wigs and revamping them into new units.', price=1600.0, image='https://phoinabeauty.com/wp-content/uploads/2022/03/phoina-service-04.jpg')
    
    hair_service5 = HairService(title='BRAIDING', description='At our Salon we are enthusiastic about new styles and trends of braiding. Create different looks by experimenting with different styles delivered neatly by our professionals.', price=2600.0, image='https://phoinabeauty.com/wp-content/uploads/2022/03/phoina-service-05.jpg')
    
    hair_service6 = HairService(title='STYLING & BRIDAL', description='We help you achieve a head turning unique look on your special day. With great expertise comes great techniques and we offer great styling effortlessly.', price=2500.0, image='https://phoinabeauty.com/wp-content/uploads/2022/03/phoina-service-06-1.jpg')
    

    makeup_service1 = MakeupService(title='Makeup Application', description='It’s our duty at Damic Beauty, to make you look the part on your wedding day. We specialize on wedding looks, where we ensure you and the bride tribe are given a natural yet beautiful look.', price=45000.0, image='https://images.unsplash.com/photo-1591570915688-e1b5292de457?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1349&q=80')
    makeup_service2 = MakeupService(title='Bridal Makeup', description='Invigorate and restore the health and beauty of your nails . At our Salon we have skilled Technicians that offer exceptional services that will help you relax and enjoy nails polished to perfection.', price=9000.0, image='https://phoinabeauty.com/wp-content/uploads/2022/03/phoina-makeup-02.jpg')
    
    nailservice1 = NailService(title='MANICURE & PEDICURE', description='Invigorate and restore the health and beauty of your nails . At our Salon we have skilled Technicians that offer exceptional services that will help you relax and enjoy nails polished to perfection.', price=4500.0, image='https://phoinabeauty.com/wp-content/uploads/2022/03/phoina-service-07.jpg')
    nailservice2 = NailService(title='NAILS', description='We offer exception nail enhancement services, including tips, acrylics, Gel among others.', price=2000.0, image='https://phoinabeauty.com/wp-content/uploads/2022/03/phoina-service-08.jpg')
    
    

    appointment1 = Appointment(date=datetime(2023, 10, 10), time=time(10, 0), service='Haircut', extra_information='No specific instructions', user=user1)
    appointment2 = Appointment(date=datetime(2023, 8, 12), time=time(12,30), service='Manicure', extra_information='French manicure', user=user2)

    db.session.add_all([product1, product2, product3, product4, user1, user2, review1, review2 ,hair_service1, hair_service2, hair_service3, hair_service4, hair_service5, hair_service6, nailservice1, nailservice2, makeup_service1, makeup_service2, appointment1, appointment2])
    db.session.commit()


    db.session.commit()
    
    
    
    # cart_item1 = CartItem(quantity=2, user=user1, product=product1, price=product1.price)
    # cart_item2 = CartItem(quantity=1, user=user1, product=product2, price=product2.price)

    # # Adding some cart items for user2
    # cart_item3 = CartItem(quantity=3, user=user2, product=product3, price=product3.price)
    # cart_item4 = CartItem(quantity=1, user=user2, product=product4, price=product4.price)

    # db.session.add_all([cart_item1, cart_item2, cart_item3, cart_item4])
    # db.session.commit()
if __name__ == "__main__":
    app.run(debug=True)
    
    