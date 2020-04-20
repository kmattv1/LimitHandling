from tornado.web import HTTPError


def get_bad_request_error(message):
    return HTTPError(status_code=400, log_message=message)


def get_not_found_error(message):
    return HTTPError(status_code=404, log_message=message)


def get_internal_server_error(message):
    return HTTPError(status_code=500, log_message=message)
