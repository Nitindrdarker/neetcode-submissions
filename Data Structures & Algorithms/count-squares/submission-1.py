class CountSquares:

    def __init__(self):
        self.points = {}
        

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] = self.points.get(tuple(point), 0) + 1
        

    def count(self, point: List[int]) -> int:
        x, y = point
        total = 0
        for x1, y1 in self.points:
            if x != x1 and y == y1:
                c = self.points[(x1, y1)]
                d = x - x1
                total += c * self.points.get((x, y - d), 0) * self.points.get((x1, y1 - d), 0)
                total += c * self.points.get((x, y + d), 0) * self.points.get((x1, y1 + d), 0)
        return total




