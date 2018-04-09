"""
This lists a raw balances response from the API
"""

from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from .market_table_columns import MarketTableColumns

from pprint import pprint as pp

class MarketTableHeader(GridLayout):
    """
    Used to separate the concern of the top label row of the market table from the rest of the rows
    """

    columns={}

    def __init__(self,  **kwargs):
        super(MarketTableHeader, self).__init__(**kwargs, rows=1, size_hint=(1, 50))
        for label, widget in MarketTableColumns().getLabels().items():
            self.columns[label] = widget
            self.add_widget(self.columns[label])

    def refresh(self):
        for label, widget in newColumns:
            if label in self.columns:
                self.columns[label].refresh()
            else:
                self.columns[label] = widget()
                self.add_widget(self.columns[label])
