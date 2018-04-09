
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import NumericProperty, ObjectProperty
from kivy.app import App

from pprint import pprint as pp

class MarketNumberLabel(Label):
    """
    UI control for Numbers in table of market data.  Inherits Kivy "label" object which is used to display text
    """
    value=NumericProperty()
    app=App.get_running_app()
    old=ObjectProperty()

    def __init__(self, getter, **kwargs):
        """
        :param getter: (Method) The function responsible for returning the numerical value--will be executed each tick
        """
        self.getter = getter
        self.value = getter()
        self.old = self.value
        self.bind(value=self.refresh)
        self.text = f'{self.value:.8f}'
        super(MarketNumberLabel, self).__init__(**kwargs, text=self.text)


    def refresh(self, instance=None, newval=None):
        """
        Callback for "bind" method -- executed on change of self.value.  Sets text to value and calls methods to change color depending on value

        :param instance: current object instance
        :param newval: new value of "value" property
        """
        self.value = self.getter()
        self.text = f'{self.value:.8f}'
        if float(self.value) > float(self.old):
            self.flashgreen()
        elif float(self.value) < float(self.old):
            self.flashred()
        self.old = self.value


    def flashred(self):
        """
        Set color to red until next tick
        """

        self.color = [1, .5, .7, 1]

    def flashgreen(self):
        """
        Set color to green until next tick
        """

        self.color = [.5, 1, .7, 1]
