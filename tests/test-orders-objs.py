import sys
sys.path.append('../')
from unittest import TestCase, skip
from nose.tools import nottest
import os



from pprint import pprint as pp
from kit import dd

import gltrader
from gltrader.action import *
from gltrader.trader import Trader
from gltrader.gltrader import GLTraderApp

os.environ['GLTRADER_CONFIG'] = os.path.dirname(os.path.abspath(__file__))+'/../config.json'


# @skip('ordersobj')
class OrdersObj(TestCase):
    app = GLTraderApp()
    trader = app.trader
    orderNumber = None

    # @nottest
    def test_buy_order(self):
        self.app.isTesting = True
        self.app.test()
        action = MinTradeUp(self.app.trader.markets["ETH"])
        (buy, sell) = action.do()
        complete = action.checkActionComplete()
        pp(complete)
        assert complete
