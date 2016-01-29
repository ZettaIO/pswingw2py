Contributing
============

Submit bugs and send pull requests on Github. Any kind of contribution is welcome.
if you're unsure or afraid of *anything*, just ask or submit the issue or pull request anyways.

Tests
-----

Make sure you run ``tox`` before submitting code::

    pip install tox

Run ``tox`` from the root of the project where ``tox.ini`` are located.

Run all actions defined in tox.ini::

    tox

Tests are located in the ``tests`` folder using with pytest_.

Vagrant
-------

For Windows and OS X users, Vagrant_ can be useful unless you are developing for your current platform. This also makes sure you don't pollute your system with packages.

.. _Vagrant: https://www.vagrantup.com/
.. _pytest: http://pytest.org/
