from collections import deque


def stock_availability(inventory, typ, *amount):
    inventory = deque(inventory)
    if typ == "delivery":
        for box in amount:
            inventory.append(box)
    elif typ == "sell":
        if amount:
            try:
                for i in range(amount[0]):
                    inventory.popleft()
            except:
                for element in amount:
                    if element in inventory:
                        while element in inventory:
                            inventory.remove(element)
        else:
            inventory.popleft()

    return list(inventory)




print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
