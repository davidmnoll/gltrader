
from kivy.app import App
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

from ..notification import *

class ViewButton(Button):
    """
    Goes to single market screen from row on trader screen
    """
    market=ObjectProperty()

    def __init__(self, market, **kwargs):
        """
        :param market: (Market) The market to view
        """
        self.market = market
        super(ViewButton, self).__init__(**kwargs, text="View")
        self.background_color = [.5,.7,.5,1]

    def refresh(self):
        pass

    def on_release(self):
        app = App.get_running_app()
        app.root.showSingleMarket(self.market)

class NotificationScreenButton(Button):
    """
    Goes to the Notifications/main screen
    """
    def __init__(self, **kwargs):
        super(NotificationScreenButton, self).__init__(**kwargs, text="Home Screen")
        self.background_color = [.5,.5,.7,1]

    def refresh(self):
        pass

    def on_release(self):
        app = App.get_running_app()
        app.root.showNotifications()

class TraderScreenButton(Button):
    """
    Goes to the market table screen
    """
    def __init__(self, **kwargs):
        super(TraderScreenButton, self).__init__(**kwargs, text="Market Table Screen")
        self.background_color = [.5,.5,.7,1]

    def refresh(self):
        pass

    def on_release(self):
        app = App.get_running_app()
        app.root.showTrader()


class StartButton(Button):
    """
    Not Currently implemented-- If market is not monitored, start monitoring
    """

    def __init__(self, market, **kwargs):
        super(StartButton, self).__init__(**kwargs, text="Start")

    def refresh(self):
        pass

class SingleMarketButton(Button):
    """
    Same functionaility as ViewButton, but Display label is different
    """
    market=ObjectProperty()

    def __init__(self, market, **kwargs):
        self.market = market
        super(SingleMarketButton, self).__init__(**kwargs, text=market.name)
        self.background_color = [.5,.7,.5,1]

    def refresh(self):
        pass

    def on_release(self):
        app = App.get_running_app()
        app.root.showSingleMarket(self.market)

class RemoveNotificationButton(Button):
    """
    Removes notification row from Notifications Layout
    """

    def __init__(self, notification, **kwargs):
        super(RemoveNotificationButton, self).__init__(text="X", width=30, size_hint_x=None)
        self.background_color = [1,.7,.7,1]
        self.color = [0,0,0,1]
        self.width = 30
        self.notification = notification


    def refresh(self):
        pass

    def on_release(self):
        self.parent.parent.removeRow(self.notification)

class PauseButton(Button):
    """
    Pauses ticks on Trader or resumes if already paused
    """
    paused = False

    def __init__(self, **kwargs):
        super(PauseButton, self).__init__(**kwargs, text="Pause")
        self.background_color = [.7,.7,.7,1]

    def refresh(self):
        pass

    def on_release(self):
        if (self.paused):
            App.get_running_app().on_resume()
            self.background_color = [.7,.7,.7,1]
            self.text = "Pause"
            self.paused = False
        else:
            App.get_running_app().on_pause()
            self.background_color = [.5,.9,.5,1]
            self.text = "Resume"
            self.paused = True


class ActionDoButton(Button):
    """
    Performs action and displays status of actions currently underway
    """
    enabled=True
    action=ObjectProperty()

    def __init__(self, action, **kwargs):
        self.action = action
        super(ActionDoButton, self).__init__(**kwargs, text="DO")
        self.background_color = [1,1,0,1]

    def refresh(self):
        if(self.action.done):
            self.background_color = [.5,.5,.5,1]
            if(not self.action.complete):
                self.background_color = [.5,.5,1,1]
                self.text = "..."
            else:
                if(self.action.success):
                    self.text = "DONE"
                    self.background_color = [.3,1,.3,1]
                else:
                    self.background_color = [1,.3,.3,1]
                    self.text = "FAIL"


    def on_release(self):
        if(not self.action.done):
            self.action.do()
        self.parent.refresh()


class ClearAllNotificationsButton(Button):
    """
    Removes all notifications from notification layout
    """

    def __init__(self, **kwargs):
        super(ClearAllNotificationsButton, self).__init__(text="X")
        self.background_color = [1,.7,.7,1]
        self.color = [0,0,0,1]


    def refresh(self):
        pass

    def on_release(self):
        App.get_running_app().on_pause()
        nlayout = App.get_running_app().rootWidget.nScreen.notification_layout
        for nID, noteRow in nlayout.rowWidgets.items():
            nlayout.remove_widget(noteRow)
        nlayout.rowWidgets = {}
        App.get_running_app().on_resume()
