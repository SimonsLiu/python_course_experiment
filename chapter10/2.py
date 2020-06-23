"""
@author:Liushihao
@time:2020/6/8:17:18
@email:Liushihao_1224@163.com
@describe:
2．编程实现如下功能：
(1)定义一个实现算术运算的类Arithmetic_Operation，可以实现两个整数的加法、减法、乘法和除法等运算。
(2)定义一个测试类Test_Arithmetic_Operation对Arithmetic_Operation中的功能进行测试。
"""
import unittest
class Arithmetic_Operation:
    a = 0
    b = 0
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a+self.b
    def Subtraction(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def dev(self):
        return self.a/self.b

class Test_Arithmetic_Operation(unittest.TestCase):
    def test_add(self):
        a = Arithmetic_Operation(1,1)
        self.assertEqual(a.add(), 2)

if __name__=="__main__":
    unittest.main()