# Date: 09/23/2018
# Author: Pure-L0G1C
# Description: Config file

header = '''
GET /?{} HTTP/1.1\r\n
Accept-Language: en-US,en;q=0.9\r\n
Accept-Encoding: gzip, deflate, br\r\n
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\n
User-Agent: {}\r\n\r\n
'''.replace('\n\n', '\n').replace('\nGET', 'GET')