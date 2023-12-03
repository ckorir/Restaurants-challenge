from review import Review

class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        # Initialize a new customer with given name and family name
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []  # Initialize the reviews attribute
        self._add_customer_to_collection()

    def _add_customer_to_collection(self):
        Customer.all_customers.append(self)

    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        # Get the full name of the customer
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        # Get a list of all customer instances
        return cls.all_customers

    def num_reviews(self):
        # Get the number of reviews authored by this customer
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, name):
        # Find a customer by their full name
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, given_name):
        # Find all customers with a given name
        return [customer for customer in cls.all_customers if customer.given_name == given_name]

    def restaurants(self):
        # Get a list of unique restaurants reviewed by this customer
        return list(set([review.restaurant for review in self.reviews]))

    def add_review(self, restaurant, rating):
        # Add a new review associated with this customer and the given restaurant
        review = Review(self, restaurant, rating)
        self.reviews.append(review)
        restaurant.reviews.append(review)