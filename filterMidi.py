# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 11:44:03 2023

@author: rolfe
"""


class Filter:
    
    # filter is calling the callbacks from the parameters in the constructor
    # the hardware is  connected  via the filterMidi instance
    ## recall:  ui.askuseropenports(rv, midi, filterMidi, ports)
    # the filter decides if it shall trigger the callbacks 
    
    '''
    1. Mido system first calls these functions in __init__  parameter
    2. Functions are then filtered dependent on their parameter 
    3. These function is then called and indicated with an _
    
    This filter handles Midi input only
    This filter only trigger callbacks with 
    midi messages with the correct channel property value
    

    '''    
    def __init__(self, callback_bass, callback_controlchord): 
        
        self._cbBass=callback_bass
        self._cb_controlchord=callback_controlchord
    
        self._midichannel_bass = -1
        self._midichannel_controls = -1
        self._midichannel_out = -1

        self._activated=False

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

    
    def activate(self):
        self._activated=True
    
    def deactivate(self):
        self._activated=False
        
    
    def filteroutBass(MidimsgTypes):
        '''
        Messages are removed, but messages with correct channel is triggered
        add an array or class properties woth datatyps to ignore 
        in the message stream 
        '''
        pass
    
    
    def filteroutControlChord(MidimsgTypes):
        '''
        add an array or class properties woth datatyps to ignore 
        in the message stream 
        '''
        pass
    
    def report(self):
 
        print('\n')
        print('--- Midi Filter Report ---')
        print("Midi channel bass: ", self._midichannel_bass)
        print("Midi channel control: ", self._midichannel_controls)
        
        if self._activated:
            print("* filter  is activated ---")
        else:
            print("* filter NOT activated ---")
            
  
          
    def _onlychannelmessages(self, msg):
        try:
            msg.channel #access attribute to check 
            return True
        except AttributeError:
            return False

    #This trigs the callback for bass 
    def trigBass(self, msg):
        # returns true of message contains channel property
        # here we filter out and make sure all messages 
        # triggered got a channel property
        #print('filter - trigBass: ', msg)
        
        #if filter is deactivated we call the callback anyway and escape
        if self._activated == False: 
            self._cbBass(msg) #calling callback function
            return
        
        
        if not self._onlychannelmessages(msg): 
            print("non cannel msg ignored: ", msg)
            return 
                
        if msg.channel == self._basschannel: 
            self._cbBass(msg) #calling callback function
            return
            
     #This trigs the callback for control and chord        
    def trigControlChord(self, msg):
        #print('filter - trigControlChord: ', msg)
        
        #if filter is deactivated we call the callback anyway and escape
        if self._activated == False: 
            self._cb_controlchord(msg) #calling callback function
            return
            
        if not self._onlychannelmessages(msg): 
            print("non channel msg ignored ", msg)
            return 
        
        if msg.channel == self._controlChordChannel: 
            self._cb_controlchord(msg) #calling callback function
            return
    
 ### messages triggered always have the channel property   
 
