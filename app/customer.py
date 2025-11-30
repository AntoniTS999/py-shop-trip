from app.car import Car

class Customer:
    def __init__(self, name, product_cart, location, money, car):
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(car["brand"], car["fuel_consumption"])

    @staticmethod
    def distance(a, b):
        return ((a[0]-b[0])**2 + (a[1]-b[1])**2) ** 0.5

    def shopping_cost_in(self, shop):
        # distance to shop and back
        dist = self.distance(self.location, shop.location)
        fuel_to_shop = self.car.trip_cost(dist)
        fuel_home = self.car.trip_cost(dist)

        # price of products
        product_cost = 0
        for p, amount in self.product_cart.items():
            if p not in shop.products:
                return None
            product_cost += shop.products[p] * amount

        return fuel_to_shop + fuel_home + product_cost
