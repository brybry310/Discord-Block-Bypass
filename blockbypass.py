import os
import requests
import time

from colorama import Fore, init
init(convert=True)

class BlockBypass:
    def __init__(self, token, userId):
        self.channelId = None
        self.userId = userId
        self.api = 'https://discord.com/api/v8/'
        self.headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
        }

    def generateChannel(self):
        request = requests.post(f'{self.api}users/@me/channels', json={'recipients': [ self.userId ]}, headers=self.headers)

        if request.status_code == 200:
            print('[Successfully] Created the channel\n')
            self.channelId = request.json()['id']
            self.main()
        else:
            print('[Un-Successfully] Couldn\'t create the channel!')
            print(request.status_code, request.json())
            exit(0)

    def sendMessage(self, message):
        request = requests.post(f'{self.api}channels/{self.channelId}/messages', json={'content': message}, headers=self.headers)

        if request.status_code == 200:
            print('[Successfully] Sent the message\n')
        else:
            print('[Un-Successfully] ', request.json(), '\n')

        self.main()

    def main(self):
        content = input('[Message To Send] -> ')

        self.sendMessage(content)

if __name__ == '__main__':
    print('\nWelcome to BlockBypass.\nWhat is it -> This is a simple script that let\'s you talk to anyone who YOU blocked.\nWhy -> Just a simple troll\nHow -> Someone by the name of Yaekith discovered this a while ago (2018) while messing around with the discord api.\n\n')
    # Variables
    token = input('Token -> ')
    userId = input('UserId to Message -> ')
    print('\n')
    # Class Definition
    yesnt = BlockBypass(token, userId)
    yesnt.generateChannel()
    yesnt.main()
