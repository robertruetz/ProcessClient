import sys
import socket
import time


def main():
    TCP_IP = '127.0.0.1'
    TCP_PORT = 1984
    BUFFER_SIZE = 1024
    IIS_EXPRESS_PATH = r"C:\Program Files (x86)\IIS Express\iisexpress.exe"
    MESSAGE = 'stop "{0}" with these args'.format(IIS_EXPRESS_PATH)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((TCP_IP, TCP_PORT))
        sock.send(bytes(MESSAGE + "\n"))
        start = time.clock()
        data = sock.recv(BUFFER_SIZE)
        end = time.clock()
        sock.close()
        elapsedMs = (end - start) * 1000
        print("Received: {0} in {1:.3g} seconds".format(data, elapsedMs))
    except socket.error as e:
        print("Could not connect to socket.\n{0}".format(str(e)))

if __name__ == "__main__":
    main()
