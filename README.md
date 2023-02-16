# DWM1001BLE-RosNode
This repo allows data to be acquired from DWM1001 sensors via Bluetooth Low Energy (BLE) - thus completely wireless - and publishes it in ROS topic. 
The DWM1001's BLE API allows it to read the same set of information that can be read via UART, and in addition, it is also possible to set all device parameters.
This repo does not publish location data, but all the code needed to collect location data from tags via bluethoot is already present along with the code to set the devices parameters.

# Tested Platforms
The code in this repo has been tested with the following configuration:
- Ubuntu 20
- Wireless Adapter Intel Wirelesss AC-9560 with Bluetooth Core Specification 5.1
- ROS Noetic
- 5 Decawave DWM1001 with FW1: 0x01030000/0x5170973E and FWM2: 0x0130000/0xCEAF1E09

# Custom Ros Messages structure
WIP

# INSTALLAZIONE
## Requisiti
- ROS (link procedura di installazione)
- Ubuntu 20
- bluethooth nel computer 
- Decawave devices (link al manuale)

##  Procedura di Installazione
- clona repo github nella catkin_ws folder
- installa le dipendenze (CONTROLLA SE LO FA IN AUTOMATICO catkin_make)
- esegui catkin_make
- source del devel/setup.bash (se non lo si ha direttamente nel .bashrc principale)

## Anchor-Tag possible configurations
- Relative Localization
- Ranging

## Get Started
- disposizione dei device nell'ambiente
- configurazione dei device usando app DRTLS (link) (qui metti i valori settati per i device leggibili dall'app)
- compilazione file Constants.py con i dati appropriati leggibili dall'applicazione DRTLS (link)
- Settaggio della modalità "Ranging" o "Localization"
- Accendere i device ed il bluethooth sul computer

# RUN
comando di rosrun su index

## Topics
All the data will be published in the topic specified by the variable "BLEDecawaveRangingTopicName" present in the file "Costants.py"


# TODO
- Add a handleNotification method for handling the classic Anchor-Tag localization directly provided by the Decawave firmware.
