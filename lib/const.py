# Date: 01/07/2019
# Author: Mohamed
# Description: Constants

header = '''
GET /?{} HTTP/1.1\r\n
Connection: keep-alive\r\n
User-Agent: {}\r\n\r\n
'''.replace('\n\n', '\n').replace('\nGET', 'GET')
