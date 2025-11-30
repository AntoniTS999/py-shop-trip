from app.configuration import config
from app.customers import Customer
from app.shop import Shop


def shop_trip() -> None:
    all_customers = [Customer(**customer_data)
                     for customer_data in config["customers"]]
    all_shops = [Shop(shop_data["name"],
                      shop_data["location"],
                      shop_data["products"])
                 for shop_data in config["shops"]]

    for current_customer in all_customers:
        print(f"{current_customer.name} "
              f"has {current_customer.money:g} dollars")

        trip_costs = {}

        for current_shop in all_shops:
            cost = current_customer.shopping_cost_in(current_shop)
            if cost is not None:
                # używamy :.2f do dokładnie 2 miejsc po przecinku
                formatted_cost = f"{cost:.2f}".rstrip("0").rstrip(".")
                print(f"{current_customer.name}'s "
                      f"trip to the {current_shop.name} "
                      f"costs {formatted_cost}")
                trip_costs[current_shop] = cost

        if not trip_costs:
            print(f"{current_customer.name} "
                  f"doesn't have enough money "
                  f"to make a purchase in any shop")
            continue

        cheapest_shop = min(trip_costs, key=trip_costs.get)
        cheapest_cost = trip_costs[cheapest_shop]

        if current_customer.money < cheapest_cost:
            print(f"{current_customer.name} doesn't "
                  f"have enough money to make a purchase in any shop")
            continue

        print(f"{current_customer.name} rides to {cheapest_shop.name}")
        current_customer.location = cheapest_shop.location[:]

        # print receipt
        cheapest_shop.receipt(current_customer)

        print(f"{current_customer.name} rides home")
        current_customer.money -= cheapest_cost
        formatted_money = (f"{current_customer.money:.2f}"
                           .rstrip("0").rstrip("."))
        print(f"{current_customer.name} now has {formatted_money} dollars")
