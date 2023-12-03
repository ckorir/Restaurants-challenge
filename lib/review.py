class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        # Initialize a new review with a customer, restaurant, and rating
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        self.all_reviews_collection()

    def all_reviews_collection(self):
        # Add the review instance to the collection of all reviews
        Review.all_reviews.append(self)

    def rating(self):
        return self.rating
    
    def customer(self):
        return self.customer
    
    def restaurant(self):
        return self.restaurant
    
    @classmethod
    def all(cls):
        # Get a list of all review instances
        return cls.all_reviews
