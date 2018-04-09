"""
This lists a raw balances response from the API
"""

from kivy.core.window import Window

from kivy.lang import Builder

from kivy.properties import ObjectProperty
from kivy.uix.scrollview import ScrollView
from kivy.effects.opacityscroll import OpacityScrollEffect

from .buttons import NotificationScreenButton



class TraderWindow(ScrollView):
    """
    The layout panel which shows the market table
    """
    market_table = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(TraderWindow, self).__init__(**kwargs, do_scroll_y=True, effect_y=OpacityScrollEffect())
        self.size = (Window.width, Window.height)

class NotificationWindow(ScrollView):
    """
    The layout panel which shows the notifications
    """
    market = ObjectProperty(None)
    notification_layout = ObjectProperty(None)

    def __init__(self, market=None, **kwargs):
        self.market = market
        super(NotificationWindow, self).__init__(**kwargs, do_scroll_y=True, effect_y=OpacityScrollEffect())
        self.size = (Window.width, Window.height)

class HomeWindow(ScrollView):
    """
    The layout panel which shows the info above the notifications on the main screen
    """
    market = ObjectProperty(None)
    info_layout = ObjectProperty(None)

    def __init__(self, market=None,  **kwargs):
        self.market = market
        super(HomeWindow, self).__init__(**kwargs, do_scroll_y=True, effect_y=OpacityScrollEffect())
        self.size = (Window.width, Window.height)

class InformationWindow(ScrollView):
    """
    The layout panel which shows information in the single market screen
    """
    market = ObjectProperty(None)
    info_layout = ObjectProperty(None)

    def __init__(self, market=None,  **kwargs):
        self.market = market
        super(InformationWindow, self).__init__(**kwargs, do_scroll_y=True, effect_y=OpacityScrollEffect())
        self.size = (Window.width, Window.height)

class ActionWindow(ScrollView):
    """
    The layout panel which shows the actions in the Single Market Screen
    """
    market = ObjectProperty(None)
    action_layout = ObjectProperty(None)

    def __init__(self, market=None, **kwargs):
        self.market = market
        super(ActionWindow, self).__init__(**kwargs, do_scroll_y=True, effect_y=OpacityScrollEffect())
