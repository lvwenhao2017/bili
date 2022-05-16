import time
import json

def timeStamp_to_time(timeStamp):
    timeArray = time.localtime(timeStamp)
    return time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

"""
置顶信息在['data']['cards'][i]['extra']['is_space_top'](1/0)
"""


class Dynamic(object):
    def __init__(self, item):
        self.item = item
        self.up = ''
        self.time = ''
        self.content = ''
        self.type = ''
        self.what_type()  # 填充type
        self.what_content()

    def __str__(self):
        if self.type == '动态' or self.type == '图片动态':
            return '''
up主:{}
时间:{}
内容:
{}
            '''.format(self.up, self.time, self.content)
        elif self.type == '视频':
            return '''
up主:{}
上传时间:{}
标题:{}
            '''.format(self.up, self.time, self.content)
        elif self.type == '小视频':
            return '''
up主:{}
上传时间:{}
内容:
{}
            '''.format(self.up, self.time, self.content)

    def what_type(self):
        item = self.item['card']
        item = json.loads(item)
        if 'user' in item.keys():  # 存在user标签,动态或者短视频
            if 'tags' in item['item'].keys():
                self.type = '小视频'
            elif 'timestamp' in item['item'].keys():
                self.type = '动态'
            else:
                self.type = '图片动态'
        else:  # 视频
            self.type = '视频'

    def what_content(self):  # 填充动态对象的up,time,content这些内容
        item_0 = self.item
        self.up = item_0['desc']['user_profile']['info']['uname']
        item = item_0['card']
        item = json.loads(item)
        if self.type == '动态':
            timestamp = item_0['desc']['timestamp']
            self.time = timeStamp_to_time(timestamp)
            self.content = item['item']['content']
        elif self.type == '图片动态':
            timestamp = item_0['desc']['timestamp']
            self.time = timeStamp_to_time(timestamp)
            self.content = item['item']['description']
        elif self.type == '视频':
            self.time = timeStamp_to_time(item['pubdate'])
            self.content = item['title']
        elif self.type == '小视频':
            self.time = item['item']['upload_time']
            self.content = item['item']['description']

