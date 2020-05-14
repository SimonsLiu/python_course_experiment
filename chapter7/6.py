"""
@author:Liushihao
@time:2020/4/27:16:33
@email:Liushihao_1224@163.com
@describe:使用Pandas库创建一个数据帧(DataFrame)，然后输出某行、某列和某个单元格的数据。
"""
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randint(1,10,(3,4)), columns=[0,1,2,3])#生成3行4列位置
print("随机创建3行4列的表格如下：")
print(df)#输出3行4列的表格
print("输出第二行：")
print(df.iloc[[1]])
print("输出列标签为2的列：")
print(df[2])
print("输出第二行第二列数据：")
print(df.iat[1, 1])

