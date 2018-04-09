"""
This lists a raw balances response from the API
"""

import threading

from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.properties import ObjectProperty, NumericProperty, DictProperty
from kivy.metrics import dp, sp
from kivy.app import App
from functools import partial
from kivy.core.window import Window


from .market_table_header import MarketTableHeader
from .market_row import MarketRow

from pprint import pprint as pp


class MarketTable(GridLayout):
    """
    The primary GUI layout for the market table which contains the rows for each market.  Contains dict marketWidgets, which is used to refresh values
    """
    height=NumericProperty(dp(50))
    marketWidgets=DictProperty(None)

    def __init__(self, **kwargs):
        """
        Binds object values to methods to be called when updated, adds refresh to app.rootWidget.refreshers so it will be called each tick
        """
        self.bind(minimum_height=self.setter("height"))
        self.bind(height=self.setter("height"))
        super(MarketTable, self).__init__(**kwargs)
        self.bind(marketWidgets=self.refresh)
        self.app=App.get_running_app()
        self.refresh()
        self.app.rootWidget.refreshers.append(self.refresh)


    def refresh(self, object=None, value=None):
        """
        called when marketWidgets changes value to update table

        :param object: instance of current object
        :param value: new value of marketWidgets
        """
        self.showMarkets()

    def removeMarket(self, market):
        """
        Removes a given market from the table --- called when market.isMonitored is set to false
        :param market: (Market) market to be removed from table
        """
        if market.name in self.marketWidgets:
            self.remove_widget(self.marketWidgets[market.name])
            del(self.marketWidgets[market.name])

    def addMarket(self, name, market):
        """
        Adds a given market to the table --- called when market.isMonitored is set to true
        :param market: (Market) market to be added to table
        """
        self.marketWidgets[name] = MarketRow(market)
        self.add_widget(self.marketWidgets[name])
        self.marketWidgets[name].refresh()

    def showMarkets(self):
        """
        Creates market rows or refreshes them (in separate threads).  
        """
        threads = []
        for name, market in self.app.trader.markets.items():
            if market.upToDate and market.isMonitored:
                if name in self.marketWidgets:
                    t = threading.Thread(target=self.marketWidgets[name].refresh)
                    threads.append(t)
                    t.start()
                    # self.marketWidgets[name].refresh()
                else:
                    self.addMarket(name, market)
            else:
                self.removeMarket(market)
        self.setter("height")
