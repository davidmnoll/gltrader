import sys
import ipdb

from pprint import pprint

def dd(var=False):
    if(var):
        pprint(var)
    ipdb.set_trace()
    sys.exit()
