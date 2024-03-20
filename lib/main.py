from customer import Customer
from restaurant import Restaurant
from review import Review

def main():
    # Instantiate customers, restaurants, and reviews
    customer1 = Customer("Kinuthia", "Nganuthia")
    customer2 = Customer("Kafukuswi", "Donkey")

    restaurant1 = Restaurant("KiAMAIKO")
    restaurant2 = Restaurant("Kwa Mathee")

    review1 = Review(customer1, restaurant1, 4)
    review2 = Review(customer2, restaurant2, 5)

    # How to use methods
    print(customer1.full_name())  
    print(restaurant2.average_star_rating())  # Output: 5.0
    print(customer2.num_reviews())  # Output: 1

if __name__ == '__main__':
    main()