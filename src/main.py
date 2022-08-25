################################################
# Noise Box Relay Rattler v0.1
# ----------------------------
# by LEVEL6
################################################

from machine import Pin
import utime

# Rotary Dial Pins
CLK_Pin=Pin(0,Pin.IN,Pin.PULL_UP)  # GP0
DT_Pin=Pin(1,Pin.IN,Pin.PULL_UP)   # GP1
SW_Pin=Pin(2,Pin.IN,Pin.PULL_UP)   # GP2

# Relay Control Pins
relays=[3,4,5,6,7,8,9,10]          # GP3 - GP10

# Relay Array
relay_pins=[]

# Patterns
pattern1Array=[[1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0],
               [0,0,0,0,1,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,1],
               [0,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,0],
               [0,0,1,0,0,0,0,0],[0,1,0,0,0,0,0,0],[1,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1]]

pattern2Array=[[1,1,1,1,1,0,1,0],[0,0,0,0,1,0,0,0],[0,0,1,0,1,0,1,0],[0,0,0,0,1,0,0,0],
               [1,1,1,1,0,0,0,0],[0,0,0,0,1,0,0,0],[0,0,1,0,1,0,1,0],[0,0,0,0,1,0,0,0],
               [1,1,1,1,0,0,0,0],[0,0,0,0,1,0,0,0],[0,0,1,0,1,0,1,0],[0,0,0,0,1,0,0,0],
               [1,1,1,1,0,0,0,0],[0,0,0,0,1,0,0,0],[0,0,1,0,1,0,1,0],[0,0,0,0,1,0,0,0]]
               
# Set all relay GP pins as output
for x in range(0,8):
    relay_pins.append(Pin(relays[x],Pin.OUT))

# Initialize the variables
thisValue=0
previousValue=1
currentMode=1
patternStep=0
delayus=0.25

# Routine to check whether there has been a change in the rotary knob
def rotary_changed():
    global previousValue
    global thisValue
    global currentMode
    global delayus

    # Check for rotation
    if previousValue!=CLK_Pin.value():
        if CLK_Pin.value()==0:
            if DT_Pin.value()==0:
                thisValue=(thisValue-1)%8
                delayus=(delayus-0.01)
                print("RELAY = ",thisValue)
                print("DELAY = ",delayus)
            else:
                thisValue=(thisValue+1)%8
                delayus=(delayus+0.01)
                print("RELAY = ",thisValue)
                print("DELAY = ",delayus)
        previousValue=CLK_Pin.value()

    if delayus<0:
        delayus=0
    if delayus>1:
        delayus=1
                    
    # Check for press
    if SW_Pin.value()==0:
        currentMode=currentMode+1
        if currentMode>3:
            currentMode=1;
        print("MODE = ",currentMode)
        utime.sleep(0.25) 

def relayPattern1():
    global patternStep
    
    for r in range(0,8):
        relay_pins[r].value(0)

    for p in range(0,8):
        relay_pins[p].value(pattern1Array[patternStep][p])
 
    patternStep=patternStep+1
    if patternStep>15:
        patternStep=0
        
    utime.sleep(delayus)    

def relayPattern2():
    global patternStep
    
    for r in range(0,8):
        relay_pins[r].value(0)

    for p in range(0,8):
        relay_pins[p].value(pattern2Array[patternStep][p])
 
    patternStep=patternStep+1
    if patternStep>15:
        patternStep=0
        
    utime.sleep(delayus)
        
# Main loop
while True:
    for i in range(0,8):
        relay_pins[i].value(0)
        rotary_changed()
        relay_pins[thisValue].value(1)
        if currentMode==2:
            relayPattern1()
        if currentMode==3:
            relayPattern2()    
        utime.sleep(0.001)
