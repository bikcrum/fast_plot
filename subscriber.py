import socket

import numpy as np

from topic import Topic

if __name__ == '__main__':
    topic = Topic()

    hostname = socket.gethostname()
    ip_add = socket.gethostbyname_ex(hostname)[2][0]

    client_addr = (ip_add, 8005)
    topic.subscribe(my_address=client_addr)

    while True:
        # Non-blocking read data from client
        data = topic.get_data()

        if data is not None:
            print(np.frombuffer(data, dtype=np.float32))
