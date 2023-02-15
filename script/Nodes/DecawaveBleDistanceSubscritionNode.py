#!/usr/bin/env python
import threading

import rospy
from bluepy import btle

from config.Constants import BLEDecawaveRangingTopicName, Devices
from msg import DecawaveRanging, DecawaveTagRanges, TagRange
from script.BleLib.DecawaveBle import parse_location_data_bytes, get_decawave_peripheral, DecawaveDevice, \
    scan_for_decawave_devices, NETWORK_NODE_SERVICE_UUID, LOCATION_DATA_CHARACTERISTIC_UUID


class MyDelegateLocalization(btle.DefaultDelegate):

    def __init__(self, handle, tagName, publisher: rospy.Publisher, rosMsg):
        # print("Ranging Delegate!")
        btle.DefaultDelegate.__init__(self)
        self.handle = handle
        self.tagName = tagName
        self.publisher = publisher
        self.rosMsg = rosMsg

    def handleNotification(self, cHandle, data, ):
        if (cHandle == self.handle):
            if len(self.rosMsg.DecawaveRanging) > len(
                    list(filter(lambda device: device['InitialStatus'] == 'Tag', Devices))):
                raise Exception("THE ROSMSG HAS MORE THAT",
                                len(list(filter(lambda device: device['InitialStatus'] == 'Tag', Devices))),
                                "TAG, THIS IS INCONSISTENT WITH THE DEVICES SPECIFIED IN THE 'Constants.py' FILE")

            parsedData = parse_location_data_bytes(data)
            newDecawaveTagRangesMsg = DecawaveTagRanges()
            newDecawaveTagRangesMsg.TagName = self.tagName

            for elm in parsedData["distance_data"]:
                tagMsg = TagRange()
                tagMsg.AnchorNodeId = elm["node_id"]
                tagMsg.distanceFromAnchor = elm['distance']
                tagMsg.qf = elm['quality']
                newDecawaveTagRangesMsg.TagRanges.append(tagMsg)

            if self.tagName not in list(map(lambda range: range.TagName, self.rosMsg.DecawaveRanging)):
                self.rosMsg.DecawaveRanging.append(newDecawaveTagRangesMsg)
            else:
                list(filter(
                    lambda range: range.TagName == self.tagName, self.rosMsg.DecawaveRanging)
                )[0].TagRanges = newDecawaveTagRangesMsg.TagRanges

            if len(self.rosMsg.DecawaveRanging) == 3:
                self.publisher.publish(self.rosMsg)
                self.rosMsg.DecawaveRanging.clear()


class MyDelegateRanging(btle.DefaultDelegate):
    def __init__(self, handle, tagName, publisher: rospy.Publisher):
        # print("Ranging Delegate!")
        btle.DefaultDelegate.__init__(self)
        self.handle = handle
        self.tagName = tagName
        self.publisher = publisher

    def handleNotification(self, cHandle, data, ):
        if (cHandle == self.handle):

            rosMsg = DecawaveRanging()

            parsedData = parse_location_data_bytes(data)
            newDecawaveTagRangesMsg = DecawaveTagRanges()
            newDecawaveTagRangesMsg.TagName = self.tagName

            for elm in parsedData["distance_data"]:
                tagMsg = TagRange()
                tagMsg.AnchorNodeId = elm["node_id"]
                tagMsg.distanceFromAnchor = elm['distance']
                tagMsg.qf = elm['quality']
                newDecawaveTagRangesMsg.TagRanges.append(tagMsg)

            if self.tagName not in list(map(lambda range: range.TagName, rosMsg.DecawaveRanging)):
                rosMsg.DecawaveRanging.append(newDecawaveTagRangesMsg)
            else:
                list(filter(
                    lambda range: range.TagName == self.tagName,
                    rosMsg.DecawaveRanging))[0].TagRanges = newDecawaveTagRangesMsg.TagRanges
            # print("going To publish: ", rosMsg)
            self.publisher.publish(rosMsg)


class BLEDWM1001(threading.Thread):
    devices = scan_for_decawave_devices()
    rosMsg = DecawaveRanging()
    peripheralDevices = []

    def __init__(self, device: DecawaveDevice, UseMode: "Ranging" or "Localization"):
        threading.Thread.__init__(self)
        self.devices = BLEDWM1001.devices
        self.device = device
        self.useMode = UseMode
        self.DWM_SERVICE_UUID = NETWORK_NODE_SERVICE_UUID
        self.DWM_LOCATION_CHARACTERISTIC_ID = LOCATION_DATA_CHARACTERISTIC_UUID

        self.publisher = rospy.Publisher(BLEDecawaveRangingTopicName, DecawaveRanging, queue_size=1)
        self.RosMsg = BLEDWM1001.rosMsg

    def run(self, event=None):

        dev = get_decawave_peripheral(self.device)
        BLEDWM1001.peripheralDevices.append(dev)
        try:
            service = dev.getServiceByUUID(self.DWM_SERVICE_UUID)
            MeasurementCharacteristics = service.getCharacteristics(
                self.DWM_LOCATION_CHARACTERISTIC_ID)[0]
            # Assign delegate to target characteristic
            if self.useMode == "Localization":
                dev.setDelegate(
                    MyDelegateLocalization(MeasurementCharacteristics.getHandle(),
                                           tagName=self.device.device_name,
                                           publisher=self.publisher,
                                           rosMsg=self.RosMsg
                                           ))
            elif self.useMode == "Ranging":
                dev.setDelegate(
                    MyDelegateRanging(MeasurementCharacteristics.getHandle(),
                                      tagName=self.device.device_name,
                                      publisher=self.publisher,
                                      ))
            desc = MeasurementCharacteristics.getDescriptors()
            dev.writeCharacteristic(desc[0].handle, b"\x01\x00")
            while not rospy.is_shutdown():
                if dev.waitForNotifications(1.0):
                    # Here the handleNotification() method is called each time a new notification is present.
                    continue
        except Exception as e:
            dev.disconnect()
            raise (e)

    @staticmethod
    def stopper(event=None):
        for device in BLEDWM1001.peripheralDevices:
            device.disconnect()
