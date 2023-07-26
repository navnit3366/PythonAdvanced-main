from collections import OrderedDict


def shopping_list(budget, **products):
    products = OrderedDict(products)
    string = ""
    basket = 5
    bought = []
    if budget >= 100:
        for product, data in products.items():
            if basket == 0:
                break
            price, quantity = data[0], data[1]
            expense = price * quantity
            if expense <= budget and basket > 0:
                basket -= 1
                budget -= expense
                string += f"You bought {product} for {expense:.2f} leva.\n"
                bought.append([product, expense])
    else:
        string = "You do not have enough budget."
    return string


# print(shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))
# print()
# print(shopping_list(20,
#                     jeans=(19.99, 1),
#                     ))
print()
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))

