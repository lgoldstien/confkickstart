# Kickstart.py
# Kickstart will ask questions to find out what application you want to 
# configure and then produce a configuration fil and give you the option 
# of saving this in the default system location.
#
# @package kickstart
# @version 0.1
# @author lgoldstien

import sys
import os

# Get the list of available function 
def getSciptOptions():
    return os.walk('./starters/').next()[1]

def main():
    if len(sys.argv) > 1 :
        application = sys.argv[1]
    else :
        print "No application was selected!"
        print "Please choose one of the following:"
        print ""
        for app in getSciptOptions():
            print app

if __name__ == '__main__':
    main()