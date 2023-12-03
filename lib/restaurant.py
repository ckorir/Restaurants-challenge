from review import Review

class Restaurant(Review):
    all_restaurants = []

    def __init__(self,name):
        super().__init__(self, None, None, None)
        self.name = name
        self._add_restaurant_to_collection()

    def add_restaurant_to_collection(self):
        Restaurant.all_restaurants.append(self)

    def name(self):
        return self.name
    
    @classmethod
    def all(cls):
        return cls.all_restaurants

    def reviews(self):
        return self.reviews

    def customers(self):
        return list(set([review.customer() for review in self.reviews]))

    def average_rating(self):
        if not self.reviews:
            return 0
        return sum([review.rating for review in self.reviews]) / len(self.reviews)