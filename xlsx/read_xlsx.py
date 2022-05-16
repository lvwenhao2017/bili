import xlrd


def print_reward(lists: dict):
    for k, info in lists.items():
        print(k + ':')
        print('================')
        for index, name in enumerate(info['name']):
            print('\t姓名:', name)
            print('\t地址:', info['address'][index])
            print('\t电话:', info['phone'][index])
            print('\t=============')


"""D(4)列是几等奖,E(5)列是奖品,FGH分别是收件人地址和电话,11列是√标志已送"""
file_path = r'F:\project\python\bili\xlsx\获奖名单（7月19日更新）.xls'
file_path = file_path.encode('utf-8')
# 获取数据
data = xlrd.open_workbook(file_path)
# 获取sheet
table = data.sheet_by_name('Sheet1')

# 获取总行数
nrows = table.nrows

# 获取总列数
ncols = table.ncols

#获取一行的数值，例如第5行
# rowvalue = table.row_values(5)
#
# print(rowvalue)

lists = {}
reward = table.cell_value(3, 4)
reward = reward.replace('\n', '')
lists[reward] = {'name': [], 'address': [], 'phone': []}

# 根据uid确定是否为准确数据,uid为357165123的忽略不计
for i in range(3, nrows):

    # 读取表格信息
    uid = table.cell_value(i, 2)
    name = table.cell_value(i, 5)
    address = table.cell_value(i, 6)
    phone = table.cell_value(i, 7)
    flag = table.cell_value(i, 10)

    # 获取奖品信息
    if table.cell_value(i, 8) == '':
        reward = table.cell_value(i+1, 4)
        reward = reward.replace('\n', '')
        lists[reward] = {'name': [], 'address': [], 'phone': []}
        continue
    elif uid != '' and uid != '357165123' and name != '' and flag == '':
        # 取消换行符,初始化字典
        address = address.replace('\n', '')
        phone = int(phone)
        lists[reward]['name'].append(name)
        lists[reward]['address'].append(address)
        lists[reward]['phone'].append(phone)
print_reward(lists)






