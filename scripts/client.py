from socket import *

from logger import Logger


class Client(socket):
    def __init__(self, ip: str, port: int):
        super().__init__()
        self.logger = Logger("Client")

        self.ip = ip
        self.port = port
        self.is_connected = False

        self.logger.log("Client is setup")

    def connect(self):
        self.connect((self.ip, self.port))
        logger.log("Connected to {self.ip}:{self.port}")

    def __repr__(self):
        if self.is_connected:
            return f"Client connected to {self.ip}:{self.port}"
        else:
            return f"Client connecting to {self.ip}:{self.port}"

