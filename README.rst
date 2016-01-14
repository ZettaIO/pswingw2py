PSWinCom GW2 Python Package
===========================

A Python_ interface to the `PPSWinCom XML SMS Gateway`_

The official pswinpy_ package has no activity in the last 5 years and only supports a small subset of the api. In January 2016 the default endpoints in the official package are no longer valid. This was main motivation for creating this library.

Installation
------------

Currently only available through Github. It will be on PyPI when the project is a bit more mature.

Basic Usage
-----------

To use this package, you will need sign up for a Gateway account with PSWinCom. Demo account are available.

This piece of code demonstrates how to send a simple SMS message::

    import pswinpygw2 as sms
    
    config = {
        'PSWIN_ENDPOINTS': ['https://xml.pswin.com', 'https://xml2.pswin.com'],
        'PSWIN_USERNAME': 'myusername',
        'PSWIN_PASSWORD': 'mypassword',
    }
    sms.send_simple_message(config, msg_to="4700000000", msg_from="My Company", text="Hello World")

More complex messages can also be sent::

    sms.send(config, data)
    sms.send_single(config, message)
    sms.send_batch(config, message_list)

Send calls also return a message status that can be inspected. Docs needed.

Properties
----------

Receiver, sender and message text are mandatory properties when sending a message. Supported properties can be found in the `Online Documentation`_.

Config Object
-------------

You configure the library by defining a config object that are passed with send calls.

THe following attributes must be defined and the config object must be able to obtain them by name using
the get(name) method. This can be a module, dict or class (or whatever structure is suitable for you)::

    PSWIN_ENDPOINTS = ['https://xml.pswin.com', 'https://xml2.pswin.com']
    PSWIN_USERNAME = 'myusername'
    PSWIN_PASSWORD = 'mypassword'

License
-------
This code is free to use under the terms of the MIT license.

.. _Python: http://www.python.org/
.. _`Online Documentation`: https://wiki.pswin.com/Gateway%20XML%20API.ashx
.. _`PPSWinCom XML SMS Gateway`: https://wiki.pswin.com/Gateway%20XML%20API.ashx
.. _pswinpy: https://github.com/PSWinCom/pswinpy
