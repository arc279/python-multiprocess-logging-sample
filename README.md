# python multiprocess logging sample

via unix domain socket.

## start log receiver

```
python receiver.py
```

## start log sender

using [uwsgi](uwsgi.ini) web app as sample.

```
uwsgi uwsgi.ini
```

## output log

```
ab -n 10000 -c 100 http://127.0.0.1:3031/
```

## check your log lines

```bash
$ wc -l test.log
10000 test.log
```
