from typing import Optional, Awaitable

import tornado.web


class RouteResource(tornado.web.RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def get(self):
        self.write("Basic Limit Handler")
