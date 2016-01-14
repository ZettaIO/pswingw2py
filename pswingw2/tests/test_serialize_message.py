"""
Test message serialization
"""
import pytest
from pswingw2.serialization import serialize, deserialize

@pytest.fixture
def config():
    return {'PSWIN_USERNAME': 'username',
            'PSWIN_PASSWORD': 'password',
            'PSWIN_ENDPOINTS': ['https://xml.pswin.com', 'https://xml2.pswin.com']}

@pytest.fixture
def single_message():
    return [{'RCV': '4700000000', 'TEXT': "This is a test message", 'SND': 'My Company'}]


def test_message_serialize(config, single_message):
    """Test message serialization"""
    xml = serialize(config, single_message)
    data = deserialize(xml)
