import requests
import random
import time
import string
ADDRESS = '192.168.43.6'
PORT = '80'
SLEEP = 0.5
ENDPOINTS = ['products.php','details.php']
ALPHABET = list(string.ascii_uppercase)

RUNTIME = 1000

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

        response = requests.get('http://'+ADDRESS +":"+ PORT +"/" + target + '?'+ param )
    if(response.status_code == 200):
        RUNTIME = RUNTIME - 1
        time.sleep(SLEEP)
    print(RUNTIME)
    print('http://'+ADDRESS +":"+ PORT +"/" + target + '?'+ param)