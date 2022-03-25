import constants

from argparse import ArgumentParser, ArgumentTypeError


def mode(arg: str) -> str:
    return arg.lower()


def parse_args():
    parser = ArgumentParser(description="Argument Parser")

    parser.add_argument(
        "mode",
        type=mode,
        choices=["server", "client"],
        help="Server or client"
    )

    parser.add_argument(
        "--ip",
        default="0.0.0.0",
        help="IP"
    )

    parser.add_argument(
        "-p", "--port",
        default=1512,
        help="Port"
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = vars(parse_args())
    for key in args:
        print(f"{key}: {args[key]}")

