import zmq


def always_yes(zcontext, in_url, out_url):
    isock = zcontext.socket(zmq.SUB)
    isock.connect(in_url)
    isock.setsockopt(zmq.SUBSCRIBE, b'00')
    osock = zcontext.socket(zmq.PUSH)
    osock.connect(out_url)
    while True:
        isock.recv_string()
        osock.send_string('Y')


def main(zcontext):
    pubsub_address = input("Bitsource address : ")
    pushpull_address = input("Tally address : ")
    pubsub = 'tcp://'+pubsub_address+':6700'
    pushpull = 'tcp://'+pushpull_address+':6702'

    always_yes(zcontext, pubsub, pushpull)


if __name__ == '__main__':
    main(zmq.Context())
