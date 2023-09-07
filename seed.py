from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review
from models import Base

engine = create_engine('sqlite:///restaurant.db')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

restaurant1 = Restaurant(name="Quiver", price=2800)
restaurant2 = Restaurant(name="Black Curves", price=3000)


customer1 = Customer(first_name="Prince", last_name="Hope")
customer2 = Customer(first_name="Jane", last_name="Anyango")


review1 = Review(star_rating=4, restaurant=restaurant1, customer=customer1)
review2 = Review(star_rating=5, restaurant=restaurant2, customer=customer2)


# session.add(restaurant1)
# session.add(restaurant2)
# session.add(customer1)
# session.add(customer2)
# session.add(review1)
# session.add(review2)

session.commit()
session.close()

restaurant_reviews = restaurant1.get_reviews()
for review in restaurant_reviews:
    print(f"Review for Restaurant: {review.get_restaurant().name}, Rating: {review.star_rating}")

restaurant_customers = restaurant1.get_customers()
for customer in restaurant_customers:
    print(f"Customer of Restaurant: {customer.get_restaurants()[0].name}, Name: {customer.first_name} {customer.last_name}")

review_customer = review1.get_customer()
print(f"Customer of Review: {review_customer.first_name} {review_customer.last_name}")

review_restaurant = review1.get_restaurant()
print(f"Restaurant of Review: {review_restaurant.name}")

 