import tornado.ioloop
import tornado.web

from src.resource.route_resource import RouteResource


def make_app():
    return tornado.web.Application([
        (r"/", RouteResource),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
