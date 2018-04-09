import sys
sys.path.append('../')
from unittest import TestCase, skip
from nose.tools import nottest


import gltrader
from gltrader.trader import Trader
from pprint import pprint as pp
from kit import dd

@skip('tradeapi')
class OrdersAPISuite(TestCase):
    trader = Trader()
    orderNumber = None

    # @nottest
    def test_buy_order(self):
        response = self.trader.api.trade_buy(
            market="BTC-ETH",
            order_type="LIMIT",
            quantity=5,
            rate=.0001,
            time_in_effect="GOOD_TIL_CANCELLED"
        )
        pp(response)
        assert (response["success"])

    # @nottest
    def test_sell_order(self):
        response = self.trader.api.trade_sell(
            market="BTC-ANT",
            order_type="LIMIT",
            quantity=3,
            rate=.1,
            time_in_effect="GOOD_TIL_CANCELLED"
        )
        pp(response)
        assert response["success"]

    # @nottest
    def test_cancel_orders(self):
        trader = Trader()
        cancel = True
        response = trader.api.get_open_orders()
        if (response["success"]):
            for order in response["result"]:
                status = trader.api.cancel(order["OrderUuid"])
                cancel = cancel and status["success"]
                pp(order["OrderUuid"])
                pp(status)
        pp(response)
        assert cancel and False
