# Yelp-style Restaurant Review System

## Overview

This project implements a Yelp-style restaurant review system, with three main entities: `Customer`, `Restaurant`, and `Review`. Customers can leave reviews for restaurants, and the system provides various methods to interact with and analyze the data.

## Project Structure

The project is organized into separate files for each class:

- **customer.py**: Contains the `Customer` class.
- **restaurant.py**: Contains the `Restaurant` class.
- **review.py**: Contains the `Review` class.
- **testing.py**: Example usage and testing.

## Class Descriptions

### Customer

The `Customer` class represents an individual customer who can leave reviews.

#### Methods:

- `__init__(given_name, family_name)`: Initialize a new customer.
- `given_name()`: Get the given name of the customer.
- `family_name()`: Get the family name of the customer.
- `full_name()`: Get the full name of the customer.
- `all()`: Get a list of all customer instances.
- `num_reviews()`: Get the number of reviews authored by the customer.
- `find_by_name(name)`: Find a customer by their full name.
- `find_all_by_given_name(given_name)`: Find all customers with a given name.
- `restaurants()`: Get a list of unique restaurants reviewed by the customer.
- `add_review(restaurant, rating)`: Add a new review associated with the customer and a given restaurant.

### Restaurant

The `Restaurant` class represents a restaurant that can be reviewed.

#### Methods:

- `__init__(name)`: Initialize a new restaurant.
- `name()`: Get the name of the restaurant.
- `all()`: Get a list of all restaurant instances.
- `reviews()`: Get a list of reviews associated with the restaurant.
- `customers()`: Get a list of unique customers who have reviewed the restaurant.
- `average_star_rating()`: Get the average star rating for the restaurant based on its reviews.

### Review

The `Review` class represents a review left by a customer for a restaurant.

#### Methods:

- `__init__(customer, restaurant, rating)`: Initialize a new review.
- `all()`: Get a list of all review instances.
- `rating()`: Get the rating of the review.
- `customer()`: Get the customer associated with the review.
- `restaurant()`: Get the restaurant associated with the review.

## Example Usage

The `testing.py` file provides an example of how to create instances of customers, restaurants, and reviews, and how to use various methods.

## How to Run

To run the project:

1. Install dependencies using the provided Pipfile.
2. Execute the testing.py file.

```bash
python3 lib/testing.py
