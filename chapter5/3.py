"""
@author:Liushihao
@time:2020/4/8:21:55
@email:Liushihao_1224@163.com
@describe:
"""
def func(str):
    digital_num = 0
    word_num = 0
    other_num = 0
    for i in str:
        if i >='0' and i<='9':
            digital_num+=1
        elif i>='a' and i<='z':
            word_num+=1
        elif i>='A' and i<='Z':
            word_num+=1
        else:
            other_num+=1
    return digital_num,word_num,other_num

str = input("输入一个字符串，将返回其中数字、字母以及其他类型字符个数:")
dig_num , word_num, other_num = func(str)
print('字符串{}中的数字有{}个、字母有{}个其他字符有{}个'.format(str, dig_num, word_num, other_num))