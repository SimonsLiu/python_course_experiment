"""
@author:Liushihao
@time:2020/3/18:15:35
@email:Liushihao_1224@163.com
@describe:
"""
population = 13
year = 2015
while(population < 20):
    population = population*(1+0.008)
    year+=1

add_year = year-2015
print("%d年后，我国人口超过20亿"%add_year)