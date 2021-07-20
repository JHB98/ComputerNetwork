import random
import zmq
import socket

B = 32  # number of bits of precision in each random integer


def ones_and_zeros(digits):
    """Express `n` in at least `d` binary digits, with no special prefix."""
    return bin(random.getrandbits(digits)).lstrip('0b').zfill(digits)


def bitsource(zcontext, in_url, out_url):
    """Produce random points in the unit square."""
    # Push pull message queue for client-bitsource
    isock = zcontext.socket(zmq.PULL)
    isock.bind(in_url)
    osock = zcontext.socket(zmq.PUB)
    osock.bind(out_url)
    num = int(isock.recv_string())
    while num > 0:
        osock.send_string(ones_and_zeros(B * 2))
        num -= 1


def main(zcontext):
    address = socket.gethostbyname(socket.getfqdn())
    pushpull = 'tcp://'+address+':6703'
    pubsub = 'tcp://'+address+':6700'
    bitsource(zcontext, pushpull, pubsub)


if __name__ == '__main__':
    main(zmq.Context())
