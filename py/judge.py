import zmq
B = 32


def judge(zcontext, in_url, pythagoras_url, out_url):
    isock = zcontext.socket(zmq.SUB)
    isock.connect(in_url)
    for prefix in b'01', b'10', b'11':
        isock.setsockopt(zmq.SUBSCRIBE, prefix)
    psock = zcontext.socket(zmq.REQ)
    psock.connect(pythagoras_url)
    osock = zcontext.socket(zmq.PUSH)
    osock.connect(out_url)
    unit = 2 ** (B * 2)
    while True:
        bits = isock.recv_string()
        n, m = int(bits[::2], 2), int(bits[1::2], 2)
        psock.send_json((n, m))
        sumsquares = psock.recv_json()
        osock.send_string('Y' if sumsquares < unit else 'N')


def main(zcontext):
    pubsub_address = input("Bitsource address : ")
    pushpull_address = input("Tally address : ")
    reqrep_address = input("Pythagoras address : ")
    pubsub = 'tcp://'+pubsub_address+':6700'
    pushpull = 'tcp://'+pushpull_address+':6702'
    reqrep = 'tcp://'+reqrep_address+':6701'
    judge(zcontext, pubsub, reqrep, pushpull)


if __name__ == '__main__':
    main(zmq.Context())
