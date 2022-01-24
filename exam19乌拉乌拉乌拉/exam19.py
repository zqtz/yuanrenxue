import requests

# 注释掉D:\Anaconda\install\Lib\site-packages\urllib3\util下的指纹算法,让网页不能识别出爬虫
count = 0
for page in range(1,6):
    headers = {
        'user-agent': 'yuanrenxue.project',
        'cookie': 'Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1642815874,1642819848,1642856073,1642988321; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1642815874,1642819847,1642856073,1642988327; tk=7570423014640128964; sessionid=yaa12xj5xtq13xw06dbyeq9ojb1wsryq; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1642988348; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1642988977',
    }
    params = (
        ('page', page),
    )
    response = requests.get('https://match.yuanrenxue.com/api/match/19', headers=headers, params=params)
    datas = response.json()['data']
    for data in datas:
        result = data['value']
        print(result)
        count+=result
print('答案为:'+str(count))

