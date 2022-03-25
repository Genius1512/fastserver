from socket import *

from logger import Logger


class Server(socket):
    def __init__(self, ip: str, port: int):
        super().__init__()
        self.logger = Logger("Server")

        self.ip = ip
        self.port = port

        self.bind((self.ip, self.port))

        self.logger.log("Server is setup")

    def get_connection(self):
        pass

    def close(self):
        logger.log("Server closed")
        super().close()

    def __repr__(self):
        return f"Server on {self.ip}:{self.port}"

