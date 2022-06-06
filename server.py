import tornado.ioloop
import tornado.web
from tornado.escape import json_decode
class MainHandler(tornado.web.RequestHandler):
    def post(self):
        if (self.request.body):
            self.write(json_decode(self.request.body))
	

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
