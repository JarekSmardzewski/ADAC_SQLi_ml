import requests
import random
import time
import string
ADDRESS = '127.0.0.1'
PORT = '8888'
SLEEP = 1
ENDPOINTS = ['products.php','details.php','account.php']
ALPHABET = list(string.ascii_uppercase)

RUNTIME = 1000
SUFFIX  = '@seattlesound.net '

while(RUNTIME >= 0):
    target = ENDPOINTS[random.randint(0, len(ENDPOINTS) - 1 )]
    param = ''
    
    if (target == 'products.php'):
        param = 'type='
        for x in range(0,  random.randint(2, 30)):
            param = param + random.choice(ALPHABET)

    elif(target == 'details.php'):
        param = 'type='
        for x in range(0,  random.randint(2, 30)):
            param = param + random.choice(ALPHABET)
        param = param +'&prod='
        for x in range(0,  random.randint(2, 30)):
            param = param + random.choice(ALPHABET)

    elif(target == 'account.php'):
        password = ''
        user = ''
        for x in range(0,  random.randint(2, 30)):
            user = user + random.choice(ALPHABET)
        user = user + SUFFIX
        for x in range(0,  random.randint(2, 30)):
            password = password + random.choice(ALPHABET)
        payload = {'usermail': user,
                    'password' : password}

    if(target == 'account.php'):
        response = requests.post('http://'+ADDRESS +":"+ PORT +"/" + target, json=payload)   
    else:
        response = requests.post('http://'+ADDRESS +":"+ PORT +"/" + target + '?'+ param )
    if(response.status_code == 200):
        RUNTIME = RUNTIME - 1
        time.sleep(SLEEP)
    #print('http://'+ADDRESS +":"+ PORT +"/" + target + '?'+ param)
    #if(target == 'account.php'):
    #    print(payload)