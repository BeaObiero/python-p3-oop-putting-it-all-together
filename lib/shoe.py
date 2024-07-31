
class Shoe:
    def __init__(self, brand, size, color, price):
        self.brand = brand
        self.size = size
        self.color = color
        self.price = price
        self.condition = "Used"  # Default condition

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            raise ValueError("Brand must be a string.")
        self._brand = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise ValueError("size must be an integer.")
        self._size = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if not isinstance(value, str):
            raise ValueError("color must be a string.")
        self._color = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not (isinstance(value, (int, float)) and value >= 0):
            raise ValueError("price must be a non-negative number.")
        self._price = value

    def __str__(self):
        return f"{self.brand} {self.color} Shoes (Size {self.size}) - ${self.price:.2f}"

    def __repr__(self):
        return f"Shoe(brand={self.brand!r}, size={self.size}, color={self.color!r}, price={self.price:.2f})"

    def cobble(self):
        self.condition = "New"
        print("The shoe has been repaired.")

