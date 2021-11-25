import socket
import sys
ss=sys.argv[1]

def conn():
    try:
        socket.create_connection(("1.1.1.1", 53))
    except OSError:
        print("No Internet Connection...")
        sys.exit()

conn()
try:
    ip=socket.gethostbyname(ss)
    print("\033[1;31m",ss ,"\033[1;36m==>\033[1;37m ", ip)
except:
    print("\033[1;37m {} \033[1;31mName or service not known".format(ss))
