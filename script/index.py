#!/usr/bin/python
import rospy

from config.Constants  import Devices
from script.Nodes.DecawaveBleDistanceSubscritionNode import BLEDWM1001

def stopper():
    print("going to disconnect the Devices")
    BLEDWM1001.stopper()


if __name__ == '__main__':

    rospy.init_node('DWM1001BLE-RosNode', anonymous=True)
    rospy.on_shutdown(stopper)

    # Here you can choose a shared use_mode for all the devices
    # The option are "Ranging" and "Localization"
    USE_MODE = "Ranging"

    for deviceName in list(filter(lambda device: device['InitialStatus'] == 'Tag', Devices)):
        ble = BLEDWM1001(device=BLEDWM1001.devices[deviceName["Name"]], UseMode=USE_MODE)
        ble.start()
    # this start the ble connection and start publishing the uwb ranging data
    # It creates istances of the class, one for each tag and use it to connect to the ble device, grab data and publish
    # in ROS

    rospy.spin()
