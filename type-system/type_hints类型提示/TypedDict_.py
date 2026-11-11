from pydantic import BaseModel

#
# class Point2D(TypedDict):
#     x: Required[int]
#     y: Required[int]
#     label: NotRequired[str]


class Point2D(BaseModel):
    x: float
    y: float
    label: str | None = None

    def distance_from_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    @property
    def coordinates(self) -> tuple[float, float]:
        return self.x, self.y

    @property
    def origin(self) -> tuple[float, float]:
        return 0, 0

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


if __name__ == "__main__":
    point: Point2D = Point2D(x=3, y=4)
    print(point.distance_from_origin())
    print(point.origin)
    print(repr(point))
