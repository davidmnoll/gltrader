import os
import sys

import json
from .bittrex import Bittrex
from .market import Market
from .notification import *
from .fakeapi import FakeAPI
from jsmin import jsmin
import threading

from pprint import pprint as pp



class Trader(object):
    """
    The object which makes the tick API read calls and dispatches the data to the markets
    """
    #raw API data from each tick
    data = None
    #dict of each market object keyed by abbr of crypto used by bittrex
    markets = {}
    #list of notifications that should be displayed
    notifications = {}
    #config is false until parsed from file
    config = False

    def __init__(self):
        """
        sets parameters and parses config dictionary from file
        """
        #open file
        with open(os.environ['GLTRADER_CONFIG'] ) as config_file:
            #parse and reduce json so it can have comments
            minified = jsmin(config_file.read())
            #convert to json
            self.config = json.loads(minified)
            #create new instance of API wrapper object and set as property of trader object so it can be accessed
            self.api = Bittrex( self.config["exchange"]["bittrex"]["key"],
                self.config["exchange"]["bittrex"]["secret"], api_version="v2.0" )
            #mocked API that can be used for some basic testing of live trades (cannot replace whole API)
            self.fapi = FakeAPI()


    def getData(self):
        """
        Makes API call to get data, returns empty if not successful

        :returns: List[Dict] if succesful, or None
        """
        #get data via get_balances to limit individual calls and make sure data used down the line is synchronous
        response = self.api.get_balances()
        #if API responds
        if response["success"]:
            return response["result"]
        #allow execution to continue with failed tick without errors, but don't actually do anything
        else:
            pp(response)
            Alert("Tick missed: "+response.get(message, "Tick failed, no message"))
            return None

    def refreshMarkets(self):
        """
        Checks for data and calls "getMarkets"
        """
        #Get data then send to markets ---Factored out in case more things need to get done on each tick at this level in the future
        self.data = self.getData()
        if (self.data is not None):
            self.getMarkets()


    def getMarkets(self):
        """
        For each list entry in the returned data, start a thread and create (if it doesn't exist) or refresh the appropriate market.

        Join the threads so it next tick cannot be called before execution is finished and UI doesn't update before they finish.
        """
        if self.data is not None:
            threads=[]
            # for each raw data dict in array
            for  marketdata in self.data:
                # get name of market from dict
                name = marketdata["Currency"]["Currency"]
                #if market is already in the dict
                if name in self.markets:
                    #set new thread to call "update" method on market
                    t = threading.Thread(target=self.markets[name].update, args=[marketdata])
                    threads.append(t)
                    t.start()
                    # threading.Thread(target=self.printVars).start()

                else:
                    #add market and set thread to update
                    self.markets[name] = Market(name, marketdata)
                    t = threading.Thread(target=self.markets[name].update, args=[marketdata])
                    threads.append(t)
                    t.start()
            #join all the threads back so UI update won't start before they finish
            for t in threads:
                t.join()
        else:
            pass


    def getNotifications(self):
        """
        :returns: Dictionary[Notification] A dictionary with the notifications
        """
        #keeping notifications run in trader in case it is necessary in the future
        return self.notifications

    def printVars(self):
        """
        For debugging purposes
        """
        for var, obj in locals().items():
            print( var, sys.getsizeof(obj))



    def dump(self):
        """
        Return api data from markets --- used for tests
        """
        pp(self.api.get_balances())

    def dumplist(self):
        """
        Return api data from markets --- used for tests
        """
        response = self.api.get_balances()
        return response["result"]
