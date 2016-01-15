"""Simple serialization class converting between xml and dict"""

from xml.etree.cElementTree import Element, SubElement
from xml.etree import ElementTree
from xml.dom import minidom
import six

# Message parameters we try to serialize
# This can easily be mocked if needed
REQUIRED_MSG_PARAMS = ['RCV', 'TEXT', 'SND']
OPTIONAL_MSG_PARAMS = ['ID', 'RCPREQ', 'OP', 'CLASS', 'TTL', 'CPATAG',
                       'AGELIMIT', 'SHORTCODE', 'REPLACE', 'DELIVERYTIME']


def serialize(config, messages):
    """Creates an xml representation we send to the server.
    Parameters:
        config: The config module
        messages - an iterable with items containing attributes:
            text: The text message to send (mandatory)
            rcv:  Number of receiver (mandatory)
            id:   id of the message
            snd:  Number of sender to be displayed on receiver's handset
            ... Needs to be extended
    """
    data = {'SESSION': {'CLIENT': None, 'PW': None, 'MSGLST': None}}
    # Pass on auth data
    data['SESSION']['CLIENT'] = config.get('USERNAME')
    data['SESSION']['PW'] = config.get('PASSWORD')

    # Generate message data
    msg_list = []
    for msg in messages:
        # Mandatory params
        entry = {name: msg.get(name) for name in REQUIRED_MSG_PARAMS}
        opt = {name: msg.get(name) for name in OPTIONAL_MSG_PARAMS
               if name in msg}
        entry.update(opt)
        msg_list.append({'MSG': entry})

    data['SESSION']['MSGLST'] = msg_list
    return _dict_to_xml(data)


def deserialize(xml):
    """
    Deserialize xml from the pswin api
    """
    return str(xml)


# --- Utility functions

def _dict_to_xml(data):
    """Converts a dict to xml"""
    if len(data) > 1:
        raise ValueError("Cannot serialize a dict with multiple root nodes")
    if len(data) == 0:
        raise ValueError("dict as no root nodes")
    name, value = six.next(six.iteritems(data))
    root = Element(name)
    _dict_xml_node(value, root)

    rough_string = ElementTree.tostring(root, 'latin-1')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


def _dict_xml_node(data, parent):
    """Traverse the dict data under the root key"""
    if isinstance(data, dict):
        for elem, value in six.iteritems(data):
            sub = SubElement(parent, elem)
            sub.text = _dict_xml_node(value, sub)
    elif isinstance(data, list):
        for entry in data:
            _dict_xml_node(entry, parent)
    else:
        return data


def _xml_to_dict(xml):
    """Converts xml response to a dict"""
    return {}
