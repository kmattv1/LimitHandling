import tornado.ioloop
from tornado.options import define, options
import tornado.web

from src.web_application import WebApplication

if __name__ == "__main__":
    tornado.options.define('port', default='8888', help='Port to listen on')
    tornado.options.parse_command_line()

    app = WebApplication()
    app.listen(port=8888)

    tornado.ioloop.IOLoop.current().start()
