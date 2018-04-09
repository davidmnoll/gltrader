"""
This lists a raw balances response from the API
"""

from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty
from kivy.metrics import dp, sp
from kivy.app import App

from ..buttons import TraderScreenButton, NotificationScreenButton

from pprint import pprint as pp



class ActionLayout(GridLayout):
    """
    Currently not Developed -- To be used on Single Market Screen to allow manual trigger of actions
    """
    height=NumericProperty(dp(50))

    def __init__(self, **kwargs):
        self.bind(minimum_height=self.setter("height"))
        self.bind(height=self.setter("height"))
        super(ActionLayout, self).__init__(**kwargs)
        self.app= App.get_running_app()
        self.add_widget(NotificationScreenButton())
