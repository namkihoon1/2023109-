class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def getArea(self):
        width = abs(self.x2 - self.x1)
        height = abs(self.y2 - self.y1)
        return width * height

    def getPerimeter(self):
        width = abs(self.x2 - self.x1)
        height = abs(self.y2 - self.y1)
        return 2 * (width + height)

    def show(self):
        print(f"좌측 상단 꼭지점이 ({self.x1}, {self.y1})이고 우측 상단 꼭지점이 ({self.x2}, {self.y2})인 사각형입니다.")


# 주 프로그램부
r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()
r1.show()
print(f"\n넓이는 {a}, 둘레는 {p}")
