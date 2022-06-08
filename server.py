import tornado.ioloop
import tornado.web
from tornado.escape import json_decode
from api import writeGPIO
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        pin=int(self.get_argument('pin'))
        state=int(self.get_argument('s'))
        print("pin", pin, state)
        writeGPIO(pin, state)
        self.write('{"success":true,"error":null}')
    def post(self):
        if (self.request.body):
            payload=json_decode(self.request.body)
        self.write("OK")

def make_app():
    return tornado.web.Application([
        (r"/api/relays", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
