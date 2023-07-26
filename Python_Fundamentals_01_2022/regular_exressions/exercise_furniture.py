import re

pattern = r">>(?P<name>[\w]+)<<(?P<price>\d+(\.\d+)?)\!(?P<qt>\d+)"
txt_line = input()
sum = 0
furniture = []
while txt_line != "Purchase":
    current_price = [obj.groupdict() for obj in re.finditer(pattern, txt_line)]
    # print(current_price)
    if len(current_price) > 0:
        # print(current_price[0]["qt"])
        # print(current_price[0]["price"])
        sum += int(current_price[0]["qt"]) * float(current_price[0]["price"])
        furniture.append(current_price[0]["name"])
    txt_line = input()
print(f"Bought furniture:")
if len(furniture) >0:
    print(*furniture, sep="\n")
print(f"Total money spend: {sum:.2f}")
