import requests 
import time
import json
from requests.auth import HTTPProxyAuth
import random
import time
import pyautogui


a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
b = 'abcdefghijklmnopqrstuvwxyz'
c = '01234567890123456789'
d = '"()!*-+'
all_password = a + b + c + d
all_username = a + b + c
dlina = 12
for i in range(10000):
    password_gen = "".join(random.sample(all_password, dlina))
    username_gen = "".join(random.sample(all_username, dlina))
    print("Username:" + username_gen, end = " ")
    print("Password:" + password_gen)


    headers ={
    'Host': 'www.instagram.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.instagram.com/',
    'Cookie': '',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'TE': 'Trailers'
    }
    data = {
    'client_id':'W8AvBQ1ALAAEbfRj5lRKWtgBiO1iL',
    'first_name':'Vladimir Astafeev',   
    'opt_into_one_tap':'false',
    'password':password_gen,    
    'email':'1234@gmail.com',
    'username':username_gen 
    }

    url_reg = 'https://www.instagram.com/accounts/web_create_ajax/'
    with requests.Session() as session:
        session.headers.update(headers)
        req = session.get(url_reg)

        session.headers.update({'X-CSRFToken':req.cookies['csrftoken']})
        time.sleep(2)
