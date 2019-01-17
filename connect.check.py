import socket
import time

s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

for x in range(5):
    try:
        s.connect("app.sock")
        print("ok")
        s.close()
        break
    except socket.error as e:
        print(e)
        time.sleep(1)

print("done")
