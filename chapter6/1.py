"""
@author:Liushihao
@time:2020/4/20:11:23
@email:Liushihao_1224@163.com
@describe:
(1)定义一个抽象类Shape，在抽象类Shape中定义求面积getArea()和周长getPerimeter()的抽象方法。
(2)分别定义继承抽象类Shape的3个子类即Triangle、Rectangle和Circle，在这3个子类中重写Shape中的方法getArea()和getPerimeter()。
(3)创建类Triangle、Rectangle、Circle的对象，对3个类中的方法进行调用测试。
"""
import abc
import math
class Shape(metaclass=abc.ABCMeta):
    # 定义抽象方法
    @classmethod
    def getArea(self):
        pass

    @classmethod
    def getPerimeter(self):
        pass

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def getArea(self):
        # 利用海伦公式求三角形面积
        p = (self.a + self.b + self.c)/2
        area = math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
        return area
    def getPerimeter(self):
        perimeter = self.a + self.b + self.c
        return perimeter

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def getArea(self):
        return self.height*self.width
    def getPerimeter(self):
        perimeter = (self.height + self.width)*2
        return perimeter

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def getArea(self):
        return math.pi*self.r*self.r
    def getPerimeter(self):
        perimeter = math.pi*self.r*2
        return perimeter

if __name__ == '__main__':
    print("输出格式规定：数字一律保留两位小数")
    triangle = Triangle(3, 3, 3)
    print("边长为%.2f,%.2f,%.2f的三角形，面积为:%.2f，周长为:%.2f" % (triangle.a, triangle.b, triangle.c, triangle.getArea(), triangle.getPerimeter()))
    rectangle = Rectangle(10, 20)
    print("宽为%.2f,高为%.2f的长方形，面积为:%.2f，周长为:%.2f" % (rectangle.width, rectangle.height, rectangle.getArea(), rectangle.getPerimeter()))
    circle = Circle(3)
    print("半径为%.2f的圆，面积为:%.2f，周长为:%.2f" % (circle.r, circle.getArea(), circle.getPerimeter()))