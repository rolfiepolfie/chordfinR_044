# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 15:07:38 2023

@author: rolfe
"""

from typing import List

#from chords import Chord
#from midicom import MidiComm

#from config import glob_midi

#from chordbug_v_1043 import midi #importing an INSTANCE and used in lgobally ...??

# rebrand midi to glob_midi 


class Globals:
    '''
    Only one instance of this is should be made 
    
    This class contains variables utilized during a live session
    these are read before a live session and not supposed to be serialized
    '''    

    chord_current = [] # the one chord currently being played are referenced here 
    
    global_chord_root = 64      # bass note index
        
    global_bassdown = False     # bass note is down/up = TRUE/FALSE
    
    controls = []               # being invoked during session,usually fixed
    
    global_Control_disable_chord_root = False # this is a control 
    
    @classmethod
    def playChord(cls, midi):   #check midi for None ? 
        
        midi.playChord(cls.chord_current,  cls.global_chord_root)


# Class methods are methods that are called on the class itself, 
# not on a specific object instance. Therefore, it belongs to a class level, and all class instances share a class method.


'''



Message 
Stream  -------- | intercept messages , listener| -----------Evoke a control 


  '''      
        
def getClassnamefromInstance(instance): return instance.__class__.__qualname__
    

