class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        self.all_reviews_collection()

    def all_reviews_collection(self):
        Review.all_reviews.append(self)

    def rating(self):
        return self.rating
    
    def customer(self):
        return self.customer
    
    def restaurant(self):
        return self.restaurant
    
    
    @classmethod
    def all(cls):
        return cls.all_reviews
