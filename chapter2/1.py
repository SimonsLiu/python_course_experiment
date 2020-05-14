"""
@author:Liushihao
@time:2020/3/5:0:29
@email:Liushihao_1224@163.com
@describe:
"""
a, b, c = map(float, input("请输入三个浮点数作为长方体棱长：").split())
volume = a*b*c
area = (a*b+b*c+c*a)*2
print("长方体体积为：",volume)
print("长方体表面积为：",area)
