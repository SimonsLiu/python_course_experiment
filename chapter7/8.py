"""
@author:Liushihao
@time:2020/4/27:16:34
@email:Liushihao_1224@163.com
@describe:编写一个程序，实现对一篇中文文章进行分词和统计，结果使用词云图展示。
"""
# -*- coding: utf-8 -*-
import jieba
import jieba.posseg as posseg
import jieba.analyse as analyse
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from imageio import imread
doupo = open('7_txt.txt',encoding='UTF-8').read()
print(len(doupo))
print("  ".join(analyse.extract_tags(doupo, topK=20, withWeight=False, allowPOS=())))
words = " ".join(jieba.cut(doupo))
wc = WordCloud(
    width=800,
    height=600,
    background_color="#ffffff",  # 设置背景颜色
    max_words=500,  # 词的最大数（默认为200）
    max_font_size=60,  # 最大字体尺寸
    min_font_size=10,  # 最小字体尺寸（默认为4）
    colormap='bone',  # string or matplotlib colormap, default="viridis"
    random_state=10,  # 设置有多少种随机生成状态，即有多少种配色方案
    mask=plt.imread("1.png"),  # 读取遮罩图片！！
    font_path='C:/Windows/Fonts/simhei.ttf'
)
my_wordcloud = wc.generate(words)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
wc.to_file('ciyun.png')  # 保存图片文件