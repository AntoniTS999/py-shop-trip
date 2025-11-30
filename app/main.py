from app.configuration import config
from app.customers import Customer
from app.shop import Shop


def shop_trip() -> None:
    customers = [Customer(**c) for c in config["customers"]]
    shops = [Shop(s["name"],
                  s["location"],
                  s["products"])
             for s in config["shops"]]

    for cus in customers:
        print(f"{cus.name} has {cus.money} dollars")

        trip_prices = {}

        for shop in shops:
            cost = cus.shopping_cost_in(shop)
            print(f"{cus.name}'s trip to {shop.name} costs {cost:.2f}")
            trip_prices[shop] = cost

        # find cheapest shop
        shop_to_go = min(trip_prices, key=trip_prices.get)
        min_cost = trip_prices[shop_to_go]

        if cus.money < min_cost:
            print(f"{cus.name} doesn't have "
                  f"enough money to make a purchase in any shop")
            continue

        print(f"{cus.name} rides to {shop_to_go.name}")
        cus.location = shop_to_go.location[:]

        # print receipt
        shop_to_go.receipt(cus)

        print(f"{cus.name} rides home")
        # subtract money
        cus.money -= min_cost
        cus.money = round(cus.money, 2)
        print(f"{cus.name} now has {cus.money} dollars")
