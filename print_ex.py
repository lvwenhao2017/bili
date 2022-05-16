import json
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
def print_dict(_dict, n_tab=0):
    """打印一个字典"""
    if isinstance(_dict, dict):
        for k, v in _dict.items():
            print('\t' * n_tab, end='')
            print("{}{}:".format('\t', k), end='')
            if isinstance(v, dict):
                print('')
                print_dict(v, n_tab+1)
            else:
                decision(v, n_tab)

def print_list(_list, n_tab):
    print(_list)


def decision(object, n_tab):
    if isinstance(object, str):
        if object.find('{') == 0:
            value = json.loads(object)  # 转化为字典
            print('')
            print_dict(value, n_tab+1)
        elif object.find('[') == 0:
            value = list(object[1:-1])  # 转化为列表
            print_list(value, n_tab)
        else:  # 正常str
            if object != '':
                print(object)
            else:
                print("''")
    elif isinstance(object, list):
        print_list(object, n_tab)
    else:  # 元素是正常值
        print(object)