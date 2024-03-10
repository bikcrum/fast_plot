import json
import socket
from multiprocessing import Manager, Process


class Topic:
    @staticmethod
    def _fetch(data, soc, packet_size=4096):

        while True:
            inc = soc.recvfrom(packet_size)

            if inc is not None:
                msg, addr = inc

                data['msg'] = msg

    def subscribe(self, my_address):
        self.soc = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.soc.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1)

        self.soc.bind(my_address)

        self.inc_data = Manager().dict()

        remote_func = Process(target=self._fetch, args=(self.inc_data, self.soc))
        remote_func.start()

    def publish(self, data, other_address):
        assert type(data) == str, "data must be a string"
        data = str.encode(data)
        self.soc.sendto(data, other_address)

    def get_data(self):
        data = self.inc_data.get('msg', None)
        if data is not None:
            return json.loads(data)
        return data

    def __del__(self):
        if self.soc is not None:
            self.soc.close()
