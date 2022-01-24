import execjs
import requests
url = 'https://match.yuanrenxue.com/match/13'

count = 0
for page in range(1,6):
    headers = {
        'User-Agent': 'yuanrenxue.project',
        'cookie': 'sessionid=dqiry7cjw1colklj2ueok5c9f23gf0le;'
    }
    res = requests.get(url,headers=headers)
    ck = res.text.replace("<script>document.cookie=('", "").replace("')+('", "").replace(
        "')+';path=/';location.href=location.pathname+location.search</script>", "")
    cookie = {
        'cookie': f'sessionid=dqiry7cjw1colklj2ueok5c9f23gf0le; {ck}'
    }
    headers.update(cookie)
    resp = requests.get(f'https://match.yuanrenxue.com/api/match/13?page={page}',headers=headers)
    results = resp.json()['data']
    for result in results:
        count += result['value']
        print(result['value'])
print('答案为:',count)
