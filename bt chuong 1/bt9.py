class Polygon:
    def __init__(self, sides):
        self.sides = sides 
    def display_info(self):
        print(f"Đây là một đa giác với {self.sides} cạnh.")
class Parallelogram(Polygon):
    def __init__(self, base, side, height):
        super().__init__(4) 
        self.base = base  
        self.side = side 
        self.height = height 
    def perimeter(self):
        return 2 * (self.base + self.side) 
    def area(self):
        return self.base * self.height  
class Rectangle(Parallelogram):
    def __init__(self, width, height):
        super().__init__(width, width, height) 
        self.width = width 
        self.height = height 
    def perimeter(self):
        return 2 * (self.width + self.height)  
    def area(self):
        return self.width * self.height 
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side) 
        self.side = side 
    def perimeter(self):
        return 4 * self.side 
    def area(self):
        return self.side ** 2 
if __name__ == "__main__":
    parallelogram = Parallelogram(10, 8, 6)
    print("Hình bình hành:")
    print(f"Chu vi: {parallelogram.perimeter()}")
    print(f"Diện tích: {parallelogram.area()}\n")
    rectangle = Rectangle(10, 5)
    print("Hình chữ nhật:")
    print(f"Chu vi: {rectangle.perimeter()}")
    print(f"Diện tích: {rectangle.area()}\n")
    square = Square(7)
    print("Hình vuông:")
    print(f"Chu vi: {square.perimeter()}")
    print(f"Diện tích: {square.area()}")