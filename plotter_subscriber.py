import socket

from matplotlib import pyplot as plt

from topic import Topic

if __name__ == '__main__':
    topic = Topic()

    hostname = socket.gethostname()
    ip_add = socket.gethostbyname_ex(hostname)[2][0]

    main_thread_addr = (ip_add, 8004)
    plotter_addr = (ip_add, 8005)

    topic.subscribe(my_address=plotter_addr)

    while True:
        data = topic.get_data()

        if data is not None:
            # Plotter thread. Does not block main thread
            if data is not None:
                plt.cla()
                plt.plot(data['line_plot'])
                plt.pause(0.0001)
