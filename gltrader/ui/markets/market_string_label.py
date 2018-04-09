"""
This lists a raw balances response from the API
"""


from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import ObjectProperty, StringProperty
from kivy.app import App

from pprint import pprint as pp

class MarketStringLabel(Label):
    """
    UI control for Numbers in table of market data.  Inherits Kivy "label" object which is used to display number formatted as percent
    """
    value=StringProperty()
    app=App.get_running_app()
    old=ObjectProperty()

    def __init__(self, getter, **kwargs):
        """
        :param getter: (Method) The function responsible for returning the numerical value--will be executed each tick
        """
        self.getter = getter
        self.bind(value=self.refresh)
        self.value = getter()
        self.text = self.value
        super(MarketStringLabel, self).__init__(**kwargs, text=self.text)


    def refresh(self, instance=None, newval=None):
        """
        Callback for "bind" method -- executed on change of self.value.  Sets text to value

        :param instance: current object instance
        :param newval: new value of "value" property
        """
        self.value = self.getter()
        self.text = self.value
        self.old = self.value
