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

            cost_rounded = round(cost, 2)

            if cost_rounded == int(cost_rounded):
                cost_rounded = int(cost_rounded)

            print(f"{amount} {product}s for {cost_rounded} dollars")

        total_rounded = round(total, 2)
        if total_rounded == int(total_rounded):
            total_rounded = int(total_rounded)

        print(f"Total cost is {total_rounded} dollars")
        print("See you again!")
