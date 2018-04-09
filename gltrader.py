import os
import sys
os.environ['KIVY_HOME'] = os.path.dirname(os.path.abspath(__file__))+'/../kivy'
# from memory_profiler import profile

from gltrader.gltrader import GLTraderApp


"""
This file can be used to call the app as a script, so it can be passed into a profiler
uncomment the 2 lines above "runapp" to start profiling
"""


# fp=open('./profiles/memory_profiler.log','w+')
# @profile(stream=fp)
def runapp():
    """
    This file can be used to call the app as a script, so it can be passed into a profiler
    uncomment the 2 lines above "runapp" to start profiling
    """
    GLTraderApp().run()


if __name__ == '__main__':
    runapp()
