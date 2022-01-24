import time
import requests
import execjs
from urllib.parse import urlencode


headers = {
    'user-agent':'yuanrenxue.project',
    'cookie':'Hm_lvt_0362c7a08a9a04ccf3a8463c590e1e2f=1642053432,1642298231,1642339082,1642465597; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1642556169,1642563455,1642564137,1642573570; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1642509275,1642556172,1642563520,1642577074; tk=-569410077022290228; sessionid=1waodlhihvl2fek0s36mousscnclo9o9; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1642577099; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1642577107',
    'pragma':'no-cache',
    'referer':'https://match.yuanrenxue.com/match/16',
    'sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-origin',    'x-requested-with':'XMLHttpRequest',
}
with open('day16.js', mode='r', encoding='utf-8') as f:
    JsData = f.read()
[p_s, m] = execjs.compile(JsData).call('get_enc_m')
print([p_s, m])
count = 0
for page in range(1,6):
    start_url = f'http://match.yuanrenxue.com/api/match/16?page={2}&m={m}&t={p_s}'
    res = requests.get(url=start_url)
    datas = res.json()['data']
    for data in datas:
        count+=data['value']
        print(data['value'])
print('答案为:',count)



