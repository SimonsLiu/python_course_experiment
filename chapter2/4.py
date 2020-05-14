"""
@author:Liushihao
@time:2020/3/5:10:35
@email:Liushihao_1224@163.com
@describe:
"""
str = "君子之行，静以修身，俭以养德，非淡泊无以明志，非宁静无以致远"
print(str)

# 找到“德”下标 然后输出“德”
index_2 = str.find("德")
print(str[index_2])

# 找到这段字符串第一个和最后一个字符的下标，然后在原串中切片输出
sub_str = "非淡泊无以明志，非宁静无以致远"
sub_str_1 = str[str.find(sub_str[0]):str.find(sub_str[-1])]
print(sub_str_1)
