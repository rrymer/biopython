# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 22:19:42 2014

@author: Richard Rymer

draft code for mocked tests of the TogoWS webserver.
"""

import mock
import urllib
import pdb

URL = "http://togows.dbcls.jp"

def test():
    handle = urllib.urlopen(URL)
    fields = handle.read().strip().split()
    print fields

mock = mock.Mock()
mock.wraps(test)

pdb.set_trace()
test()