"""
Welcome to :mod:`SikuliServer`'s documentation!
==================================================

Library for using Sikuli from Robotframework or other python code

.. toctree::
   :maxdepth: 4

   sikuli_server
   sikuli_client

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
from SikuliServer.sikuli_client import SikuliClient, sikuli_client_session
from SikuliServer.sikuli_client.misc import RemoteLib
from SikuliServer.sikuli_client.exceptions import *
from SikuliServer.sikuli_server import SikuliServer, run_sikuli_server
__author__ = 'Alistair Broomhead'
