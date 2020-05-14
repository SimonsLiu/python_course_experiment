"""
@author:Liushihao
@time:2020/4/27:16:33
@email:Liushihao_1224@163.com
@describe:
"""
import turtle

turtle.fillcolor("red")
turtle.begin_fill()

count = 1

while count <= 5:
    turtle.forward(100)
    turtle.right(144)
    count += 1

turtle.end_fill()
turtle.exitonclick()



