from arg_parse import parse_args
from client import Client
from exceptions import *
from logger import Logger
from server import Server


# globals
logger = Logger("Core")


def main():
    args = parse_args()

    if args.mode == "server":
        server = Server(args.ip, args.port)

    else:
        client = Client(args.ip, args.port)


if __name__ == "__main__":
    main()

