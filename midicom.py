# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 11:13:25 2023

@author: rolfe
"""

from utilities import MidimsgType, CCvalues

import time
import copy
import keyboard
from sessionclass import SessionMain

import globalvars as glob

from typing import List



class MidiComm():
    """ 
    supports one out and many inports 
    
    """
    def __init__(self, mido, offset : int, chordTimeLength):
        
        
        self._outPort = None  
        self._inPortBass = None 
        self._inPortControlButtons = None 
        
        self._inPortBass_name=''
        self._inPortControlButtons_name=''
        
        self._offset = offset
        self._chordLength = chordTimeLength
        
        self._mido =mido

        self._midichannel_bass = -1
        self._midichannel_controls = -1    
        self._midiChannel_out = -1
        

    def sendMessageOut(self, msg):
 
        self._send(msg) #, channel=5) #### fix this 
    
        
    def sendOutVolume(self, vol=100):
        '''
        mido.Message('control_change', channel=..., control=7))
        Channel volume
        DOES NOT WORK 
        '''
        m=self._mido
        message=m.Message('control_change', channel=self._midiChannel_out, control=7, value=vol)
        print("Output volume set to: ", vol)
        print("on channel: ", self._midiChannel_out)
        
        self._send(message) 

    def sendOutVolumeExp(self, vol=100):
        '''
        mido.Message('control_change', channel=..., control=7))
        Channel volume
        DOES NOT WORK 
        '''
        m=self._mido
        message=m.Message('control_change', channel=self._midiChannel_out, control=11, value=vol)
        print("Output expression volume set to: ", vol)
        print("on channel: ", self._midiChannel_out)     
        self._send(message)
        
    def sendAllSoundOff(self):
        """
        send note_off CC to all 16 channels ....
        """
        print("sending ALL_SOUND_OFF Control message")
        
        for chan in range(16):
            m=self._mido.Message('control_change', channel=chan, control=CCvalues.ALL_SOUND_OFF)
            self._send(m) 
        
    def sendAllNotesOff(self):
        """
        send note_off CC to all 16 channels ....
        """        
        for chan in range(16):
            m=self._mido.Message('control_change', channel=chan, control=CCvalues.ALL_NOTES_OFF)
            self._send(m) 
            
            #yield self._send(m) #is yield needed?
            
    def InportsEmty(self):
        ports=[self._inPortBass, self._inPortControlButtons]
        return all(i is None for i in ports)
        
        
    def sendProgamChange(self, program, channel):
        # sent to out port
        #  return Mido.Message('control_change', channel=self.channel, control=self.control, value=self.value, time=self.time)
        #        
        
        msg=self._mido.Message(MidimsgType.programchange, channel=channel, program=program) 
        if not self._outPort: print("output port not selected!")
        try:
            self._outPort.send(msg)
        except Exception as e:
            print("error - sendProgamChange: " + str(e))
        
        return program
            
        
    def report(self):
        print('\n')
        print(" --- Midi Layer Report --- ")
        print("Midi channel out: ", self._midiChannel_out)
        print("Midi channel control: ", self._midichannel_controls)
        print("Midi channel bass: ", self._midichannel_bass)
        
        
    def printMidiChannels(self):
        
        midi=self
        s = f"""midichannels:
        midi out: \t\t\t {midi._midiChannel_out}  
        midi bass in: \t\t {midi._midichannel_bass} 
        midi ctrl+chords in: {midi._midichannel_chords_controls}"""
        print(s)
    
        
    def setOutPort(self, port):
        self._outPort = port
    
        
 
        
    def playChord(self, global_Chord : List[int], global_root : int): 
        """ 
        The goal is send the chord indexes to midi out port
        recall , we are using chords indexes

        """
        
        print("*playchord, ch: ", self._midiChannel_out)
        
        #deepcopy needed?
        notes= copy.deepcopy(global_Chord)  
        root = copy.deepcopy(global_root)
        
        offset = self._offset
    
        notes=list(map(lambda x: x + root-offset, notes))
        
        print("notes: ", notes)
        print("global_Chord: ", global_Chord)
        print("global_root: ", global_root)
        
        
        
        for note in notes:
            message=self._mido.Message(MidimsgType.note_on, channel=self._midiChannel_out, note=note)
            self._send(message)
        
        #turn the chord off    
        time.sleep(self._chordLength)    
        for note in notes:     
            self._send(self._mido.Message(MidimsgType.note_off, channel=self._midiChannel_out, note=note))    
        
    
    #def sendMessageOut(self, msg): self._send(msg) #, channel=5) #### fix this 
        
        
    
    def startLoop(self):     
        """ 
        we loop on input ports only 
        """
        def messageloopEmpty():
            return all(i is None for i in ports)
        
        def removeUnusedPorts(ports):
            return [i for i in ports if i != None] #remove None, or ports not in use
             
        ports=[self._inPortChordButtons, self._inPortBass, self._inPortControlButtons]
        ports=removeUnusedPorts(ports)
 
        print('\n Engage in message loop: ')
        try:
            for port in ports:
                print("{} {}".format('\t *', port.name[:-1].ljust(30))) # "is open - "# + str(c)))
        
        except Exception as e:
            print("error - function startLoop: " + str(e))
                
       
        if messageloopEmpty():
            print("no input devices available message-polling, returning: ", ports)
            
            return False
            
        while True:   #loop is engaged
            for port in ports: 
                port.poll
                
    
    def startLoop_keyboardlistener(self, _callback, midi, Misc, session: SessionMain):     
        """ 
        we loop on input ports only 
        """
        def messageloopEmpty():
            return all(i is None for i in ports)
        
        def panic():
            print("*** PANIC ***")
            self.sendAllNotesOff()
            
        
        def removeUnusedPorts(ports):
            return [i for i in ports if i != None] #remove None, or ports not in use
             
        ports=[self._inPortBass, self._inPortControlButtons]
        ports=removeUnusedPorts(ports)
 
        print('\n Engage in message loop: ')
        try:
            for port in ports:
                print("{} {}".format('\t *', port.name[:-1].ljust(30))) # "is open - "# + str(c)))
        
        except Exception as e:
            print("error - function startLoop: " + str(e))
                
       
        if messageloopEmpty():
            print("no input devices available message-polling, returning: ", ports)
            _callback() #calls the destructor
            
            
        while True:   #loop is engaged
            if keyboard.read_key() == "q": # q=quits
                _callback()      # destructor
            
            if keyboard.read_key() == "p": # all notes off -  TEST THIS 
                panic()
                
            
            if keyboard.read_key() == "t": # t=test (test-tone)
                midi.sendOutVolume(vol=100) 
                midi.testOut()      #not working in test while running 
                #midi.sendOutVolume(vol=0) 
            
            if keyboard.read_key() == "n": #new chord page
                print("new chord palette !")
                pass
                
            if keyboard.read_key() == "i": #list info about controls 
                Misc.registeredControls(glob.Globals.controls)
                session.report()
                
                
                
            # - - - - - - - -  - - - - - - - - - - - - - - 
            for port in ports: 
                port.poll()  
                
        
    #midicom
    def setinPort_bass(self, port, name, callbackfunction=None):
        self._inPortBass=port
        self._inPortBass_name=name
    
        print("bass input assigned to: ", self._inPortBass_name)
        
        try:   
            self._inPortBass.callback = callbackfunction
        except Exception as e:
            print("error - setinPort_bass" + str(e))
    
    def setinPort_chordButtons(self, port, name, callbackfunction=None):
        self._inPortChordButtons = port 
        self._inPortChordButtons_name=name
        print("chord input assigned to: ", self._inPortChordButtons_name)
        try:     
            self._inPortChordButtons.callback = callbackfunction
        except Exception as e:
            print("error - setinPort_chord" + str(e))

    def setinPort_controlButtons(self, port, name, callbackfunction=None):
        self._inPortControlButtons = port 
        self._inPortControlButtons_name=name
        print("control input assigned to : ", self._inPortControlButtons_name)
        
        try:     
            self._inPortControlButtons.callback = callbackfunction
        except Exception as e:
            print("error - setinPort_control" + str(e))        
            
        
        
    def testOut(self, velocity=100):
        '''
        play 4 tones to check for sound
        '''
        notes=[0,4,7,12]
        notes=list(map(lambda x: x + 64, notes))
   
        for note in notes:
            message=self._mido.Message(MidimsgType.note_on, channel=self._midiChannel_out, note=note, velocity=64)
            self._send(message)
            time.sleep(0.2)
            self._send(self._mido.Message(MidimsgType.note_off, channel=self._midiChannel_out, note=note))
        
        print("*** tones are playing *** channel: "    , message.channel+1)
        time.sleep(0.5)
 
    def _send(self,   message): #
        """
        the message must be a mido.Message()
        """
        p=self._outPort
        try:
            p.send(message)
        except Exception as e:
            print("Error in send: " + str(e))
            return
 
