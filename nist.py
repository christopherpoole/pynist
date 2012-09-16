from httplib2 import Http
from urllib import urlencode
from pprint import pprint

import numpy
import yaml

from lxml import etree


schema = yaml.load(file("schema.yaml"))

class NistData(object):
    def __init__(self, **kwargs):
        self.config = schema[self.__class__.__name__].copy()
        self.postdata = self.config["postdata"]
    
        # post data user overrides
        for key, val in self.postdata.iteritems():
            if not isinstance(val, dict):
                continue
            
            v = val.values()[0]
            if kwargs[val.keys()[0]] is not None:
                v = kwargs[val.keys()[0]]
                self.postdata[key] = v
            
            setattr(self, val.keys()[0], v)

       http = Http()
       self._response, self._content = http.request(self.config["url"], "POST",
                                                    urlencode(self.postdata))

        self.tree = etree.HTML(self._content)
        self.rows = list(self.tree.iter("tr"))
        self.data = [[r.text for r in row] for row in self.rows[self.config["head_offset"]:]]

        self.name = self.tree.iter("h2").next().text

        for i, p in enumerate(self.config["properties"]):
            name = p.keys()[0]
            try:
                units = p.values()[0]["units"]
            except (KeyError, TypeError):
                dtype = self.config["defaults"]["units"]

            try:
                dtype = p.values()[0]["dtype"]
            except (KeyError, TypeError):
                dtype = self.config["defaults"]["dtype"]

            setattr(self, name,
                    Property(name, units, [d[i] for d in self.data], dtype=dtype))


class Property:
    def __init__(self, name, units, data, dtype=float):
        self.name = name
        self.units = units
        self.data = data
        
        if dtype != 'None':
            self.data = numpy.array(self.data, dtype=numpy.dtype(dtype))

    def __repr__(self):
        return self.data.__repr__()

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, key):
        return self.data[key]


class PhotonCrossSection(NistData):
    def __init__(self, symbol=None, atomic_number=None):
        super(PhotonCrossSection, self).__init__(atomic_number=atomic_number,
                                                 min_energy=None, max_energy=None)

