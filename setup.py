# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 11:27:42 2023

@author: rolfe
"""


from controls import Controls # for type hints
from chords import Chords # for type hints

#from globalvars import Globals

class SetupBlacstarController():
    
    controlarray = []
    '''
    This controller got 6 knobs ...
    last time used set to ch:16
    
    06.07.23 - the unit was programmed:
    All note_on/off +  sysex data=(0,0,116,1,0,77,67,1,0,70,1,0,6) 

    
    # 12-14-16-17-19-20(cc) -- programmed 24/7
    
    # the two external inputs are only CC
    # values EXP2 = CC 22
    # EXP1 = CC 21
    
    Everything MIDI ch 16
        
    '''
    
    '''
    note_off 	 note:16 ch:15 vel:0
    
    CC 	 control_change:21 ch:15 value:74
    '''
    
    '''
    ###            1       2        3       4        5      6
    ###           maj7   sept7    major   minor   Sus2    minor7  
    ###
    ###                              
    ###            
    ### alt              minor7   slash    7      sus4                      
    ###
    ### alternative for sept7 = slash accord F/D
    
    '''
    
    
    def __init__(self, controls: Controls , chords : Chords, midi, callbackLive):
        
        # we keep within the class-member style, not instances (Chords structure)
        # static member do not need self... 
        
        # set up chord structure 
    
        maj7 = chords.maj7
        maj7.alternations  = [None]
        
        major=chords.major
        major.alternations = [chords.cm7_plus_2]
        
        sus2 = chords.sus2
        sus2.alternations = [chords.sus4]
        
        sept7 = chords.normal_7th
        sept7.alternations = [chords.nine9] # or minor7
        
        minor = chords.minor
        minor.alternations = [chords.minor7]
        
        minor7 = chords.minor7
        minor7.alternations = [None]
        

        # chords
        send_maj7_note      = controls.sendChord_Note([12],     maj7,   midi)
        send_sept7_note     = controls.sendChord_Note([14],     sept7,  midi)
        send_major_note     = controls.sendChord_Note([16],     major,  midi)
        send_minor_note     = controls.sendChord_Note([17],     minor,  midi)
        send_sus2_note      = controls.sendChord_Note([19],     sus2,   midi)
        send_minor7_note    = controls.sendChord_Note([20],     minor7, midi)
        
        
        # controls
        alternate_cc = controls.alternateChord_CC([22], midi) #uses global chord reference
        freeze_cc = controls.freezeroot_CC([21],        midi) #we're listening to note-messages by default       
        
        sustain_trig_call = controls.sustain_trig_a_control_CC(midi)
        
        #activates or reacts to controller nr 1 ... on the bass device ...
        trigControl1 = controls.trig_a_control_Nr1_CC(midi)
        
        
        trigControl5 = controls.trig_a_control_Nr5_CC(midi)
        trigControl5.attachOutputCallback(callbackLive) #<-testing callback
        
        
        c=[]
        c.append(send_maj7_note)
        c.append(send_sept7_note) 
        c.append(send_major_note) 
        c.append(send_minor_note) 
        c.append(send_sus2_note) 
        c.append(send_minor7_note) 
        c.append(alternate_cc) 
        c.append(sustain_trig_call)
        c.append(trigControl1)
        c.append(trigControl5)
        #c.append(freeze_cc)
        
        self.controlarray = c
    
    