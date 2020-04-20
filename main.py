import tornado.ioloop
from tornado.options import define, options
import tornado.web

from src.web_application import WebApplication

define("port", default=8888, help="run on the given port", type=int)

if __name__ == "__main__":
    tornado.options.parse_command_line()

    http_server = tornado.httpserver.HTTPServer(WebApplication(), decompress_request=True)
    http_server.listen(tornado.options.options.port)

    tornado.ioloop.IOLoop.instance().start()
