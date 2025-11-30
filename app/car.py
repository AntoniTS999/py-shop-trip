from app.configuration import config

class Car:
    fuel_price = config["FUEL_PRICE"]

    def __init__(self, brand, fuel_consumption):
        self.brand = brand
        self.fuel_consumption = fuel_consumption  # liters per 100 km

    def trip_cost(self, distance_km):
        liters = (distance_km / 100) * self.fuel_consumption
        return liters * Car.fuel_price