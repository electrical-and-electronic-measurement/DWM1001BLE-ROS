# DWM1001BLE-RosNode
This repo allows data to be acquired from DWM1001 sensors via Bluetooth Low Energy (BLE) - thus completely wireless - and publishes it in ROS topic. 
The DWM1001's BLE API allows it to read the same set of information that can be read via UART, and in addition, it is also possible to set all device parameters.
This repo does not publish location data, but all the code needed to collect location data from tags via bluethoot is already present along with the code to set the devices parameters.

# Tested Platforms
The code in this repo has been tested with the following configuration:
- Wireless Adapter Intel Wirelesss AC-9560 with Bluetooth Core Specification 5.1
- 5 Decawave DWM1001 with FW1: 0x01030000/0x5170973E and FWM2: 0x0130000/0xCEAF1E09
- Ubuntu 20
- ROS Noetic
- Pycharm - Professional 2022

# Custom Ros Messages structure
To see the message stucture referes to the .msg files in the msg folder

# INSTALLATION
## Requisiti
- Linux based system 
- ROS Noetic (here the installation instruction http://wiki.ros.org/noetic/Installation)
- BLE Adapter 
- At least 2 Decawave DWM1001 devices ([here](https://www.qorvo.com/products/p/MDEK1001) the manufacter device web page)

##  Softare installation steps
- Setup your ROS environment: complete the steps given [here](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment) up to step 3
- Clone this repo into a folder into your catkin_ws workspace. Once you are into the 'catkin_ws' folder, for expample runnig this command: ``` git clone https://github.com/valiokei/DWM1001BLE-RosNode.git ``` or using the [GitHub Desktop app](https://gist.github.com/berkorbay/6feda478a00b0432d13f1fc0a50467f1?permalink_comment_id=4381065#gistcomment-4381065) using the link in the '<> Code' button above.
- Install the dependencies in the file requirements.txt using  ```pip install -r requirements.txt```
- execute ```catkin_make``` command in the caktin_make folder 
- source the file 'devel/setup.bash' with ```source devel/setup.bash``` from the catkin_ws folder

## Dwm1001 devices configuration steps
To setup a DWM1001 device you have to use the [app DRTLS](https://www.qorvo.com/products/d/da007984).
Below the parameter setted for a Tag and a Achor through the app.

- ### Tag Configuration 
  - UWB: active
  - Node Type: tag
  - Responsive Mode: enabled
  - BLE: enabled
  - Location Engine: enabled
  - Stationary Detection: enabled
  - Normal Update Rate: 10 Hz
  - Stationary Update Rate: 10 Hz
- ### Anchor Configuration
  - UWB: active
  - Node Type: anchor
  - BLE: enabled
  - Initiator: enabled

## UWB Devices Available Features
This repo provides two different features: Localization and Ranging
- ### Localization: with this feature all the measures collected from each Tag are published at the same time to maintain the synchronization. This is essential if you want to locate multiple devices at the same time. This, to work need that all the ranging data from all the tags were collected.
- ### Ranging: this feature just give the rannging data, e.g. the distance, between a couple of device (one Tag and one Anchor)


## Get Started
- In accordance with the chosen feature, appropriately arrange the appropriately configured uwb devices 
- Fill file 'Constants.py' with the data of yours uwb devices. This data can be read from the app. Also remember to set the "Ranging" or "Localization".

# RUN
- An index file is provided in the script  folder, you can run it with: ```rosrun DWM1001BLE-RosNode index.py```

## Topics
All the data will be published in the topic specified by the variable "BLEDecawaveRangingTopicName" present in the file "Costants.py"


# TODO
- Add a handleNotification method for handling the classic Anchor-Tag localization directly provided by the Decawave firmware.
- Update to ROS2
