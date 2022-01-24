import base64
import requests

def b64woff(data,name):
    data = base64.b64decode(data)
    with open(name,'wb')as f:
        f.write(data)
        print('下载完毕')


# 测试
if __name__ == '__main__':
    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'yuanrenxue.project',
        'Referer': 'http://match.yuanrenxue.com/match/6',
    }
    resp = requests.get('https://match.yuanrenxue.com/api/match/7?page=2',headers=headers)

