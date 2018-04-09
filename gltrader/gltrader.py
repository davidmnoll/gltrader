"""

This is the Entrypoint which generates the GUI

"""

import os
import kivy
import sys

import threading


from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty

from .trader import Trader
from .ui.screen_management import ScreenManagement
from .notification import Error

# import cProfile
from pprint import pprint as pp
from datetime import datetime


import socket

# import resource

kivy.require('1.10.0')
os.environ['GLTRADER_CONFIG'] = os.path.dirname(os.path.abspath(__file__))+'/../config.json'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('127.0.0.1',80))


class GLTraderApp(App):

    """
    Calls main app
    """

    trader = Trader()
    tick = ObjectProperty()
    rootWidget = ObjectProperty()
    dataThread = None
    uiThread = None
    isTesting = False

    def get_application_config(self):
        """
        Gets config file
        :returns: (String) path to config file
        """
        return os.environ['KIVY_HOME']+'/config.ini'

    def build(self):
        """
        Starts up Application.  Loads GUI from kv file, loads config file, gets markets, and starts tick

        :returns: (kivy.Widget)
        """
        self.rootWidget = Builder.load_file('gltrader/ui/kv/gltrader.kv')
        if not self.trader.config:
            Error("badconfig")
        else:
            self.updateMarkets()
            self.tick = Clock.schedule_interval(self.updateMarkets, self.trader.config["ratelimit"])
        return self.rootWidget

    def updateMarkets(self, dt=None):
        """
        Updates Data, then Updates GUI at each tick
        """
        pp(datetime.now().strftime("%Y%m%d%H%M"))
        self.trader.refreshMarkets()
        self.rootWidget.refresh()

    def test(self):
        """
        Runs 3 ticks of data update only for testing purposees
        """
        self.trader.refreshMarkets()
        Clock.schedule_once(self.trader.refreshMarkets, 5)
        Clock.schedule_once(self.trader.refreshMarkets, 5)
        Clock.schedule_once(self.trader.refreshMarkets, 5)

    def on_stop(self):
        """
        Runs when kivy is quit normally
        """
        self.tick.cancel()

    def on_pause(self):
        """
        Runs on sleep, or when clicking "pause" button
        """
        self.tick.cancel()

    def on_resume(self):
        """
        Runs after waking up, or after clicking "resume" button
        """
        self.tick = Clock.schedule_interval(self.updateMarkets, self.trader.config["ratelimit"])
