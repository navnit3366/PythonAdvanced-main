import re

lines = int(input())
pattern = r"(?P<symbol1>@#+)(?P<barcode>[A-Z][A-Za-z0-9]{4,}[A-Z])(?P<symbol2>@#+)"
valid_barcodes = []
for line in range(lines):
    string = input()
    result = [obj.groupdict() for obj in re.finditer(pattern, string)]
    if result:
        barcode = result[0]["barcode"]
        product_group = ""
        for char in barcode:
            if char.isnumeric():
                product_group += char
        if product_group == "":
            product_group = "00"
        print(f"Product group: {product_group}")
    else:
        print(f"Invalid barcode")
