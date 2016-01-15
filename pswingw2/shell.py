"""
Handles the shell entry point
"""
import argparse
import sys
from pswingw2.config_defaults import get_simple_config
from pswingw2 import send_simple_message


def parse(args):
    """Parse arguments"""
    parser = argparse.ArgumentParser(description="Sending SMS using PSWin Gateway")
    parser.add_argument('-u', dest="username", metavar="username",
                        help="Username", required=True)
    parser.add_argument('-p', dest="password", metavar="password",
                        help="Password", required=True)
    parser.add_argument('-to', dest="msg_to", metavar="msg_to",
                        help="The destinaion mobile number", required=True)
    parser.add_argument('-from', dest="msg_from", metavar="msg_from",
                        help="Name or mobile numer of the sender", required=True)
    parser.add_argument('message', metavar="message",
                        help="Message", nargs="+")

    data = parser.parse_args(args)
    message = " ".join(data.message)
    return (data.username, data.password, data.msg_to, data.msg_from, message)


def send(config, msg_to, msg_from, message):
    """Send message"""
    send_simple_message(config, msg_to=msg_to, msg_from=msg_from, text=message)


def main(argv=sys.argv[1:]):
    """Entry point for console"""
    username, password, msg_to, msg_from, message = parse(argv)
    config = get_simple_config(username, password)
    send(config, msg_to, msg_from, message)
