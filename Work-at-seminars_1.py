import math


class GeometryError(Exception):
    pass


# Точка, задаваемый (x, y, z)

class Point:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def distance_to(self, other):
        if not isinstance(other, Point):
            raise GeometryError("Ожидалась точка")
        return math.sqrt(
            (self.x - other.x) ** 2 +
            (self.y - other.y) ** 2 +
            (self.z - other.z) ** 2
        )

    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.z})"


# Вектор, задаваемый (x, y, z)

class Vector:
    TOL = 1e-9

    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def multiply(self, k):
        if not isinstance(k, (int, float)):
            raise GeometryError("Можно умножать только на число")
        return Vector(self.x * k, self.y * k, self.z * k)

    def add(self, other):
        if not isinstance(other, Vector):
            raise GeometryError("Ожидался вектор")
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def subtract(self, other):
        if not isinstance(other, Vector):
            raise GeometryError("Ожидался вектор")
        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    def dot(self, other):
        if not isinstance(other, Vector):
            raise GeometryError("Ожидался вектор")
        return self.x * other.x + self.y * other.y + self.z * other.z

    def is_collinear(self, other):
        if not isinstance(other, Vector):
            raise GeometryError("Ожидался вектор")
        cx = self.y * other.z - self.z * other.y
        cy = self.z * other.x - self.x * other.z
        cz = self.x * other.y - self.y * other.x
        return abs(cx) < self.TOL and abs(cy) < self.TOL and abs(cz) < self.TOL

    def is_perpendicular(self, other):
        return abs(self.dot(other)) < self.TOL

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"


# Шар в 3-х мерном пространстве

class Ball:
    def __init__(self, center, radius):
        if not isinstance(center, Point):
            raise GeometryError("Центр должен быть точкой")
        if radius < 0:
            raise GeometryError("Радиус не может быть отрицательным")
        self.center = center
        self.radius = float(radius)

    def contains_point(self, point):
        return self.center.distance_to(point) <= self.radius

    def is_on_surface(self, point):
        return abs(self.center.distance_to(point) - self.radius) < 1e-9

    def surface_area(self):
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        return 4 / 3 * math.pi * self.radius ** 3

    def __repr__(self):
        return f"Ball(center={self.center}, radius={self.radius})"


# Демонстрация

if __name__ == "__main__":
    p1 = Point(0, 0, 0)
    p2 = Point(1, 1, 1)

    v1 = Vector(1, 2, 3)
    v2 = Vector(2, 4, 6)

    print(v1)
    print("|v1| =", v1.magnitude())
    print("v1 + v2 =", v1.add(v2))
    print("v1 · v2 =", v1.dot(v2))
    print("Коллинеарны?", v1.is_collinear(v2))

    ball = Ball(p1, 2.5)
    print(ball)
    print("Точка внутри шара?", ball.contains_point(p2))
    print("Площадь поверхности:", ball.surface_area())
    print("Объём:", ball.volume())