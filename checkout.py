import json

""" Script for cashier at till.
    Should record individual items, quantity and price.
    To account for money received whilst - determining
    how much change given."""


def cashier():
    basket = []
    price_basket = []
    total = 0
    print("Welcome to the Neighbourhood store.")

    while True:

        product = input("Enter name of item: ")

        with open("stock.json") as st:
            inv_read = json.load(st)
        store_room = inv_read["inventory"][
            0:
        ]  # break down inventory json to list elements
        try:
            for elements in store_room:
                if elements["product_name"] == product:
                    print(elements["price"])
                    price = elements[
                        "price"
                    ]  # isolate product price from product name and store for use later

            basket.append(product)
            quantity = int(input("How many? "))
            print(f"{quantity}")
            summary_price = quantity * price
            print(f"{summary_price:.2f}")
            price_basket.append(summary_price)
            print(f"cost of {quantity} {product}s is : £{summary_price:.2f}")

            # for val in price_basket:
            #   print(f"{val:.2f}")

            for items in basket:
                for val in price_basket:
                    zipped = zip(
                        basket, price_basket
                    )  # useful for correlating products selected with cost of quantity
            for (a, b) in zipped:
                print(f"{a}  --->  {b:.2f}")

            total += float(b)
            to_exit = input("Would that be all? ")
            if to_exit.lower() in ("yes"):
                print(f"Grand Total: £{total:.2f}")
                money_received = float(input("How much money given? £ "))
                change = float(money_received) - total
                print(f"Your change is =====> £{change:.2f}")
                print("Thanks for your custom. \nHave a great day!!!")
        except UnboundLocalError:
            print(
                f"The product {product} doesn't exist in database. \nPlease check again."
            )
            return total
