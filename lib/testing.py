# Import necessary classes from respective files
from customer import Customer
from restaurant import Restaurant
from review import Review

# Example usage:
customer1 = Customer("John", "Doe")
customer2 = Customer("Mary", "Jane")
customer3 = Customer("John", "Whick")
restaurant1 = Restaurant("Pizza Inn")
restaurant2 = Restaurant("The Mayuras")

customer1.add_review(restaurant1, 5)
customer2.add_review(restaurant1, 4)
customer3.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 5)
customer3.add_review(restaurant2, 3)

print("Average Star Rating for Delicious Grill:", restaurant1.average_star_rating())
print("Restaurants reviewed by John Doe:", [restaurant.name for restaurant in customer1.restaurants()])
print("Customer found by name 'John Doe':", Customer.find_by_name("John Doe").full_name())
print("All customers with given name 'John':", [customer.full_name() for customer in Customer.find_all_by_given_name("John")])
