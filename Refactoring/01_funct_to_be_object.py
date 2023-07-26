def draw_circle(x, y, radius, color):
    print(f'Drawing a circle at ({x}, {y}) with radius {radius} and color {color}')


def change_color(x, y, radius, new_color):
    print(f'Changing the color of circle at ({x}, {y}) with radius {radius} to {new_color}')


def move_circle(x, y, radius, new_x, new_y):
    print(f'Moving the circle at ({x}, {y}) with radius {radius} to ({new_x}, {new_y})')


class Circle:
    def __init__(self, radius, color, x, y):
        self.color = color
        self.radius = radius
        self.y = y
        self.x = x

    def draw(self):
        print(f'Drawing a circle at ({self.x}, {self.y}) with radius {self.radius} and color {self.color}')

    def new_color(self, new_color):
        self.color = new_color
        print(f'Changing the color of circle at ({self.x}, {self.y}) with radius {self.radius} to {self.color}')

    def move_circle(self, x, y, new_x, new_y):
        if self.x == x and self.y == y:
            print(f'Moving the circle at ({self.x}, {self.y}) with radius {self.radius} to ({new_x}, {new_y})')
            self.x = new_x
            self.y = new_y

    def __str__(self):
        return f"circle with: coords={self.x}:{self.y},and color={self.color}, and radius={self.radius}"


c = Circle(10, "red", 5, 6)
print(c.color)
c.color = "Blue"
print(c.color)
c.move_circle(5, 6, 10, 20)
print(c.x)

