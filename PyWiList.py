from IWList import *
import sys, os, logging

logging.basicConfig()
log = logging.getLogger("PyWiList")
log.setLevel(logging.DEBUG)

if __name__  ==  '__main__':
    iwl = IWList(sys.argv[1])
    print(iwl.getData())

    
