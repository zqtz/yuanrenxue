import base64

import requests

headers = {
    'user-agent': 'yuanrenxue.project',
    # 定期更新cookie
    'cookie': 'Hm_lvt_0362c7a08a9a04ccf3a8463c590e1e2f=1641860894,1642053432,1642298231,1642339082; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1642298373,1642298560,1642337871,1642383574; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1642294043,1642301869,1642337923,1642383578; tk=4232913597945731159; sessionid=dqiry7cjw1colklj2ueok5c9f23gf0le; yuanrenxue_cookie=1642392802|CG2ZBcEOsmTKHmx5f1KkquyqBGhlLf6tK2ORDRur45utSa0OmygsoIrNy2M0tLNfbJNhM4uH7sUVuzE2wxx1k; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1642392806; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1642392815',
}
count = 0
for page in range(1,6):
    page_b64 = base64.b64encode('yuanrenxue{}'.format(page).encode()).decode('utf-8')
    params = (
        ('page', page),
        ('m', page_b64),
    )
    response = requests.get('https://match.yuanrenxue.com/api/match/12', headers=headers, params=params)
    datas = response.json()['data']
    for data in datas:
        count+=data['value']
        print(data['value'])
print('答案为:',count)





