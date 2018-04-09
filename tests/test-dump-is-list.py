import sys
sys.path.append('../')
from unittest import TestCase
from nose.tools import nottest



import json

import gltrader
from gltrader.trader import Trader
from pprint import pprint as pp
from kit import dd

@nottest
def test_dump_is_list():
    trader = Trader()
    result = trader.dumplist()

    if type(result) is list:
        assert True
    else:
        assert False
