import re
import requests
import b64woff
from fontTools.ttLib import TTFont

def get_papge_data(page):
    headers = {
        'user-agent': 'yuanrenxue.project',
    }

    params = (
        ('page', page),
    )

    resp = requests.get('https://match.yuanrenxue.com/api/match/7', headers=headers, params=params)
    datas = resp.json()['data']
    down_load_woff_data(resp.json()['woff'])
    value_data_list = []
    for data in datas:
        value_data = data['value'].replace('&#x','').replace(' ','')
        value_data_list.append(value_data)
    return value_data_list

def down_load_woff_data(woff_data):
    b64woff.b64woff(woff_data,'online_font_data.woff')
    print('在线woff文件已下载完毕')

def paese_online_woff_data():
    online_font = TTFont('./online_font_data.woff')
    online_font.saveXML('online_font.xml')
    extraName = str(online_font.getTableData('post') + b'\0x2')
    pat = re.compile(r'uni(.*?)\\x0')
    number_value = pat.findall(extraName)
    return number_value


all_number_list = []
def parse_real_data(value_data_list,number_data):
    print(number_data)
    print(value_data_list)
    number_data_list = [number_data[9]]
    number_data_list.extend(number_data[0:9])
    print(number_data_list)
    number_data_dict = {number_data_list[i]:i for i in range(10)}
    print(number_data_dict)
    # for numbers in value_data_list:
    #     all_number_list.append(int(''.join([str(__) for __ in [number_data_dict[numbers[index*4: (index+1)*4]] for index in range(int(len(numbers)/4))]])))
    for j in value_data_list:
        number_list = []
        for i in range(int(len(j)/4)):
            sigle_number =j[i*4:(i+1)*4]
            number = number_data_dict[sigle_number]
            number_list.append(str(number))
            all_number = ''.join(number_list)
            all_number = int(all_number)
        all_number_list.append(all_number)

if __name__ == '__main__':
    for page in range(1,6):
        value_data_list = get_papge_data(page)
        number_data = paese_online_woff_data()
        parse_real_data(value_data_list,number_data)
    max = max(all_number_list)
    print(f'最高的点数为{max},它的位置在{all_number_list.index(max)+1}位')
