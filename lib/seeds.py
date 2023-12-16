# seed.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Review, Customer

if __name__ == '__main__':
    engine = create_engine('sqlite:///review.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # instances
    restaurant1 = Restaurant(name='shaka', price=800)
    restaurant2 = Restaurant(name='sera', price=360)

    customer1 = Customer(first_name='momoa', last_name='jason')
    customer2 = Customer(first_name='jackson', last_name='simiyu')

    review1 = Review(star_rating=3, restaurant=restaurant1, customer=customer1)
    review2 = Review(star_rating=1, restaurant=restaurant2, customer=customer2)
     
    

    # Adding
    session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2])
    print("Instances added to the session.")

    # Committing
    session.commit()
    print("Session committed.")

