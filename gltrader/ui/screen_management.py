
import threading

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.app import App

from .windows import TraderWindow, NotificationWindow, InformationWindow, ActionWindow, HomeWindow
from .markets.market_table import MarketTable
from .notifications.notification_layout import NotificationLayout
from .single.information_layout import InformationLayout
from .single.action_layout import ActionLayout
from .notifications.home_layout import HomeLayout

class TraderScreen(Screen):
    """
    The screen widget that contains the Market Table layout
    """
    kv = Builder.load_file('gltrader/ui/kv/traderscreen.kv')


class SingleMarketScreen(Screen):
    """
    The screen widget that contains the Single market screen layout
    """
    kv = Builder.load_file('gltrader/ui/kv/singlemarketscreen.kv')
    info_layout = ObjectProperty()
    action_layout = ObjectProperty()
    notification_layout = ObjectProperty()
    market = ObjectProperty()

    def __init__(self, market=None, **kwargs):
        """
        :param market: (Market) the market to be displayed
        """
        self.market = market
        self.bind(market=self.refresh)
        super(SingleMarketScreen, self).__init__(**kwargs)

    def refresh(self, caller, market):
        self.action_layout.market = market
        self.notification_layout.market = market
        self.info_layout.market = market


class NotificationScreen(Screen):
    """
    The screen widget which contains the main home notificaiton layout
    """
    notification_layout = ObjectProperty()
    kv = Builder.load_file('gltrader/ui/kv/notificationscreen.kv')



class ScreenManagement(ScreenManager):
    """
    The Screen controller. Can be accessed via App.get_running_app().rootWidget (requires import kivy.App)  Contains list of "refresher" functions which are executed each tick to update GUI elements
    """
    nScreen = ObjectProperty()
    tScreen = ObjectProperty()
    smScreen = ObjectProperty()
    refreshers = []

    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)
        app = App.get_running_app()
        app.rootWidget = self

    def refresh(self):
        """
        Calls functions that are in "refreshers" list
        """
        # threads=[]
        # for refresher in self.refreshers:
        #     t = threading.Thread(target=refresher)
        #     threads.append(t)
        #     t.start()
        for refresher in self.refreshers:
            refresher()


    def showNotifications(self):
        """
        Transitions to notifications screen
        """
        if self.current == 'trader':
            self.transition.direction = 'left'
            self.current = 'notifications'
        elif self.current == 'singlemarket':
            self.transition.direction = 'right'
            self.current = 'notifications'

    def showSingleMarket(self, market=None):
        """
        Transitions to single market screen

        :param market: (Market) market to be displayed
        """
        if market is not None:
            self.smScreen.market = market
        if self.current == 'notifications':
            self.transition.direction = 'left'
            self.current = 'singlemarket'
        elif self.current == 'trader':
            self.showNotifications()
            self.showSingleMarket(market)

    def showTrader(self):
        """
        Transitions to market table screen
        """
        if self.current == 'notifications':
            self.transition.direction = 'right'
            self.current = 'trader'
        elif self.current == 'singlemarket':
            self.showNotifications()
            self.showTrader()
