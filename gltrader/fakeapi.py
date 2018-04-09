

BUY_ORDERBOOK = 'buy'
SELL_ORDERBOOK = 'sell'
BOTH_ORDERBOOK = 'both'

TICKINTERVAL_ONEMIN = 'oneMin'
TICKINTERVAL_FIVEMIN = 'fiveMin'
TICKINTERVAL_HOUR = 'hour'
TICKINTERVAL_THIRTYMIN = 'thirtyMin'
TICKINTERVAL_DAY = 'Day'

ORDERTYPE_LIMIT = 'LIMIT'
ORDERTYPE_MARKET = 'MARKET'

TIMEINEFFECT_GOOD_TIL_CANCELLED = 'GOOD_TIL_CANCELLED'
TIMEINEFFECT_IMMEDIATE_OR_CANCEL = 'IMMEDIATE_OR_CANCEL'
TIMEINEFFECT_FILL_OR_KILL = 'FILL_OR_KILL'

CONDITIONTYPE_NONE = 'NONE'
CONDITIONTYPE_GREATER_THAN = 'GREATER_THAN'
CONDITIONTYPE_LESS_THAN = 'LESS_THAN'
CONDITIONTYPE_STOP_LOSS_FIXED = 'STOP_LOSS_FIXED'
CONDITIONTYPE_STOP_LOSS_PERCENTAGE = 'STOP_LOSS_PERCENTAGE'

API_V1_1 = 'v1.1'
API_V2_0 = 'v2.0'


PROTECTION_PUB = 'pub'  # public methods
PROTECTION_PRV = 'prv'  # authenticated methods

