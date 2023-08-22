# -*- coding: utf-8 -*- 

import logging as logg
import config ##globals config variables for this app 

from chords import Chords
from midicom import MidiComm
from ports import Ports
from controls import Controls
from midiMessage import Midimess
from utilities import MidimsgType, Misc
from filterMidi import Filter 

from setup import SetupBlacstarController
from sessionclass import SessionMain
from sessionclass import UserInteraction as ui # set this in a proper system

import rtmidi as rt
import sys
import mido

from globalvars import Globals

from paletteSelector import Palette_normal1, Palette_normal2, Palette_advanced1, PaletteSelector

#testing out the palette (cordpalette selector)
normal1=Palette_normal1()
normal2=Palette_normal2() 
advanced=Palette_advanced1()
     
ps=PaletteSelector(normal1, normal2, advanced)



### tesing callback which is registered with any controller of choice 
## used for controls that shall evoke other controls
## a control must be registered with this callback
def callback_controls_live(msg):   
    print("callback live, registered with  control5: ", msg)
    
    arrPalette=ps.scan(msg.value)
    
    print("arr: Palette or chord scheme: ", arrPalette)
    
    
    
    
    
    

### too many callbacks?
    

#being called when the foot controller hardware is invoked                   
def callback_Control_Buttons(msg) -> None:
    
    mess=Midimess(msg) # assume all have a mess.type property 
    #print(mess.totext())
    
    def scanGlobals(trigtype : MidimsgType, msg):
        
        for c in Globals.controls: 
            c._execute(trigtype, msg) # every control got a _execute(...)
            
     
    if mess.isnoteOn():         scanGlobals(MidimsgType.note_on,        msg)       
    if mess.isnoteOff():        scanGlobals(MidimsgType.note_off,       msg) 
    if mess.isControlChange():  scanGlobals(MidimsgType.controlchange,  msg)
        
    
def callbackBass(msg) -> None:  #rename msg to midiOriginal    
    ''' 
    msg = original MIDI message, recall only original messages for the engine 
        set flag global_bassdown
    set root-note in global_chord_root
    send bass-note as midi-trough if requested 
    '''
    midimsg = Midimess(msg)
    
    #the device used for bass can also send CC messages
    # send CC to all controls
    if midimsg.isControlChange(): callback_Control_Buttons(msg) # <- test
    
    
    #logg.info("callbackBass")
    #print('callbackBass - ', msg)
    
    def alterOutMidiChannel(newchannel):
        '''
        if you want alter the output midichannel only
        while retaining  other parameters  like another channel'''
        midi.sendMessageOut(msg.copy(channel=newchannel))
        
    if session._midiTrough:       
        midi.sendMessageOut(msg) 
        # mimics the same as midi-through 
        # using midimsg did not work ..need original midi message!
        # alterOutMidiChannel(10)
    
    if midimsg.isnoteOn():
        Globals.global_bassdown=True
        
        if Globals.global_Control_disable_chord_root == False: #control = freeze-root
           Globals.global_chord_root = msg.note #we know it is a note at this stage
            
        #print("global_chord_root note: ", glob.Globals.global_chord_root)
        return
        
    if midimsg.isnoteOff():
        Globals.global_bassdown=False
        #print("Globals.global_bassdown=False")
        return
        

def setupSession(session : SessionMain , midi, ports, filterMidi, glob : Globals, callbackLive) -> None:
    
    ctrl = SetupBlacstarController(Controls, Chords, midi, callbackLive).controlarray
        
    session.registerControls(ctrl)   # loads global control array with controls 
    
    # remark Misc class object not an instance, test globals
    Controls.printall(Controls) #to be improved 
      
    session.showControlsRegistered(Globals.controls)
    
    # midichannels [0...15] - other subclasses copy these values 
    session.midichannelBass=3
    session.midiChannelControls=0
    session.midiChannelOut=15  
    session._midiTrough = True   
        
    # attach big objects
    session.filterMidi = filterMidi
    session.midi = midi
    session.ports = ports
    
    session.reportDevices() #port devices
    portindexes=ui.readportnumbers()  # reads port indexes from user
        
    session.setupSession(portindexes)

    session.testout(30)
    session.report()
    
    

def _destruct():
    '''
    This will work as the destructor in the later Session Class 
    '''    
    
    if midi.InportsEmty()== False:
        print('* sending all notes off')
        midi.sendAllNotesOff() #hardware dependent 

        print('* closing all ports')
        ports.closeAllPorts() 
        
    ports.report()
    print('* program ended - bye')
    Misc.printTitle(mido, rt, sys, config.___version___, config.___title___)
    raise SystemExit(0) #clean way to exit , no traceback



# Global instances to be shared among modules 
session     = SessionMain()
midi        = MidiComm(mido, offset=config.__offset__, chordTimeLength=config.__chordTimeLength__) #offset = transpose 
ports       = Ports(mido)
filterMidi  = Filter(callbackBass, callback_Control_Buttons) 


# use the sustain pedal to "lock" the chord?
# we also need a C_plus or C-aug = C-augmented (sharpen 5th command)
# an add6, add2 to 7 = 9th chord?   also dim
# function for going to the most used chord - reset-chord ... minor, major


def main():
    #logg.basicConfig(level=logg.INFO)
    
    #https://www.pylenin.com/blogs/python-logging-guide/
    logg.basicConfig(stream=sys.stdout, level=logg.INFO)
    # logg.debug('debug')
    logg.info("info message 123")
    # logg.warning('warning')
    # logg.error('error')
    Misc.printLogo()
    Misc.printTitle(mido, rt, sys, config.___version___, config.___title___)
    setupSession(session, midi, ports, filterMidi, Globals, callback_controls_live) 
    Misc.printMainMenu()

    midi.startLoop_keyboardlistener(_destruct, midi, Misc, session) # polling the keyboard 
        
##################################################################################   
if __name__ == "__main__": main()    
    
    