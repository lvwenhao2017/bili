import cv2
import requests
from bs4 import BeautifulSoup
import pandas as pd
import jieba
import wordcloud
from matplotlib import pyplot as plt

"""重要信息如aid,cid都在heartbeats中->post请求"""
url = 'https://comment.bilibili.com/210288241.xml'  # heartbeat中cid
"""http://api.bilibili.com/pgc/review/user?media_id=28229233 番剧信息
    http://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn=2&type=1&oid=626339509&sort=2 评论(oid就是aid->avid)
    md号也就是mediaid -><a href="" class="media-desc>"""
request = requests.get(url)  # 获取页面
request.encoding = 'utf8'  # 因为是中文，我们需要进行转码，否则出来的都是unicode

soup = BeautifulSoup(request.text, 'lxml')
results = soup.find_all('d')  # 找出所有'd'
comments = [comment.text for comment in results]  # 得到完整的list
comments = [x.upper() for x in comments]  # 统一大小写
comments_clean = [comment.replace(' ', '') for comment in comments]  # 去掉空格

set(comments_clean)  # 看一下都有啥类似的没用的词语

useless_words = ['//TEST',
                 '/TESR',
                 '/TEST',
                 '/TEST/',
                 '/TEXT',
                 '/TEXTSUPREME',
                 '/TSET',
                 '/Y',
                 '\\TEST']

comments_clean = [
    element for element in comments_clean if element not in useless_words]  # 去掉不想要的字符
cipin = pd.DataFrame({'danmu': comments_clean})
cipin['danmu'].value_counts()  # 查看词频

danmustr = ''.join(element for element in comments_clean)  # 把所有的弹幕都合并成一个字符串
words = list(jieba.cut(danmustr))  # 分词
fnl_words = [word for word in words if len(word) > 1]  # 去掉单字

wc = wordcloud.WordCloud(
    width=1000,
    font_path='simfang.ttf',
    height=800)  # 设定词云画的大小字体，一定要设定字体，否则中文显示不出来
wc.generate(' '.join(fnl_words))

plt.imshow(wc)  # 看图
wc.to_file(r"C:\Users\吕文浩\Desktop\毕设\danmu_pic.png")  # 保存

