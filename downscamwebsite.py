import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = input("Enter the request url of the scam website: ") #put the request url of the website login

names = json.loads(open('names.json').read())

for name in names:
    name_extra = ''.join(random.choice(string.digits))

    username = name.lower() + name_extra + '@yahoo.com'
    password = ''.join(random.choice(chars) for i in range(8))

    response = requests.post(url, allow_redirects=True, data={
        'email': username, #Modify this, depends on the website post requesr of the username and password
        'password': password
    })

    if response.status_code == 200:
        print(f'Successfully sent request with username {username} and password {password}. Redirected to {response.url}')
    else:
        print(f'Failed to send request with username {username} and password {password}. Status code: {response.status_code}')
