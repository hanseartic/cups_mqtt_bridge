#!/usr/bin/env python

import daemon
import os.path
import ConfigParser
from MqttBridge import MqttBridge

def init():
    config = ConfigParser.ConfigParser()
    for loc in os.curdir,\
               os.path.join(
                   os.path.expanduser("~"),
                '.config',
                'cups_mqtt_bridge'
               ),\
               os.path.join(
                   '/etc',
                   'cups_mqtt_bridge'
               ):
        try:
            with open(os.path.join(loc, "cups_mqtt_bridge.conf")) as source:
                config.readfp(source)
        except IOError as e:
            # print e
            pass
    for item in config.sections():
        print item

    from CUPSWatch import CUPSWatch
    cupsWatch = CUPSWatch(config.items('mqtt'))


# with daemon.DaemonContext:
#    main()

if __name__ == "__main__":
    init()
