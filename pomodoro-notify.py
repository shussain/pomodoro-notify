#!/usr/bin/env python

# This script is a Pomodoro timing tool (http://en.wikipedia.org/wiki/Pomodoro_Technique).
# It will use pynotify to display notificaiton to user to either take a break or to
# get back to work - depending on arguments passed to it in the command line
#
# To work for 25 minutes, enter: ./pomodoro-notify
# To keep track of a 5 minute break, enter: ./pomodoro-notify -b
import sys
from optparse import OptionParser
from time import sleep

try:
    import pynotify
except:
    sys.stderr.write("ERROR: pynotify not found. Application will not work without it.\n")
    sys.exit(1)

BREAKTIME = 300 # 5 minutes (in seconds)
WORKTIME = 1500 # 25 minutes (in seconds)

VERSION = 0.1   # Version of the software

# Parse options that user has entered
def parse_options():
    usage = """\
pomdoro-notify.py
        [options]
"""
    parser = OptionParser(usage=usage)
    parser.add_option('-b', '--breaktime',
                      action='store_true',
                      help="Have a %d minute break countdown." % (BREAKTIME/60) )

    parser.add_option('-v', '--version', action='store_true',
                      help="Display version")

    options, args = parser.parse_args()

    if args:
        parser.print_help()
        sys.exit(1)

    return options

def main():
    options = parse_options()

    if (options.version):
        print "Version %2.2f" % (VERSION)
        sys.exit(1)

    # Sleep till notification is needed.
    sleeptime = BREAKTIME if (options.breaktime) else WORKTIME
    sleep(sleeptime)

    title = "Breaktime is over." if (options.breaktime) else "Good job!"
    body = "Get back to work!" if (options.breaktime) else "Now take a break."

    pynotify.init( "Init string")
    n = pynotify.Notification(title, body, "dialog-info")
    n.set_urgency(pynotify.URGENCY_NORMAL)
    n.show()
    n.close()

if __name__ == '__main__':
    main()
