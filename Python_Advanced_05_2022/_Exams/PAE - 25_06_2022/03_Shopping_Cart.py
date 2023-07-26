def shopping_cart(*food):
    string = ""
    meals = {"Pizza": [], "Soup": [], "Dessert": []}
    for data in food:
        if isinstance(data, str):
            break
        else:
            meal = data[0]
            product = data[1]
            if meal not in meals:
                meals[meal] = []
            if product not in meals[meal]:
                if meal == "Soup" and len(meals[meal]) < 3:
                    meals[meal].append(product)
                elif meal == "Pizza" and len(meals[meal]) < 4:
                    meals[meal].append(product)
                elif meal == "Dessert" and len(meals[meal]) < 2:
                    meals[meal].append(product)

    sum_of_meals = 0
    for key in meals:
        sum_of_meals += len(meals[key])

    if sum_of_meals == 0:
        return "No products in the cart!"
    else:
        for key, values in sorted(meals.items(), key=lambda x: (-len(x[1]), x[0])):
            string += f"{key}:\n"
            for value in sorted(values):  # not sure what they want
                string += f" - {value}\n"
        return string


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Pizza', 'ham'),
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))
# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))
