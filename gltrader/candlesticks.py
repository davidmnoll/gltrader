
import os
from datetime import datetime
import collections

from pprint import pprint as pp

class MarketCandlesticks(object):
    """
    This class is where the data about prices, etc is stored.  Each tick calls "update" and sends an array of data to this object per market, which is then added to the ordered dictionary with max length defined in config file as "datalength."
    """
    movAvgVol = 0
    movAvgCount = 0

    def __init__(self, market):
        """
        Accepts the market which created it
        :param market: (Market) -- the market which is associated with this object
        """
        self.config = market.config
        self.marketname = market.name
        self.archive = collections.OrderedDict({})
        self.latest = {}
        self.update(market.data["BitcoinMarket"])

    def update(self, data):
        """
        Accepts the array of data passed by the trader at each tick
        :returns: void
        """
        self.archive[datetime.now().strftime("%Y%m%d%H%M%S%f")] = data # Timestamp used as key in case graphs are to be used in future
        self.latest = data
        self.last = self.latest
        self.setMovAvgVol()
        self.movAvgCount += 1
        if len(self.archive) >= self.config["datalength"]:
            oldest = min(self.archive.keys())
            del(self.archive[oldest])

    def setMovAvgVol(self):
        """
        Void method sets class property of moving average volume
        :returns: void
        """
        self.movAvgVol = (self.movAvgVol*self.movAvgCount + float(self.latest["BaseVolume"]))/(1+self.movAvgCount)
