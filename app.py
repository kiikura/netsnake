import argparse
import os
import sys
import socket


def netsnake(address, port, cmd, args):

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((address, port))
    server_socket.listen()
    print("netsnake: listening %s:%s" % (address, port))
    conn, address = server_socket.accept()

    server_socket.close()
    os.dup2(conn.fileno(), 0)
    os.dup2(0, 1)
    os.dup2(0, 2)

    os.execl(cmd, os.path.basename(cmd), *args)


def main(argv=sys.argv):
    parser = argparse.ArgumentParser(
        prog="netsnake",
        description="This is socket to stdin/stdout tool.")
    parser.add_argument(
        "--port", "-p",
        type=int,
        default=8888,
        help="listen port"
    )
    parser.add_argument(
        "--listen", "-l",
        metavar="ADDRESS",
        type=str,
        default="localhost",
        help="listen address"
    )
    parser.add_argument(
        "cmd",
        action="store",
        help="absolute command path.")
    parser.add_argument(
        "args",
        nargs="*",
        action="store",
        help="command arguments.")

    args = parser.parse_args()
    netsnake(args.listen, args.port, args.cmd, args.args)


if __name__ == "__main__":
    main()

