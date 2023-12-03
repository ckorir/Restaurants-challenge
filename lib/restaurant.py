from review import Review

class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        # Initialize a new restaurant
        self.name = name
        self.reviews = []  # Initialize the reviews attribute
        self._add_restaurant_to_collection()

    def _add_restaurant_to_collection(self):
        # Add the restaurant instance to the collection of all restaurants
        Restaurant.all_restaurants.append(self)

    def name(self):
        return self.name

    @classmethod
    def all(cls):
        # Get a list of all restaurant instances
        return cls.all_restaurants

    def reviews(self):
        return self.reviews

    def customers(self):
        # Get a list of unique customers who have reviewed this restaurant
        return list(set([review.customer() for review in self.reviews]))

    def average_star_rating(self):
        if not self.reviews:
            return 0.0
        avg_rating = sum([review.rating for review in self.reviews]) / len(self.reviews)
        # Round the average rating to one decimal place
        return round(avg_rating, 1)