class FakeAPI(object):
    """
    Class used to mock responses from  API.  Can be called with "App.get_running_app().Trader.fapi" in most places
    """

    def __init__(self):
        pass


    def get_markets(self):

        return {'success': True,
             'message': '',
             'result': [ {'MarketCurrency': 'LTC',
                          'BaseCurrency': 'BTC',
                          'MarketCurrencyLong': 'Litecoin',
                          'BaseCurrencyLong': 'Bitcoin',
                          'MinTradeSize': 1e-08,
                          'MarketName': 'BTC-LTC',
                          'IsActive': True,
                          'Created': '2014-02-13T00:00:00',
                          'Notice': None,
                          'IsSponsored': None,
                          'LogoUrl': 'https://i.imgur.com/R29q3dD.png'},
                          ...
                        ]
            }

    def get_currencies(self):
        docstring
        pass

    def get_ticker(self, market):
        pass

    def get_market_summaries(self):
        pass

    def get_marketsummary(self, market):
        pass

    def get_orderbook(self, market, depth_type=BOTH_ORDERBOOK):
        pass

    def get_market_history(self, market):
        return {'success': True,
            'message': '',
            'result': [ {'Id': 5625015,
                         'TimeStamp': '2017-08-31T01:29:50.427',
                         'Quantity': 7.31008193,
                         'Price': 0.00177639,
                         'Total': 0.01298555,
                         'FillType': 'FILL',
                         'OrderType': 'BUY'},
                         ...
                       ]
            }

    def buy_limit(self, market, quantity, rate):

        return {
        	"success" : False,
        	"message" : "",
        	"result" : {
        			"uuid" : "98347-5q908457nx908457-qx23904857"
        		}
        }

    def sell_limit(self, market, quantity, rate):
        return {
        	"success" : False,
        	"message" : "",
        	"result" : {
        			"uuid" : "98347-5q908457nx908457-qx23904857"
        		}
        }

    def cancel(self, uuid):
        return {
            "success" : True,
            "message" : "",
            "result" : None
        }

    def get_open_orders(self, market=None):

        return {'message': '',
             'result': [{'CancelInitiated': False,
                 'Closed': None,
                 'CommissionPaid': 0.0,
                 'Condition': 'NONE',
                 'ConditionTarget': None,
                 'Exchange': market,
                 'Id': 5957856521,
                 'ImmediateOrCancel': False,
                 'IsConditional': False,
                 'IsOpen': True,
                 'Limit': 0.000001,
                 'Opened': '2018-03-02T21:50:16.95',
                 'OrderType': 'LIMIT_SELL',
                 'OrderUuid': '98347-5q908457nx908457-qx23904857',
                 'Price': 0.0,
                 'PricePerUnit': None,
                 'Quantity': 3.0,
                 'QuantityRemaining': 3.0,
                 'Updated': '2018-03-02T21:50:16.9526301',
                 'Uuid': '98347-5q908457nx908457-qx23904857'}],
             'success': True}

    def get_balances(self):
        pass

    def get_balance(self, currency):
        pass

    def get_deposit_address(self, currency):
        pass

    def withdraw(self, currency, quantity, address):
        pass

    def get_order_history(self, market=None):
        pass

    def get_order(self, uuid):
        return {
        	"success" : True,
        	"message" : "",
        	"result" : {
        		"AccountId" : None,
        		"OrderUuid" : uuid,
        		"Exchange" : "BTC-SHLD",
        		"Type" : "LIMIT_BUY",
        		"Quantity" : 3,
        		"QuantityRemaining" : 3,
        		"Limit" : 0.000001,
        		"Reserved" : 0.00001000,
        		"ReserveRemaining" : 0.00001000,
        		"CommissionReserved" : 0.00000002,
        		"CommissionReserveRemaining" : 0.00000002,
        		"CommissionPaid" : 0.00000000,
        		"Price" : 0.00000000,
        		"PricePerUnit" : None,
        		"Opened" : "2014-07-13T07:45:46.27",
        		"Closed" : None,
        		"IsOpen" : False,
        		"Sentinel" : "6c454604-22e2-4fb4-892e-179eede20972",
        		"CancelInitiated" : False,
        		"ImmediateOrCancel" : False,
        		"IsConditional" : False,
        		"Condition" : "NONE",
        		"ConditionTarget" : False
        	}
        }

    def get_withdrawal_history(self, currency=None):
        pass

    def get_deposit_history(self, currency=None):
        pass

    def list_markets_by_currency(self, currency):
        pass

    def get_wallet_health(self):
        pass

    def get_balance_distribution(self):
        pass

    def get_pending_withdrawals(self, currency=None):
        pass

    def get_pending_deposits(self, currency=None):
        pass

    def generate_deposit_address(self, currency):
        pass

    def trade_sell(self, market=None, order_type=None, quantity=None, rate=None, time_in_effect=None,
                   condition_type=None, target=0.0):
        return {
            "success" : True,
            "message" : "",
            "result" : {
                "BuyOrSell": "Sell",
                "MarketCurrency": market,
                "MarketName": market,
                "OrderId": "98347-5q908457nx908457-qx23904857",
                "OrderType": "LIMIT",
                "Quantity": quantity,
                "Rate": 0.00002
            }
        }

    def trade_buy(self, market=None, order_type=None, quantity=None, rate=None, time_in_effect=None,
                  condition_type=None, target=0.0):
        return {
            "success" : True,
            "message" : "",
            "result" : {
                "BuyOrSell": "Buy",
                "MarketCurrency": "DGB",
                "MarketName": market,
                "OrderId": "98347-5q908457nx908457-qx23904857",
                "OrderType": "LIMIT",
                "Quantity": quantity,
                "Rate": 0.00001
            }
        }

    def get_candles(self, market, tick_interval):
        return { "success": True,
              "message": '',
              "result":
               [ { "O": 421.20630125,
                   "H": 424.03951276,
                   "L": 421.20630125,
                   "C": 421.20630125,
                   "V": 0.05187504,
                   "T": '2016-04-08T00:00:00',
                   "BV": 21.87921187 },
                 { "O": 420.206,
                   "H": 420.206,
                   "L": 416.78743422,
                   "C": 416.78743422,
                   "V": 2.42281573,
                   "T": '2016-04-09T00:00:00',
                   "BV": 1012.63286332 }]
            }
