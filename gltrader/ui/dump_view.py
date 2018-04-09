"""
This lists a raw balances response from the API
"""

from kivy.uix.listview import ListView

class DumpView(ListView):
    """
    Only used for testing
    """

    def __init__(self, trader, **kwargs):
        dump = trader.dumplist() # call dumplist method to receive raw JSON about balances in list
        super().__init__( item_strings=[str(index) for index in dump] ) # Create list view from list of balances
