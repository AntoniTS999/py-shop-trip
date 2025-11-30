from __future__ import annotations
import datetime


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def receipt(self, customer: str) -> None:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"\nDate: {now}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        total = 0
        for product_name, amount in customer.product_cart.items():
            cost = self.products[product_name] * amount
            total += cost

            # formatowanie liczb
            cost_str = f"{cost:.2f}".rstrip("0").rstrip(".")
            print(f"{amount} {product_name}s for {cost_str} dollars")

        total_str = f"{total:.2f}".rstrip("0").rstrip(".")
        print(f"Total cost is {total_str} dollars")
        print("See you again!\n")
