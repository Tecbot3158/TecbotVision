__author__ = "Trevor - tecbot"


import sys
from networktables import NetworkTables

import logging
import time

logging.basicConfig(level=logging.DEBUG)

#verifies that command line argument is valid
if len(sys.argv) != 2:
    print("Error: specify an IP to connect to!")
    exit(0)

#gets first argument from the command line
#TODO change ip address to 10.31.58.2
ip = sys.argv[1]

NetworkTables.initialize(server=ip)

chameleonNT = NetworkTables.getTable("chameleon-vision")
camera0NT = chameleonNT.getSubTable("camera0")

#initializing tecbot tables
tecbotVisionNT = NetworkTables.getTable("tecbotVision")
tecbotVisionNT.getBoolean("object", False)

if __name__ == "__main__" :
    try:
        while True:
            
            isValid = camera0NT.getBoolean("isValid", True)
            #print(isValid)
            tecbotVisionNT.getEntry("object").setBoolean(isValid)
    except KeyboardInterrupt:
            pass
