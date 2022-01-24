import re

import requests

headers = {
    'authority': 'match.yuanrenxue.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://match.yuanrenxue.com/match/8',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,en-US;q=0.6',
    'cookie': 'Hm_lvt_0362c7a08a9a04ccf3a8463c590e1e2f=1642298231,1642339082,1642465597,1642586792; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1642641253,1642662742,1642674407,1642744575; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1642662737,1642674404,1642727623,1642744577; tk=-3015013886331926054; sessionid=53fc0ydon3i20fuvq0mdppui82981gky; m=d723c59efe2bfdc3d4342b5402f2e599; RM4hZBv0dDon443M=VNy32fgzHwWGeoCUk4Ix09fzJI5RPZVmdG7ZxbzJzO4Hd2XtFua7PhgXoYYzsFiWbDpBgLPopJAK79+6ItCzGuyncuedYUI7Louvkui3A6x7iOP6j0IL9UMm4ml7/9EU0eA2u7/Qyl+DgF/Jfh46xr8d+SAd8NHJVJR5+8nUJvc8LaJ2ccMD1QJ8jnP/JkljD6eEmIXOr0TmEjf2iAw61KbSOLXfNObgcAErEm/nIn8=; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1642744740; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1642744782',
}

response = requests.get('https://match.yuanrenxue.com/api/match/8_verify', headers=headers)
data = response.json()['html']
print(data)
data1 = re.findall(r'<p>(.*?)</p>',data)
print(data1)
result = re.findall(r'src="(.*?)"',data)[0].replace('data:image/jpeg;base64,','')
print(result)
