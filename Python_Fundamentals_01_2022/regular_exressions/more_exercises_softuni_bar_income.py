import re

# pattern = r"%(?P<name>[A-Z][a-z]+)%\<(?P<product>\w+)\>\|(?P<count>\d+)\|(?P<price>\d+(\.\d+)?)\$"
pattern = r"%(?P<name>[A-Z][a-z]+)%([^\|\$\%\.]+)?\<(?P<product>\w+)\>([^\|\$\%\.]+)?\|(?P<count>\d+)\|([a-z]+)?(?P<price>\d+(\.\d+)?)\$"
list_of_sums = []
client = input()
while client != "end of shift":
    result = [obj.groupdict() for obj in re.finditer(pattern, client)]
    # print(result)
    # print(f"{result[0]['name']}")
    if len(result) > 0:
        order_sum = (int(result[0]['count'])*float(result[0]['price']))
        print(f"{result[0]['name']}: {result[0]['product']} - {order_sum:.2f}")
        list_of_sums.append(order_sum)
    client = input()
print(f"Total income: {sum(list_of_sums):.2f}")