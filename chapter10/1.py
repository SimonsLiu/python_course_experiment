"""
@author:Liushihao
@time:2020/6/8:16:45
@email:Liushihao_1224@163.com
@describe:
1．编程实现如下功能：
(1)定义一个利用列表实现队列的类List_Queue，可以实现队列元素进入、删除、求队列长度等功能。
(2)定义一个异常处理类List_Queue_Exception对类List_Queue中可能出现的异常进行处理。
"""
class List_Queue:
    def __init__(self, list1):
        self.queue = list1
    # 添加元素
    def addList(self):
        a = input("请输入插入的元素:")
        self.queue.append(a)
    # 删除元素
    def delItem(self):
        self.queue.pop(0)
    # 求队列长度
    def lenList(self):
        print("队列长度：", len(self.queue))
    # 获取队列
    def get(self):
        return self.queue

class List_Queue_Exception(BaseException, List_Queue):
    def __init__(self, list1):
        List_Queue.__init__(self, list1)

    # 添加元素
    def addList(self):
        try:
            a = input("请插入队列元素：")
            self.queue.append(a)
        except TypeError as e1:
            print("数据类型错误！", e1)
        except IOError as e1:
            print("输入异常！", e1)
        except RuntimeError as e1:
            print("一般运行时错误！", e1)
        except:
            print("程序运行异常！")

List1 = [1,2,3]
Q = List_Queue_Exception(List1)
print("初始化队列为：",Q.get())
Q.addList()
Q.addList()
Q.addList()
Q.addList()
print("插入四次之后，队列为：", Q.get())
Q.delItem()
Q.delItem()
print("删除两次之后，队列为：", Q.get())