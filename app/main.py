from app.configuration import config
from app.customer import Customer
from app.shop import Shop

def shop_trip():
    customers = [Customer(**c) for c in config["customers"]]
    shops = [Shop(s["name"], s["location"], s["products"]) for s in config["shops"]]

    for c in customers:
        print(f"{c.name} has {c.money} dollars")

        trip_prices = {}
        for s in shops:
            cost = c.shopping_cost_in(s)
            print(f"{c.name}'s trip to {s.name} costs {round(cost, 2)}")
            trip_prices[s] = cost

        # find cheapest shop
        shop_to_go = min(trip_prices, key=trip_prices.get)
        min_cost = trip_prices[shop_to_go]

        if c.money < min_cost:
            print(f"{c.name} doesn't have enough money to make a purchase in any shop")
            continue

        print(f"{c.name} rides to {shop_to_go.name}")
        c.location = shop_to_go.location[:]

        # print receipt
        shop_to_go.receipt(c)

        print(f"{c.name} rides home")
        # subtract money
        c.money -= min_cost
        print(f"{c.name} now has {round(c.money, 2)} dollars")