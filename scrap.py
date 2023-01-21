import requests
from vars import vk_token, vk_group, water_names
import time


def search_post(water, fish=None):
    if fish is None:
        query = f'#{water}'
    else:
        query = f'#{water}, {fish}'
    data = {
        'domain': 'pp4wikipedia',
        'query': query,
        'owners_only': '0',
        'count': '5',
        'extended': '0',
        'access_token': vk_token,
        'v': '5.131',
    }
    response = requests.post('https://api.vk.com/method/wall.search', data=data)
    r = response.json()
    data = r['response']['items']
    msgs = []
    for i in data:
        id = i['id']
        d = i['date']
        date_post = time.ctime(d)
        text = i['text']
        url = f"https://vk.com/pp4wikipedia?w=wall{i['from_id']}_{id}"
        msg = f'{date_post}\n{text}\n{url}'
        msgs.append(msg)
    return msgs


def lastposts():
    url = f'https://api.vk.com/method/wall.get?domain={vk_group}&count=10&access_token={vk_token}&v=5.131'
    r = requests.get(url).json()
    data = r['response']['items']
    msgs = []
    for i in data:
        if 'is_pinned' in i:
            pass
        else:
            id = i['id']
            d = i['date']
            date_post = time.ctime(d)
            text = i['text']
            url = f"https://vk.com/pp4wikipedia?w=wall{i['from_id']}_{id}"
            msg = f'{date_post}\n{text}\n{url}'
            msgs.append(msg)
    return msgs