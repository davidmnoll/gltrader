import sys
sys.path.append('../')
from unittest import TestCase
from nose.tools import nottest


import gltrader
from gltrader.trader import Trader
from pprint import pprint as pp
from kit import dd

@nottest
def test_api_connected():
    trader = Trader()
    response = trader.dump()
    # pp(response)
    if response["success"]:
        assert True
    else:
        assert False
