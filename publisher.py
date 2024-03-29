import socket

import numpy as np

from topic import Topic

if __name__ == '__main__':
    topic = Topic()

    hostname = socket.gethostname()
    ip_add = socket.gethostbyname_ex(hostname)[2][0]

    server_addr = (ip_add, 8004)
    client_addr = (ip_add, 8005)

    topic.subscribe(my_address=server_addr)

    while True:
        # Main thread
        data = np.random.randn(10).astype(np.float32)

        # Non-blocking data publish to client
        topic.publish(data.tobytes(), other_address=client_addr)
