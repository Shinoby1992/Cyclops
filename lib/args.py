# Date: 09/25/2019
# Author: Pure-L0G1C
# Description: Arguments 

from re import match 
from argparse import ArgumentParser

class Args(object):

 def __init__(self):
  self.ip = None
  self.port = None
  self.threads = None
  self.is_aggressive = False
 
 def error(self, error):
  print('Error: {}'.format(error))
  
 def get_args(self): 
  parser = ArgumentParser()

  parser.add_argument('-i',
                     '--ip',
                     required=True,
                     help='the targeted ip. \
                      Example: -i 127.0.0.1')

  parser.add_argument('-p',
                     '--port',     
                     default=str(80),
                     help='the targetd ports. \
                      Example: -p 80')

  parser.add_argument('-t',                      
                     '--threads',   
                     default=str(256),                  
                     help='number of threads. \
                      Example: -t 256') 

  parser.add_argument('-m',
                     '--mode',
                     default='S',
                     help='mode of attack; (A)ggressive (S)tealthy. \
                      Example: -m S') 

  return parser.parse_args()

 def set_args(self):
  args = self.get_args()

  self.ip = args.ip 
  self.port = args.port
  self.threads = args.threads 
  self.is_aggressive = args.mode 

  if any([not self.valid_ip, not self.valid_port, not self.valid_threads, not self.valid_mode]):
   return False
  return True 

 @property 
 def valid_threads(self):
  if not self.threads.isdigit():
   self.error('Threads must be an integer')
   return False

  if int(self.threads) <= 0:
   self.error('Threads must not be less than 1')
   return False

  self.threads = int(self.threads)
  return True 

 @property
 def valid_mode(self):
  mode = self.is_aggressive.upper()
  if all([mode != 'A', mode != 'S']):
   self.error('Mode must be set to A or S')
   return False
  self.is_aggressive = True if mode == 'A' else False
  return True

 @property 
 def valid_ip(self):
  if not match(r'^(?!0)(?!.*\.$)((1?\d?\d|25[0-5]|2[0-4]\d)(\.|$)){4}$', self.ip):
   self.error('Invalid IP address')
   return False 
  return True

 @property 
 def valid_port(self):
  #  check if number
  for item in self.port:
   if not item.isdigit():
    return False    

  # check if number starts with a zero
  if int(self.port[0]) == 0:
   return False 

  # check if number is larger than 65535
  if int(self.port) > 65535:
   return False 
  self.port = int(self.port)
  return True