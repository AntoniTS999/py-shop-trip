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
        for product, amount in customer.product_cart.items():
            cost = self.products[product] * amount
            total += cost
            print(f"{amount} {product}s for {cost} dollars")

        print(f"Total cost is {total} dollars")
        print("See you again!")
