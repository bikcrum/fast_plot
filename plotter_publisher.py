import json
import socket

import numpy as np

from topic import Topic

if __name__ == '__main__':
    topic = Topic()

    hostname = socket.gethostname()
    ip_add = socket.gethostbyname_ex(hostname)[2][0]

    main_thread_addr = (ip_add, 8004)
    plotter_addr = (ip_add, 8005)

    topic.subscribe(my_address=main_thread_addr)

    while True:
        # Main thread
        data = np.random.randn(10)

        # Non-blocking call to plotter
        topic.publish(json.dumps({'line_plot': data.tolist()}), other_address=plotter_addr)
