# -*- coding:utf-8 -*-
import logging
import logging.handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
sh = logging.handlers.SocketHandler(
    host='app.sock',
    port=None
)
sh.setLevel(logging.DEBUG)
logger.addHandler(sh)


def application(environ, start_response):
    status = '200 OK'
    output = b'Hello World!'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    logger = logging.getLogger(__name__)
    logger.info([status, response_headers, output])
    return [output]
