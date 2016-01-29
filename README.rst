.. image:: https://travis-ci.org/ZettaIO/pswingw2py.svg?branch=master
    :target: https://travis-ci.org/ZettaIO/pswingw2py

PSWinCom GW2 / LINK SMS GatewayPython Package
=============================================

A Python_ interface to the `PSWinCom XML SMS Gateway`_ now also called the `LINK SMS Gateway`_. Link Mobility bought PSWinCom 31 December 2014.

The official pswinpy_ package has no activity in the last 5 years and only supports a small subset of the api. In January 2016 the default endpoints in the official package are no longer valid. This was the main motivation for creating this library.
This module sends data as XML over HTTPS.

Installation
------------

pip install pswingw2

Basic Usage
-----------

To use this package, you will need sign up for a Gateway account with PSWinCom. Demo account are available.

This piece of code demonstrates how to send a simple SMS message::

    import pswingw2 as sms
    config = sms.config("username", "password") 
    sms.send_simple_message(config, msg_to="4700000000", msg_from="My Company", text="Hello World")

More complex messages can also be sent::

    sms.send(config, data)
    sms.send_single(config, message)
    sms.send_batch(config, message_list)

Send calls also returns a message status structure that can be inspected. Docs needed.

Messages can also be sent using a client class::
    
    client = sms.Client(config)
    
    client.send_simple_message(..)
    client.send(..)
    client.send_single(..)
    client.send_batch(..)

Console Support
---------------

Installing this module also adds a console command for sending messages::

    pswinsms -u username -p password -to 4700000000 -from "My Company" This is a test message

Properties
----------

Receiver, sender and message text are mandatory properties when sending a message. Supported properties can be found in the online
documention under `Element valid for a Submit SMS request`_.

Config Object
-------------

You configure the library by defining a config object that are passed with send calls.

The following attributes must be defined and the config object must be able to obtain them by name using
the get(name) method. This can be a module, dict or class (or whatever structure is suitable for you)::

    ENDPOINTS = ['https://xml.pswin.com', 'https://xml2.pswin.com']
    USERNAME = 'myusername'
    PASSWORD = 'mypassword'

The ``pswingw2.config_defaults`` module have some useful examples.

License
-------
This code is free to use under the terms of the MIT license.

.. _Python: http://www.python.org/
.. _`Online Documentation`: https://wiki.pswin.com/Gateway%20XML%20API.ashx
.. _`PSWinCom XML SMS Gateway`: https://wiki.pswin.com/Gateway%20XML%20API.ashx
.. _pswinpy: https://github.com/PSWinCom/pswinpy
.. _`LINK SMS Gateway`: http://www.linkmobility.com/products/LINK-sms-gateway/
.. _`Element valid for a Submit SMS request`: https://wiki.pswin.com/Gateway%20XML%20API.ashx#Element_valid_for_a_Submit_SMS_request:_0
