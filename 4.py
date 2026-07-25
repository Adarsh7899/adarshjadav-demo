import requests

url = 'https://fanyi.baidu.com/sug'

while True:
    text = input('请输入中文或者英语：').strip()
    if text == 'q':
        break

    data = {'kw': text}

    resp = requests.post(url, data)

    found = False
    if resp.status_code == 200:
        data = resp.json()
        if data['errno'] == 0:
            ds = data['data']
            for kv in ds:
                if kv['k'] == text:
                    found = True
                    print(kv['v'])
            if not found:
                print('没有找到')
        else:
            print(data)
    else:
        print(resp.content)
