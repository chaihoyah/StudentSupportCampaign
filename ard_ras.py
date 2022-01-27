import pyfirmata
import http.server
import time
import json

class HTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    # 부모 클래스 init 및 arduino, servo motor 관련 init 추가
    def __init__(self, request, client_address, server):
        self.DELAY = 1
        self.MAX = 175
        self.MIN = 5
        self.ANG = 90
        self.board = pyfirmata.Arduino('/dev/ttyUSB0')
        self.servo = self.board.get_pin('d:11:s')
        
        http.server.BaseHTTPRequestHandler.__init__(self, request, client_address, server)

    # Post가 왔을 때
    def do_POST(self):
        # rfile에 post된 값을 'Content-Length'만큼 읽어옴
        content_len = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_len)

        print(post_body)
        print(type(post_body))

        # bytes -> str decode
        mm = post_body.decode('utf-8')

        # 받은 값에서 실제 value parsing
        temp = mm.split(":")
        temp = temp[-1].split("}")
        temp = temp[0]
        print(temp)

        # 1이 들어오면 open (servo motor 90도 회전), 2가 들어오면 close (servo motor -90도 회전)
        try:
            num = int(temp)
            if num == 1:
                print("in")
                print(num)
                self.move_servo(self.ANG)
                time.sleep(1)
            elif num == 2:
                print("in")
                print(num)
                self.move_servo(0)
                time.sleep(1)
        except:
            print("Got wrong value")

        # http post에 대한 response 보냄
        self.response(200, "Hello")
        #return http.server.BaseHTTPRequestHandler.do_POST(self)

    #Get을 할 때
    def do_GET(self):
        
        self.route()
    
    def route(self):
        
        if self.path == '/hello':
            self.hello()
        else:
            self.response_404_not_found()
    
    def hello(self):
        self.response(200,"Hello")
    
    def response_404_not_found(self):
        self.response(404, "Command not found")
    
    def response(self, status_code, body):
        self.send_response(status_code)
        
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        
        self.wfile.write(body.encode('utf-8'))

    # 각도 v까지로 모터를 회전
    def move_servo(self, v):
        self.servo.write(v)
        print("inMove")
        self.board.pass_time(self.DELAY)
        
# ADDRESS = '***.***.***.***' , PORT (IP 주소, Port 번호)

listener = http.server.HTTPServer(ADDRESS, HTTPRequestHandler)
print(f'waiting')
listener.serve_forever()
