def rectangle(lenght, width):
    def area(l_, w):
        return l_ * w

    def perimeter(l_, w):
        return 2 * (l_ + w)

    if not isinstance(lenght, int) or not isinstance(width, int):
        return "Enter valid values!"
    else:
        return f"Rectangle area: {area(lenght, width)} \nRectangle perimeter: {perimeter(lenght, width)}"


print(rectangle(2, 10))
print(rectangle('2', 10))
