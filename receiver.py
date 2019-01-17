# -*- coding:utf-8 -*-
import os
import socketserver
import logging
import _pickle as cPickle
import struct


class ThreadingUnixStreamServer(socketserver.ThreadingMixIn, socketserver.UnixStreamServer):
    pass


class SocketLogHandler(socketserver.StreamRequestHandler):
    def handle(self):
        print("connect from:", self.client_address)
        logger = logging.getLogger(__name__)

        while True:
            chunk = self.request.recv(4)
            if len(chunk) < 4:
                break

            slen = struct.unpack(">L", chunk)[0]
            chunk = self.request.recv(slen)
            while len(chunk) < slen:
                chunk = chunk + self.request.recv(slen - len(chunk))

            obj = cPickle.loads(chunk)
            record = logging.makeLogRecord(obj)

            logger.handle(record)

        self.request.close()


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("\t".join([
        "[%(asctime)s]",
        "%(levelname)s",
        "%(name)s",
        "[p%(process)s:%(threadName)s]",
        "[%(pathname)s:%(lineno)d]",
        "%(message)s",
    ]))

    h1 = logging.FileHandler(filename="test.log")
    h1.setLevel(logging.INFO)
    h1.setFormatter(formatter)
    logger.addHandler(h1)

    server = ThreadingUnixStreamServer("app.sock", SocketLogHandler)
    print('pid: ', os.getpid())
    print('listening:', server.socket.getsockname())
    server.serve_forever()
