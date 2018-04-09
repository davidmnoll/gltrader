from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.properties import DictProperty
from .market_table_columns import MarketTableColumns
from kivy.app import App


from pprint import pprint as pp

class MarketRow(GridLayout):
    """
    Responsible for displaying a single row of the market info table.  Gets "getters" from MarketTableColumns and creates a dictionary of Labels from those getters
    """

    columns=DictProperty()

    def __init__(self, market=None, **kwargs):
        """
        :param market: (Market) The market to be displayed
        """
        self.market=market
        self.bind(columns=self.refresh)
        super(MarketRow, self).__init__(**kwargs, rows=1, size_hint=(1, 30))
        self.columns = MarketTableColumns(self.market).getWidgets()
        for label, widget in self.columns.items():
            self.columns[label] = widget
            self.add_widget(self.columns[label])
            self.columns[label].refresh()
        self.app=App.get_running_app()
        self.app.rootWidget.refreshers.append(self.refresh)
        self.refresh()

    def refresh(self, obj=None, val=None):
        """
        self.column is a dict of widgets.  This either refreshes or adds each widget in the view when the dict is updated

        :param obj: The current instance
        :param val: The new value of "columns"
        """
        for label, widget in self.columns.items():
            if label in self.columns:
                self.columns[label].refresh()
            else:
                self.columns[label] = widget
                self.add_widget(self.columns[label])
                self.columns[label].refresh()
