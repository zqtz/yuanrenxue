import jsonpath
import requests
from requests import utils
from hyper.contrib import HTTP20Adapter

headers = {
    'cookie':'Hm_lvt_0362c7a08a9a04ccf3a8463c590e1e2f=1642053432,1642298231,1642339082,1642465597; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1642556169,1642563455,1642564137,1642573570; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1642509275,1642556172,1642563520,1642577074; tk=-569410077022290228; sessionid=1waodlhihvl2fek0s36mousscnclo9o9; yuanrenxue_cookie=1642577217|2bfaWf0b9fqE4qAaAh3meDxKrPX6w9LYocEteu6LDWom4QwUCtdBpFXNw9mVsVlMYXz6imfh8mpKozFgIzrYWfBkP6v700SqLAWBIWx7SlAgTF1TN9N4zzs62tAfpbJeZfwO3S8OZByjRnH7A7byc75veKQgVWERMSyvHiza7xNjyiyCaMHTIV; m=cc430c1532e13aa78a8929050b783f90; RM4hZBv0dDon443M=Qi9V4mypEdg+5XzIl2T0+mDkE42X15uWfD2yziIcbgOzlrA5yH4GH/q/W26JeOnBqOaXZPwdvz0uBKoanFSEIOhLXJwGv0CVNZf+ldtdIeoMN3oT8JNsQKFWUpwS4RixHvO/8HT+yQZ999oenoZ5wJOsmJKYI/LpfYl77HKHJVh/6zezv4k1F04ulWXw9drSadJdBfR/sHb7kFWN5Xe8VtgCr/sAtA3MuT1yaevFVis=; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1642579486; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1642579570',
    'user-agent':'yuanrenxue.project',
}
session = requests.session()
session.headers = headers
session.mount('https://match.yuanrenxue.com',HTTP20Adapter())
result = 0
for page in range(1,6):
    url = f'https://match.yuanrenxue.com/api/match/17?page={page}'
    resp = session.get(url).json()
    datas = resp['data']
    for data in datas:
        print(data['value'])
        result+=data['value']
print('答案为:',result)