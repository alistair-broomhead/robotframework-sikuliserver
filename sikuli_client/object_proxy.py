""" Interfaces for interacting with serverside objects """
__author__ = 'Alistair Broomhead'

from weakref import proxy

# Only used for docstrings, doesn't need to me imported
try:
    from SikuliServer.sikuli_client import SikuliClient
except ImportError:
    SikuliClient = None


class ObjectProxyMap(object):
    """ Used by ObjectProxy objects to interact with the server """

    def __init__(self, sikuli_client):
        """
        :type sikuli_client: SikuliClient
        """
        self.client = proxy(sikuli_client)
        self._objects = {}

    def __getitem__(self, item):
        """
        :type item: int
        """
        return self._objects[item]

    def __del__(self):
        for k in self._objects:
            del self._objects[k]


class ObjectProxy(object):
    """ Proxies a server-side object """

    def __init__(self, proxy_map, id_, obj):
        """
        :type proxy_map: ObjectProxyMap
        """
        self.mapper = proxy(proxy_map)
        self.client = proxy(proxy_map.client)
        self.obj = proxy(obj)

        self.active = True
        self.id_ = id_
        self.refs = 0
        self.up_ref()

    def _gc(self):
        if self.id_ not in self.client._sikuliserver.held_objects():
            self.active = False
            del self.mapper._objects[self.id_]
            if self.refs > 0:
                raise NameError("%r has been garbage collected on the server "
                                "side, should have had %r references left" %
                                (self, self.refs))


    def up_ref(self, times=1):
        """
        Ups the number of references by times
        :param times: int
        """
        self.refs += times
        self.client._sikuliserver.jython_object_addrefs(self.id_, times)
        self._gc()

    def de_ref(self, times=1):
        """
        Decreases the number of references by times
        :param times: int
        """
        self.up_ref(-times)

    def __del__(self):
        self.de_ref(self.refs)
