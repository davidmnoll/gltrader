from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty, ObjectProperty
from kivy.metrics import dp, sp
from kivy.app import App
from kivy.clock import Clock

from ..buttons import NotificationScreenButton, TraderScreenButton, PauseButton, ClearAllNotificationsButton
from ..markets.market_number_label import MarketNumberLabel

from kivy.uix.label import Label
from pprint import pprint as pp
# import resource


class HomeLayout(GridLayout):
    """
    GUI element that displays balance and control buttons at top of notifications menu
    """
    market = ObjectProperty(None)
    height = NumericProperty(dp(50))
    widgets = {}

    def __init__(self, **kwargs):
        """
        Binds height and adds self to "refreshers" to keep elements up to date
        """
        self.bind(minimum_height=self.setter("height"))
        self.bind(height=self.setter("height"))
        self.app= App.get_running_app()
        super(HomeLayout, self).__init__(**kwargs)
        self.app.rootWidget.refreshers.append(self.refresh)

    def refresh(self):
        """
        Adds widgets for BTC balance and buttons for switching to the market table, pausing, or clearing all notifications
        """
        BTCmarket = self.app.trader.markets["BTC"]
        if "name" not in self.widgets:
            self.widgets["name"] = Label(text=BTCmarket.name)
            self.add_widget(self.widgets["name"])
        if "available" not in self.widgets:
            self.widgets["available"] = MarketNumberLabel(lambda: BTCmarket.balance["Available"])
            self.add_widget(self.widgets["available"])
            self.app.rootWidget.refreshers.append(self.widgets["available"].refresh)
        # if "memory" not in self.widgets:
        #     memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1000000
        #     self.widgets["memory"] = Label(text=str(memory))
        #     self.add_widget(self.widgets["memory"])
        # else:
        #     memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1000000
        #     self.widgets["memory"].text=str(memory)


        if "gototrader" not in self.widgets:
            self.widgets["gototrader"] = TraderScreenButton()
            self.add_widget(self.widgets["gototrader"])

        if "pause" not in self.widgets:
            self.widgets["pause"] = PauseButton()
            self.add_widget(self.widgets["pause"])

        if "clearall" not in self.widgets:
            self.widgets["clearall"] = ClearAllNotificationsButton()
            self.add_widget(self.widgets["clearall"])
