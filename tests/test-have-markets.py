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
def test_have_markets():
    trader = Trader()
    result = trader.getData()
    # pp(result)
    if type(result) is list:
        assert True
    else:
        assert False
