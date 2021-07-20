import zmq
import socket
import matplotlib.pyplot as plt


def client(zcontext, in_url, out_url):
    # Push pull message queue for client-tally
    isock = zcontext.socket(zmq.PULL)
    isock.bind(in_url)
    # Push pull message queue for client-bitsource
    osock = zcontext.socket(zmq.PUSH)
    osock.connect(out_url)
    try:
        num = int(input("num : "))
        if num <= 0:
            raise Exception('You should input over 0.')  # if you input under 0
        osock.send_string(str(num))  # send num to bitsource
        while num > 0:  # iterate 'num' times
            ans = isock.recv_string()  # receive number of iterations and pi value from tally
            print(ans)
            x = ans.split()[0]  # number of iterations
            y = ans.split()[1]  # pi value
            plt.scatter(int(x), float(y), 10, 'k')  # plots the change in graph
            plt.pause(0.0001)
            num -= 1
        plt.show()  # show graph
    except Exception as e:
        print(e)


def main(zcontext):
    in_address = socket.gethostbyname(socket.getfqdn())
    out_address = input("Bitsource address : ")
    in_pushpull = 'tcp://'+in_address+':6704'
    out_pushpull = 'tcp://'+out_address+':6703'

    client(zcontext, in_pushpull, out_pushpull)


if __name__ == '__main__':
    main(zmq.Context())
