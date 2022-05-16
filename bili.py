# 爬取动态信息
import urllib3
import requests
import json
from dynamic import Dynamic
# 啦啦啦

"""
req = requests.get(url)
json = req.json()--->返回json格式数据,得到一个字典
编码问题
    # print(req.headers['content-type'])
    # print(req.encoding)
    # print(req.apparent_encoding)
    确定网页charset,可以直接设置encoding
"""

if __name__ == '__main__':
    dynamics = []
    # dynamics_type = {'动态': 0, '小视频': 0, '视频投稿': 0}
    offset = '0'
    flag = 1
    # uid = input("请输入up主的uid:")  # 420249427
    while True:
        if not flag:
            break
        # url = "https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history?&host_uid={}".format(uid)
        # url += "&offset_dynamic_id={}&need_top=1".format(offset)
        url = "https://www.bilibili.com/video/BV1Vf4y127N5?spm_id_from=333.337.search-card.all.click"
        req = requests.get(url)
        req.encoding = 'utf-8'
        html = req.text
        item_0 = json.loads(req.text)['data']
        flag = item_0['has_more']
        offset = str(item_0['next_offset'])
        num = len(item_0['cards'])
        for i in range(num):
            item = item_0['cards'][i]
            dynamic = Dynamic(item)
            print(dynamic)
            dynamics.append(dynamic)
        state = input("已收集{}条动态,是否继续?(y/n):".format(len(dynamics)))
        if state == 'n':
            break

