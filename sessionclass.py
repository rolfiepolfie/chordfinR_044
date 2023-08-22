# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 17:51:35 2023

@author: rolfe
"""

# sessionclass.py
  


import time
from dataclasses import dataclass
import globalvars as glob 
import gmsounds as gm
#from midicom import MidiComm
from ports import Ports

from globalvars import Globals


class SessionMain():
    
    def __init__(self):
        self._midichannel_bass = -1
        self._midiTrough = True
        self._midichannel_out = -1
        self._midichannel_controls = -1
        
        self._controlArraySession = None
    
        self._midi = None
        self._filterMidi = None
        self._ports = None
        
        
        self._globalVars = []
        
        self._sustainTrigFreeze = False
    
    
    @property
    def sustainTrigFreeze(self):
        pass
    
    @sustainTrigFreeze.setter
    def sustainTrigFreeze(self, flag):
        self._sustainTrigFreeze=flag
    
    
    @property
    def midi(self):
        return self._midi
    
    @midi.setter
    def midi(self, midi): 
        self._midi = midi
        
        
    @property
    def filterMidi(self):
        return self._filterMidi

    @filterMidi.setter
    def filterMidi(self, filterMidi): 
        self._filterMidi = filterMidi


    @property
    def ports(self): 
        return self._ports
    
    
    @ports.setter
    def ports(self, ports): 
        self._ports = ports
        
    
  
    @property
    def midichannelBass(self):
        return self._midichannel_bass
    
    @midichannelBass.setter
    def midichannelBass(self, ch):
        self._midichannel_bass = ch
            
    @property
    def midiChannelControls(self):
        return self._midichannel_controls
    
    @midiChannelControls.setter
    def midiChannelControls(self, ch):
        self._midichannel_controls = ch      
        
    @property
    def midiChannelOut(self):
        return self._midichannel_out
    
    @midiChannelOut.setter
    def midiChannelOut(self, ch):
        self._midichannel_out = ch   
        
    
    def showControlsRegistered(self, controls : Globals.controls):
        
        #print("\n")
        print("* Controls registered for this session")
        print(" ----------------------------------------")
        
        for control in controls:     
            
            print("control name: \t", control.name())   #is in parent class
            print("\t triggered: \t", control._triggers)
                        
            print("\t note_cc: \t\t", control._cc_note)
            
        
        print("\n")    
        
    
    def report(self):
        print('\n')
        print(" --- Session Report --- ")
        print("Midi channel out: \t\t", self._midichannel_out)
        print("Midi channel control: \t", self._midichannel_controls)
        print("Midi channel bass: \t\t", self._midichannel_bass)
        
        print('Midi trough: ', self._midiTrough)
        
        
        self._midi.report()
        self._filterMidi.report()
        self._ports.report()  
        
        
              
  # @dataclass
  # class data:
  #     '''
  #     data struct used during a typical session
  #     '''
  #     out_port_index: int
  #     in_port_index_bass: int
  #     in_port_index_control: int
    
  #     midi_channel_in_bass: int
  #     midi_channel_in_control: int
     
  #     midi_channel_out: int
     
  #     filepath: str
  #     controlSchemes: int
  
  
    def filterSetup(self):
        
        self._filterMidi.midichannelBass = self.midichannelBass
        self._filterMidi.midiChannelControls = self.midiChannelControls
        self._filterMidi.midiChannelOut = self.midiChannelOut
        
        
        self._filterMidi.deactivate()  # <- remember to activate Filter 
        
    
    def midiSetup(self):
        
        self._ports : Ports
        ports = self._ports 
        
        #self._midi : MidiComm
        self._midi.setOutPort(ports._outPort)       
        
        
        self._midi._midiChannel_out = self._midichannel_out
        self.midi._midichannel_bass = self._midichannel_bass
        self.midi._midichannel_controls = self._midichannel_controls
        
            
        self._midi.sendProgamChange(gm.GmSounds.FX_5_brightness, self._midichannel_out)

    def testout(self, volume=100):
        
        self._midi.sendOutVolume(volume)
        self._midi.testOut()
        #self._midi.sendOutVolume(0)
    
    def portsSetup(self, rv):
        
        self._ports.openOutPort(rv.out_index) #usually there is always an outport on a computer
        UserInteraction.askuseropenports(rv, self._midi, self._filterMidi, self._ports)
        
        
    def setupSession(self, rv):
        self.portsSetup(rv)
        self.filterSetup()
        self.midiSetup()
        
        
    def reportDevices(self):
        '''
        important foruser to select harwdare 
        '''
        self._ports.report_devices() 
        
    
    
    def registerControls(self, controlarr):
        # copy controls to the global session array 
        
        glob.Globals.controls.extend(controlarr)        
        
        
        
    def nextChordScheme():
        pass
    
    

        
     
     

class UserInteraction:
    
    def askuseropenports(rv, midi, filt, ports):
        
        
        print("open inport for bass: ")
        #if ans == 'y':
        ports.openInport_bass(rv.in_index_bass) 
        midi.setinPort_bass(ports._inPort_bass, ports._inPort_bass_name, filt.trigBass) 
        time.sleep(1)
                        
        ports.openInport_control(rv.in_index_control1) 
        midi.setinPort_controlButtons(ports._inPort_control, ports._inPort_control_name, filt.trigControlChord) 
        time.sleep(1)
        
        print("open inport for control2: ")
        
        if rv.in_index_control2 != -1: 
        
            ports.openInport_control(rv.in_index_control2) 
            midi.setinPort_controlButtons(ports._inPort_control, ports._inPort_control_name, filt.trigControlChord) 
        
        else:
            print("NB ** port not opened **")
                    
        
        time.sleep(1)


    def readportnumbers():
        
        @dataclass
        class Returnvalue:
            out_index:          int
            in_index_bass:      int
            in_index_control1:  int
            in_index_control2:  int
            
        while True: # read in a midi port device 
            try:
                print(" *********** -1 if this service is not wanted. ************* ")
                print(" - ")
                out_index = int(input("For chord output, enter a number (default 0): ") or "0")
                print('\n')
                
                in_index_bass = int(input("For bass input, enter a number(default 1): ") or "1") #1
                      
                in_index_control1 = int(input("For control input1, enter a number(default 0): ") or "0") #3
                in_index_control2 = int(input("For control input2, enter a number(default -1): ") or "-1") #0
                
                break
            
            except Exception as e:
                print("er, ror: " + str(e))
                
        return Returnvalue(out_index, in_index_bass, in_index_control1, in_index_control2)
          

    