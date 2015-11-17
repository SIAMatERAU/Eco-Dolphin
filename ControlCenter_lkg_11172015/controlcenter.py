#Eco-Dolphin
#Control center for the decision making interface. 
#Each imported function will support the node output in some capacity.

import serial
import math
import time
import avoid
import checkpoint
import cmdAgent
import getHeading
import getPosGraph
import isfloat
import getPosition
import hover
import proximity
import resurface
import separateString
import setAcceleration
import setBoundary
import setPoint
import setTarget
import surface
import toll

#set up communication: publish info received from serial port to appropriate file
fob = open('/home/pi/Eco-Dolphin/ControlCenter_output/accel.txt','w')
fob2 = open('/home/pi/Eco-Dolphin/ControlCenter_output/ylocation.txt','w')
port = '/dev/ttyACM0'
baud = 4800

ser = serial.Serial(port, baud, timeout=timeOut)
ser.open()

#initialize variables
response = ""
timeOut = 1
hoverTime = 150

#commands to send to agent
Accel = '1'
PwrOn = '2'
PwrOff = '3'
Idle = '4'
Right = '5'
Left = '6'
Rise = '7'
Dive = '8'
Fwd = '9'
Back = '0'


#################################### MAIN code begins here #########################################
response = cmdAgent(PwrOn)
print response

#functional loop
while 1:
   elapsetime+=time.clock()
   #check if destination has been reached
   if (isLocation):
        #hover for a prescribe amount of time before retreat
           ser.write(Hover(hoverTime))
           print 'Hovering'
           resurface()
           response  = cmdAgent(PwrOff)
           print response
   else:
                #check the state of the agent
        if response == "" or response == 'Ready':
               print 'Ready'
        else:#add Ready, Abort, Override option
               print 'Not Ready'
               response = cmdAgent(PwrOn)
  


