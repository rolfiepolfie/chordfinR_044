# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 11:10:45 2023

@author: rolfe
"""

from utilities import MidimsgType
import mido

class Midimess:
    def __init__(self, msg):
    
        self.type = msg.type
        
        # future: take meta.messages into account ... (stored into midi.files) 

        if msg.type == 'note_on' or msg.type == 'note_off':
            self.channel = msg.channel
            self.velocity=msg.velocity
            self.note = msg.note
        
        if msg.type == 'control_change':
            self.control=msg.control
            self.value =msg.value
            self.channel = msg.channel
            
        if msg.type == 'program_change':
            pass
        
        
        if msg.type == 'clock': # needed?
            pass
        
        
    def toMidoMsg(self): 
        '''
        only notes and controls are handled 
        '''
            
        if self.type =='control_change':
            return mido.Message('control_change', control=self.control, value=self.value)
        
        if self.type == self.isnoteOn(self):
            return mido.Message('note_on' , control=self.note, velocity=self.velocity)
            
        if self.type == self.isnoteOff(self):
            return mido.Message('note_off' , control=self.note, velocity=self.velocity)    
        
        else:
            return None
        
    def isnoteOn(self): return self.type == MidimsgType.note_on and self.velocity > 0
    def isnoteOff(self): return self.type == MidimsgType.note_on and self.velocity == 0 or self.type == MidimsgType.note_off
      
    def isControlChange(self): return self.type == MidimsgType.controlchange
    #def isProgramChange(self): return True  #finish this 
    
    def isClock(self): return self.type == 'clock'
    
    def totext(self):
        
        if self.type == 'control_change':
            #if self.control==0: return "" #sensor fcb bug
            return "{} \t control_change:{} ch:{} value:{}".format("CC", self.control, self.channel, self.value)
        
        if self.type == 'note_on' or self.type == 'note_off':
            return "{} \t note:{} ch:{} vel:{}".format(self.type, self.note, self.channel, self.velocity)
        
        
        else: 
            return "unsup message: " + str(self.type) #enable this line if you want to show unnsop messages
            
