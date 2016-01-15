"""
Example config module.

You can use this module for your own config object, but remember
that this is a singleton. There can only be one single config.
Simply mock the values and import them.

Make your own config definition for each account used. This can be
any structure that can support a get(NAME) function. A module like
this, a dict or a class should be straight forward.

Note that all config values are mandatory. The API will crash otherwise.

--- Config Values ---
These are mandatory attributes for the config object

ENDPOINTS:
  A list of endpoints for the service. If the request to the first
  endpoint fails due to some http error, we continue down the list.

USERNAME
  Your pswin username

PASSWORD
  Your pswin password
 """

# --- Default ---
# Fallback endpoints if they are not specified.
# You should ideally always define them.
DEFAULT_ENDPOINTS = ['https://xml.pswin.com', 'https://xml2.pswin.com']

# --- Config as a package ---
ENDPOINTS = DEFAULT_ENDPOINTS
USERNAME = 'myusername'
PASSWORD = 'mypassword'


def get(name):
    """Make the config values accessible through get()"""
    return globals().get(name)

# --- Config as dictionary ---
CONFIG = {
    'ENDPOINTS': DEFAULT_ENDPOINTS,
    'USERNAME': 'myusername',
    'PASSWORD': 'mypassword',
}


# --- Config as class ---
class Config(object):
    """This is just used as a namespace to store values"""
    PSWIN_ENDPOINTS = DEFAULT_ENDPOINTS,
    PSWIN_USERNAME = 'myusernamec'
    PSWIN_PASSWORD = 'mypasswordc'

    @classmethod
    def get(cls, name):
        """We create a custom get() class method
        to support then get() interface"""
        return getattr(cls, name)


# --- Shortcut for getting simple config
def get_simple_config(username, password):
    """Creates a config object using default endpoints"""
    return {
        'ENDPOINTS': DEFAULT_ENDPOINTS,
        'USERNAME': username,
        'PASSWORD': password,
    }
