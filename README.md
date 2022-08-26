## Relay Rattler

<link rel="stylesheet" type="text/css" href="css/github.css"> 
 
<h1 align="center"> 
  <img src="images/L6_RelayRattler_Logo.png" alt="Relay Rattler Logo" width="75%" align="middle">
</h1> 


Use an RPi Pico microcontroller to make rhythms on an array of mechanical relays <br>


## Table of contents:

* [Relay Rattler](#relay-rattler) 
* [Table of Contents](#table-of-contents) 
* [Description](#description)
	* [Why?](#why)
* [Theory of Operation](#theory-of-operation) 
	* [Hardware Components](#hardware-components)
	* [Software Components](#software-components)
	* [Usage](#usage)
	* [Other Ideas](#other-ideas)
* [Requirements](#requirements)
* [Build](#build)
	* [Hardware](#hardware)
	* [Software](#software)

## Description:
[Table of Contents](#table-of-contents)

The "Relay Rattler" is a simple array of electromagnetic relays set up to be triggered by the output pins of a Raspberry Pi Pico (RP2040) and controlled by a rotary push knob module also hooked into the Pico.  The circuit was kept minimal, as we only need to trigger the switch to get the "clack" sound on and off and are not actually handling any load on the other side of the relays.  This design should be easily ported to any microcontroller you have on hand, and is easily expandable to larger arrays of relays as well as different relay configurations, all allowing for a lot more experimentation on your part.

The code has been kept very simple, as well.  Basic delays are used to get us "mostly there" and functional, without the complexity of asyncio, threading, etc.  You are, of course, welcome to expand on that and make it much better than it is.

### Why?:

Relay Rattler was built as an addition to a new "noise box" I am building.  I just wondered what an old clickity-clack style mechanical relay would sound like if it were triggered inside of one.  Then, I wondered what 8 of them would sound like.  Then, I wondered if they could be "sequenced" in different patterns with a little speed control.  And, here we are - with many more unanswered questions.  I hope someone can have some fun answering their own.

## Theory of Operation:
[Table of Contents](#table-of-contents)

We will refer to the following diagram for this explaination:

<h1 align="center"> 
  <img src="images/L6_RelayRattler_Schematic.PNG" alt="Relay Rattler Schematic" width="75%" align="middle">
</h1> 

### Hardware Components:



### Software Components:


### Usage:


### Other Ideas:

The most obviously immediate idea is to expand this up to 12, 16, even 32 relays, to see when the delay tricks break down and asyncio needs to be used.  Could one go for more identifiable percussive sounds, using 32?   What if one used 16 large and 16 small relays?  Could one conjor up the "tiss" of a closed hihat?  The "snap" of a snare sidestick?

One thing I will be exploring further is how the arrangement of these 16 relays in the bottom of the box can affect the sound.  Could putting them into a circle, with the pick-up piezo mic in one far corner give a sort of "doppler effect", as they traveled around in a circle?  Or, does doppler effect only happen when sounds travels through the air?  Could more and less volume be controlled by arrangement?

What about solenoids?   A good push/pull solenoid could be made to tap on just about anything.  Solenoids hitting glass?  A sheet of tin?  Tuning forks?!  oooo... a MIDI-controlled Kalimba?

It feels like this could be a bottomless pit of fun exploration for folks.

## Requirements:
[Table of Contents](#table-of-contents)

You will need the following hardware to duplicate this project, although much substitution is possible given a little thought:

(Don't worry.  None of these are affiliate links.)

* Raspberry Pi Pico RP2040 (Original or clones should work.  I used one of these: https://www.amazon.com/dp/B092S2KCV2)
* 5V SPST electromagnetic coil relays (I used 8 of these: https://www.amazon.com/dp/B088PLWFN1)
* General purpose BJT NPN transistors (I used 8 2N3904's from this kit: https://www.amazon.com/dp/B06Y49GB3F)
* Rotary encoder knob module (I used one of these: https://www.amazon.com/dp/B07F26CT6B)
* General purpose diodes (I used 8 1N4007's from this kit: https://www.amazon.com/gp/product/B007L4DX6Q)
* 150 Ω 1/4W resistor (I have so many E12 kits, not sure which I pulled from.)
* 10K Ω 1/4W resistor (I have so many E12 kits, not sure which I pulled from.)
* Amber LED (Again... easy to source.   Not much current is going through this for long.  Don't worry about color too much.)
* Breadboard... jumper wire... eventually perfboard, a soldering iron, solder, etc., if you go that way.
* A computer with Thonny to get the MicroPython code onto the Pico (or, use your favorite method)
* You can power the Pico however you desire.  I have used it powered on from the computer USB and with a dedicated regulated 5V supply of my own design.  A battery pack might work, too.  Remember, we are only triggering the switch in the relay, not actually running any load on the other side of it.

## Build:
[Table of Contents](#table-of-contents)

### Hardware:


### Software:


