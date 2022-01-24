import execjs
import time
import requests

def get_m():
    ts = int(time.time()*1000)
    node = execjs.get()
    ctx = node.compile(open('./exam06.js',encoding='utf-8').read())
    funcName = "get_q_m_value()"
    [timestamp,m] = ctx.eval(funcName)
    q = '1-' + str(timestamp) + '|'
    return m,q


def get_result():
    headers = {
        'User-Agent': 'yuanrenxue.project'
    }
    m,q = get_m()
    count = 0
    for page in range(1,6):
        params = {
            'page':page,
            'm':m,
            'q':q
        }
        url = 'https://match.yuanrenxue.com/api/match/6'
        response = requests.get(url, headers=headers,params=params)
        datas = response.json()['data']
        print(f'第{page}页的数据为:{datas}')
        for data in datas:
            value = data['value']
            print(value)
            count += data['value']*24
    return count
print('答案为:',get_result())

