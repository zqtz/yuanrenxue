import requests
import os
import execjs


def main():
    url = 'https://match.yuanrenxue.com/match/2'
    response = requests.get(url)

    with open('02.js', 'wb') as f:
        f.write(response.content[8:-9])

    os.system('node ast')

    sums = 0
    nodejs = os.popen('node decrypt')
    m = nodejs.read().replace('\n', '').split('; ')[0]
    nodejs.close()
    print(m)
    headers = {
        'cookie': m,
        'User-Agent': 'yuanrenxue.project'
    }
    for page in range(1, 6):
        url = 'https://match.yuanrenxue.com/api/match/2?page='+str(page)
        response = requests.get(url, headers=headers).json()
        print(response)
        for each in response['data']:
            sums += each['value']
    print(sums)
    # 总和：248974

if __name__ == '__main__':
    main()