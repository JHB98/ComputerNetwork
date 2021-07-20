import zmq
import socket


def tally(zcontext, in_url, out_url):
    isock = zcontext.socket(zmq.PULL)
    isock.bind(in_url)
    # Push pull message queue for client-tally
    osock = zcontext.socket(zmq.PUSH)
    osock.connect(out_url)
    num = 1
    p = q = 0
    while True:
        decision = isock.recv_string()
        q += 1
        if decision == 'Y':
            p += 4
        # receive number of iterations and pi value to client
        osock.send_string(str(num) + ' ' + str(p/q))
        num += 1


def main(zcontext):
    in_address = socket.gethostbyname(socket.getfqdn())
    out_address = input("Client address : ")
    in_pushpull = 'tcp://'+in_address+':6702'
    out_pushpull = 'tcp://'+out_address+':6704'

    tally(zcontext, in_pushpull, out_pushpull)


if __name__ == '__main__':
    main(zmq.Context())
