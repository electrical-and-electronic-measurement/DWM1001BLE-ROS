# DWM1001BLE-RosNode
Questo repo permette di acquisire dati da sensori DWM1001 tramite BLE (quindi completamente wireless) e li pubblica in topic.
I dati di ranging raccolti vengono pubblicati in un topic ROS.
Questo repo non pubblica dati di localizzazione, ma tutto il codice necessario per raccogliere i dati di posizizione dai tag tramite bluethoot è già presente.

# Tested Platforms
- Ubuntu 20
- scheda BLE
- ROS Noetic
- 5 Decawave DWM1001 with FWM1: .... and FWM2:....

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
