import zmq
import socket


def pythagoras(zcontext, url):
    zsock = zcontext.socket(zmq.REP)
    zsock.bind(url)
    while True:
        numbers = zsock.recv_json()
        zsock.send_json(sum(n * n for n in numbers))


def main(zcontext):
    address = socket.gethostbyname(socket.getfqdn())
    reqrep = 'tcp://'+address+':6701'
    pythagoras(zcontext, reqrep)


if __name__ == '__main__':
    main(zmq.Context())
