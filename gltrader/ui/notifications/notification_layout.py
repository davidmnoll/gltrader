"""
This lists a raw balances response from the API
"""

from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty, DictProperty
from kivy.metrics import dp, sp
from kivy.app import App

from ..buttons import TraderScreenButton
from .notification_row import NotificationRow

from kivy.uix.label import Label
from pprint import pprint as pp



class NotificationLayout(GridLayout):
    """
    Primary layout for Notifications
    """
    height=NumericProperty(dp(50))
    notifications=DictProperty()
    rowWidgets={}

    def __init__(self, market=None, **kwargs):
        super(NotificationLayout, self).__init__(**kwargs)
        self.bind(minimum_height=self.setter("height"))
        self.bind(height=self.setter("height"))
        self.bind(notifications=self.getRows)
        App.get_running_app().rootWidget.refreshers.append(self.refresh)


    def refresh(self, object=None, newval=None):
        """
        sets self.notifications to a dict of notifcations in the Trader object, which triggers a bind callback to getRows

        :param object: the object if called via "bind" callback
        :param newval: the new value if called via "bind" callback
        """
        self.notifications = App.get_running_app().trader.getNotifications()

    def getRows(self, object=None, value=None):
        """
        Callback when self.notifications is updated -- adds notifications or calls refresh

        :param object: the current object instance
        :param value: the new dict of notifications keyed by their memory address
        """
        for key, val in value.items():
            if key not in self.rowWidgets:
                self.add(val)
            else:
                self.rowWidgets[key].refresh()


    def add(self, note):
        """
        Adds a new notification to the layout

        :param note: (Notification) note to be added to screen
        """
        self.rowWidgets[id(note)] = NotificationRow(note)
        self.add_widget(self.rowWidgets[id(note)])


    def removeRow(self, note):
        """
        Removes a notification from the layout

        :param note: (Notification) notification to be removed
        """
        del(App.get_running_app().trader.notifications[id(note)])
        self.remove_widget(self.rowWidgets[id(note)])
        del(self.rowWidgets[id(note)])
