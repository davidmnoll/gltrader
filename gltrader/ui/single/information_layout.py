"""
This lists a raw balances response from the API
"""

from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty, ObjectProperty
from kivy.metrics import dp, sp
from kivy.app import App
from kivy.clock import Clock

from ..buttons import NotificationScreenButton, TraderScreenButton


from kivy.uix.label import Label
from pprint import pprint as pp



class InformationLayout(GridLayout):
    """
    Used on Single Market screen to display basic info about Market.  Currently not very developed
    """
    market = ObjectProperty(None)
    height = NumericProperty(dp(50))
    widgets = {}

    def __init__(self, market=None, **kwargs):
        """
        Sets up screen to display and refresh information from market by binding "market" property to refresh method that pulls from market currently assigned to property
        """
        self.bind(minimum_height=self.setter("height"))
        self.bind(height=self.setter("height"))
        self.bind(market=self.refresh)
        self.app= App.get_running_app()
        super(InformationLayout, self).__init__(**kwargs)
        self.refresh()
        self.app.rootWidget.refreshers.append(lambda : self.refresh(market=self.market))


    def refresh(self, obj=None, market=None):
        """
        Accepts market to display and displays or refershes widgets

        :param obj: instance of current object
        :market: the new market set to self.market
        """
        if market is None and self.market is None:
            if "BTC" in self.app.trader.markets:
                self.market = self.app.trader.markets["BTC"]
        else:
            self.market = market
        if self.market is not None and self.market.upToDate:
            if "name" not in self.widgets:
                self.widgets["name"] = Label(text=self.market.name)
                self.add_widget(self.widgets["name"])
            else:
                self.widgets["name"].text = self.market.name
            if "available" not in self.widgets:
                self.widgets["available"] = Label(text=f'{self.market.balance["Available"]:.8f}')
                self.add_widget(self.widgets["available"])
            else:
                self.widgets["available"].text = f'{self.market.balance["Available"]:.8f}'
