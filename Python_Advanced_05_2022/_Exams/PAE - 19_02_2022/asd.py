def field_with_coordinates():
    coordinated_field = []
    row = 9
    for r in range(8):
        row -= 1
        coordinated_field.append([])
        for c in range(8):
            col = chr(97+c)
            coordinated_field[r].append(f"{col}{row}")
    return coordinated_field


def print_field(fld):
    print("==" * 20)
    [print(' '.join(fld[r])) for r in range(len(fld))]
    
print_field(field_with_coordinates())