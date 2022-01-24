import pywasm
import time
import math
import random
import requests


def env_abort(_: pywasm.Ctx):
    return

def get_m():
    t1 = int(time.time() / 2)
    t2 = int(time.time() / 2 - math.floor(random.random() * 50 + 1))
    vm = pywasm.load('./main.wasm', {
        'env': {
            'abort': env_abort,
        }
    })
    r = vm.exec('encode', [t1, t2])
    m = str(r) + '|' + str(t1) + '|' + str(t2)
    return m


def get_answer():
    count = 0
    for page in range(1,6):
        url = f'https://match.yuanrenxue.com/api/match/15?m={get_m()}&page={page}'
        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,en-US;q=0.6',
            'cache-control': 'no-cache',
            'cookie': 'Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1642383578,1642410620,1642421174,1642421508; sessionid=bnc97a421v0hq2tgjl3r7n0xmdioa19w; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1642410409,1642421165,1642421301,1642465453; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1642465453',
            'pragma': 'no-cache',
            'referer': 'https://match.yuanrenxue.com/match/15',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'yuanrenxue.project',
            'x-requested-with': 'XMLHttpRequest',
        }
        resp = requests.get(url,headers=headers)
        datas = resp.json()['data']
        for data in datas:
            print(data['value'])
            count += data['value']
    print('答案为:', count)


if __name__ == '__main__':
    get_answer()


        


