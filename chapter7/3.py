"""
@author:Liushihao
@time:2020/4/27:16:33
@email:Liushihao_1224@163.com
@describe:使用Os模块获取当前项目工作路径，并输出当前工作路径下的所有文件。
"""
import os
print("当前工作路径为：%s"%os.getcwd())
print("当前工作路径下的所有文件：",os.listdir(os.getcwd()))
