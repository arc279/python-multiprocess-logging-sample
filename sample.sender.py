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
sh = logging.handlers.SocketHandler(
    host='app.sock',
    port=None
)

logger.addHandler(sh)
logger.info('sample message')
