import re
import requests
import execjs

# node = execjs.get()
# ctx = node.compile(open('exam01.js', encoding='utf-8').read())
# funcName = 'getvalue()'
# m = ctx.eval(funcName)
# print(m)
# exit()

def get_plane_ticket_peice(page):
    node = execjs.get()
    ctx = node.compile(open('exam01.js', encoding='utf-8').read())
    funcName = 'getvalue()'
    m = ctx.eval(funcName)
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,en-US;q=0.6',
        'cache-control': 'no-cache',
        'cookie': 'sessionid=bsn3dg4fi6spw7itaebx8dwufiujqku6; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1642143953,1642146543,1642147824,1642218423; m=20d3d565d264f2a61a76357044b88b63|1642224853000; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1642212896,1642213205,1642213388,1642224854; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1642224976',
        'pragma': 'no-cache',
        'referer': 'https://match.yuanrenxue.com/match/1',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'yuanrenxue.project',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'page': page,
        'm': m,
    }
    response = requests.get('https://match.yuanrenxue.com/api/match/1?', headers=headers, params=params)
    datas = response.json()['data']
    return datas

count = 0
price = 0
for page in range(1,6):
    datas  =get_plane_ticket_peice(page)
    for data in datas:
        print(data['value'])
        price += data['value']
        count += 1
print('答案为:', price / count)






