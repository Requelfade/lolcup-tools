##pip install colorama
import json
from pprint import pprint
import urllib3
urllib3.disable_warnings()

import requests

from colorama import init as coloramainit
from colorama import Fore, Back, Style
coloramainit()
"""
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
"""
lolpath="E:\3a\programy\"

headers = {
    'Accept' : 'application/json',
    'Authorization' : 'Basic cmlvdDpnV0puTDVya0ZEWFB2cWlydjBCMUl3'
}

def rqget(url, headers):
    url='https://127.0.0.1:65119/'+url
    return requests.get(url, headers=headers, verify=False)
def rqpost(url, headers):
    url='https://127.0.0.1:65119/'+url
    return requests.post(url, headers=headers, verify=False)

def CheckLauncherScale():
    LauncherScale = rqget('riotclient/zoom-scale', headers)
    LauncherScale.json
    if LauncherScale.text == '1.25':
        return Fore.GREEN + 'OK'
    else:
        rqpost('riotclient/zoom-scale?newZoomScale=1.25', headers)
        return Fore.YELLOW + 'Fixed'
        


print('Launcher Size: ['+ CheckLauncherScale() + Fore.RESET + ']')

print(CheckLauncherScale())

data = rqget("lol-collections/v1/inventories/chest-eligibility", headers).text
parsed_json = json.loads(data)
print(parsed_json["earnableChests"])