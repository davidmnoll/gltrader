
from kivy.app import App
from kivy.properties import ObjectProperty
from datetime import datetime
# from .ui.notifications.notification_row import NotificationRow
from pprint import pprint as pp
import inspect

class Notification(object):
    """
    This class controls lines that are added to the notification screen
    """
    rowWidget = ObjectProperty
    isError = False
    level = 0
    market = None
    action = None
    order = None
    status = 0
    sender = None

    def __init__(self, msg, sender=None, **kwargs):
        """
        Parses message and sender, sends object to GUI, and refreshes GUI so notification shows up instantly rather than wait for the tick

        :param msg: Either a string to be used as the message or a shorthand manually defined in the getMessageValues dict
        :param sender: (Default=None) the object sent.  Allows buttons to be added to link to objects that sent the notification
        """
        self.time = datetime.now()
        self.message = self.getMessage(msg)
        self.sender = sender
        self.getObjects( kwargs)
        if(self.sender):
            self.header()
            print(self.message)
            pp(self.sender)
            self.footer()
        else:
            self.oneline()
        self.notified = False
        App.get_running_app().trader.notifications[id(self)] = self
        App.get_running_app().rootWidget.nScreen.notification_layout.refresh()

    def getMessageValues(self):
        """
        Defines a set of short-hand messages that can be sent

        :returns: (Dict) mapping of shorthand messages to longer strings
        """
        return {
            "added" : "Market was added for Monitoring",
            "removed" : "Market was removed from Monitoring",
            "minbuy" : "A minimum buy was suggested",
            "minsell" : "A minimum sell was suggested",
            "maxbuy" : "A maximum buy was suggested",
            "maxsell" : "A maximum sell was suggested",
        }

    def refreshWidget(self):
        App.get_running_app().rootWidget.nScreen.notification_layout.rowWidgets[id(self)].refresh()

    def getMessage(self, msg):
        """
        Checks shorthand list and returns appropriate message

        :param msg: (String) the msg string passed into object
        :returns: (String) message to be displayed
        """
        values = self.getMessageValues()
        if msg in values:
            return values[msg]
        else:
            return msg

    def getObjects(self, kwargs):
        """
        Sets object properties depending on what object is sent into self as "sender"

        :param kwargs: the keyword args passed into the object
        """
        self.action = kwargs.get("action", False)
        self.market = kwargs.get("action", False)
        if self.sender:
            for base in inspect.getmro(self.sender.__class__):
                if "Market" == base.__name__ or "Market" == self.sender.__class__.__name__:
                    if self.sender.checkUpToDate:
                        self.market = self.sender
                    else:
                        pp( self.sender.name)
                        return None
                elif "Action" == base.__name__ or "Action" == self.sender.__class__.__name__:
                    self.market = self.sender.market
                    self.action = self.sender

                elif "Order" == base.__name__ or "Order" == self.sender.__class__.__name__:
                    self.market = self.sender.market
                    self.order = self.sender


    def header(self):
        """
        Cleaner logging in terminal
        """
        print("||````````")
        print(self.message)
        pp(self.sender)

    def footer(self):
        """
        Cleaner logging in terminal
        """
        pp("````````||")

    def oneline(self):
        """
        Cleaner logging in terminal
        """
        print("|| "+self.message+" ||")



class Info(Notification):
    """
    Alias for Notification with different console logging style
    """

    def oneline(self):
        print("----Info: "+self.message+" ------")

    def header(self):
        print("||----Info:")

    def footer(self):
        print("---------||")

class Success(Notification):
    level = 3

    """
    Shows as green in GUI notification_row
    """

    def oneline(self):
        print("....Success: "+self.message+" .......")

    def header(self):
        print("||....Success:")

    def footer(self):
        print("............||")

class Error(Notification):
    level = 9

    """
    Shows as red in GUI notification_row
    """

    def oneline(self):
        print("******ERROR: "+self.message+" ******")

    def header(self):
        print("||*************")
        print("ERROR:")

    def footer(self):
        print("*************||")

class Alert(Notification):
    level = 6

    """
    Shows as yellow in GUI notification_row
    """

    def oneline(self):
        print("=======ALERT: "+self.message+" ======")

    def header(self):
        print("||=======ALERT:")

    def footer(self):
        print("=============||")
