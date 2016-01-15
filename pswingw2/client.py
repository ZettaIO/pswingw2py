"""Simple functions for sending sms"""

import requests
from requests.exceptions import HTTPError, ConnectionError
from pswingw2.serialization import serialize


def send_simple_message(config, msg_to=None, msg_from=None, text=None):
    """Sends a single sms.
    Parameters:
        config:   config object
        msg_to:   The number to send the message to
        msg_from: The number or name of the sender
        text:     Characters send in the message
    """
    if not all([msg_to, msg_from, text]):
        raise ValueError("Missing parameter. Mandatory: msg_to, msg_from, text")

    msg = {'RCV': msg_to, 'TEXT': text, 'SND': msg_from}
    return send_single(config, msg)


def send(config, data):
    """Generic send method taking a single msssage or a list"""
    if isinstance(data, list):
        return send_batch(config, data)
    return send_single(config, data)


def send_single(config, message):
    """Sends a single sms"""
    if isinstance(message, list):
        raise ValueError("Attempts to send batch as single message")
    return send_batch(config, [message])


def send_batch(config, messages):
    """Sends multiple sms in a batch"""
    xml = serialize(config, messages)
    headers = {"Content-Type": "text/xml", "Content-Length": len(xml)}
    return _post_request(config, xml, headers)


def _post_request(config, data, headers):
    """Attempts to do a post request on all endpoints"""
    if not config:
        raise ValueError("Config object not supplied")
    resp = None
    for endpoint in config.get("ENDPOINTS"):
        try:
            resp = requests.post(endpoint, data=data, headers=headers)
            if resp.status_code == 200:
                return resp.text
        except HTTPError:
            print("HTTPError while sending sms with endpoint {}".format(endpoint))
        except ConnectionError:
            print("ConnectionError: {}".format(endpoint))

    raise HTTPError("All endpoints failed")


class Client(object):
    """Client class holding config object.
    It can be practical in some cases"""

    def __init__(self, config):
        self.config = config

    def send_simple_message(self, msg_to, msg_from, text):
        """Sends a single sms.
        Parameters:
            config:   config object
            msg_to:   The number to send the message to
            msg_from: The number or name of the sender
            text:     Characters send in the message
        """
        send_simple_message(self.config, msg_to, msg_from, text)

    def send(self, data):
        """Generic send method taking a single msssage or a list"""
        send(self.config, data)

    def send_single(self, message):
        """Sends a single sms"""
        send_single(self.config, message)

    def send_batch(self, messages):
        """Sends multiple sms in a batch"""
        send_batch(self.config, messages)
