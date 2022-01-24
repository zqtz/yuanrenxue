import requests
from requests import utils
session = requests.session()


number_list = []
for i in range(1,6):
    headers = {
        'Host':'match.yuanrenxue.com',
        'Connection':'keep-alive',
        'Content-Length':'0',
        'Pragma':'no-cache',
        'Cache-Control':'no-cache',
        'sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'sec-ch-ua-mobile':'?0',
        'User-Agent':'yuanrenxue.project',
        'sec-ch-ua-platform':'"Windows"',
        'Accept':'*/*',
        'Origin':'https://match.yuanrenxue.com',
        'Sec-Fetch-Site':'same-origin',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Dest':'empty',
        'Referer':'https://match.yuanrenxue.com/match/3',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,en-US;q=0.6',
        # 定期更新cookie
        'Cookie':'sessionid=3wnl7zqp05d6i8lildtfxyrft4n20ax1; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1642744575,1642815874,1642819847,1642856073; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1642765423,1642815874,1642819848,1642856073; m=pua; tk=1672229442160709740; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1642856926; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1642856999',
    }
    session.headers = headers
    response = session.post('https://match.yuanrenxue.com/jssm')
    resp = session.get(f'https://match.yuanrenxue.com/api/match/3?page={i}').json()
    datas = resp['data']
    for data in datas:
        print(data['value'])
        number_list.append(data['value'])
print('答案为:',max(number_list,key=number_list.count))




