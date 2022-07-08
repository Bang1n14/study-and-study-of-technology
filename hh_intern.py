import requests


url = 'https://spb.hh.ru/'

headers = {'Accept': '*/*',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'
}

req = requests.get(url, headers=headers)

src = req.text
print(src)