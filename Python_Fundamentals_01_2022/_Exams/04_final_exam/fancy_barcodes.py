import re

lines = int(input())
# pattern = r"(?P<symbols>@#+)(?P<product>([A-Z]([A-Za-z0-9]+){4,}[A-Z]))(?P=symbols)"
pattern = r"(?P<symbols>@#+)(?P<product>([A-Z]([A-Za-z0-9]+){4,}[A-Z]))(@#+)"
for line in range(lines):
    product = ""
    pr_group = ""
    current_line = input()
    # result = [obj.groupdict() for obj in re.finditer(pattern, current_line)]
    result = re.search(pattern, current_line)
    if result:
        product = result.group("product")
    if not product:
        print(f"Invalid barcode")
    else:
        for idx in range(len(product)):
            if product[idx].isdigit():
                pr_group += product[idx]
        if len(pr_group) > 0:
            print(f"Product group: {pr_group}")
        else:
            print(f"Product group: 00")
