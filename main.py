import tornado.ioloop
import tornado.web
import tornado.httpserver
import os
from tornado.options import define, options
from handlers.mainhandler import MainHandler

define("port", 8001, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', MainHandler)
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            data_path=os.path.join(os.path.dirname(__file__), "datas"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=False,
            autoreload=False
        )
        super(Application, self).__init__(handlers, **settings)

def main():
    tornado.options.parse_command_line()
    try:
        http_server = tornado.httpserver.HTTPServer(Application())
        http_server.listen(options.port)
        tornado.ioloop.IOLoop.current().start()
    except OSError as error:
        print("Hata: %s" % error.strerror)

if __name__ == "__main__":
    main()