class Point:
    __slots__ = ("x", "y")

    def __init__(self, x: float | int, y: float | int):
        self.x = x
        self.y = y

    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    @property
    def distance(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5


if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(2, 3)
    p3 = p1 + p2
    print(p3)
