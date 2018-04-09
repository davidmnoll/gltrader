import sys
sys.path.append('../')
from unittest import TestCase, skip
from nose.tools import nottest


import gltrader
from gltrader.trader import Trader
from pprint import pprint as pp
from kit import dd


@skip('openorders')
def test_open_orders():
    trader = Trader()
    response = trader.api.get_open_orders("BTC-BCC")
    pp(response)
    assert response["success"] and False
