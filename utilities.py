# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 11:04:21 2023

@author: rolfe
"""

from PIL import Image

#display picture 
def allchords():
    with Image.open('allchords.png') as img:
        img.show()
    
    

### small classes and datatypes 

class MidimsgType():  
    note_on = 'note_on'
    note_off = 'note_off' 
    controlchange = 'control_change'
    programchange = 'program_change'
    sysex_data = 'sysex_data'
    pitchwheel = 'pitchwheel'
    aftertouch = 'aftertouch'
    
class Actiontype:
    momentary = 'momentary' # or temporary, remove effect when pedal is up
    toggle = 'toggle'
    other = 'other'



class CCvalues:
    """
    defines values that follows a CC (Control Change) message (CC, value)
    """
    ALL_SOUND_OFF = 120 #check midi spec for this one 
    RESET_ALL_CONTROLLERS = 121
    ALL_NOTES_OFF = 123
   
    # 122 Local Control On/Off  -  interrupt the internal control path between the keyboard and the sound-generating circuitry
    # 123 All Notes Off
    # 124 Omni Mode Off
    # 125 Omni Mode On
    # 126 Poly Mode On/Off
    # 127 Poly Mode Mono Off

    #https://www.lim.di.unimi.it/IEEE/MIDI/SOT0.HTM#Local

class utils:
    def availableCC():
        s="""
        These is free to use Control Change Messages ...
        """
        print(s)
        print("CC 3")
        print("CC 9")
        print("CC 14-15")
        print("CC 20-31")
        print("CC 85-87")
        print("CC 89-90")
        print("CC 102-119")
    
    # def showkeyb():
    #     img = mpimg.imread('keyb.png')
    #     plt.imshow(img)
    #     plt.show()




class Misc():
    
    
    def printMainMenu():
        print(" \n NB! if using same midi-channel on both chord+controls")
        print("do not use the same MIDI-notes or CC messages \n")
        
        print("q - quits")
        print("p - panic")
        print("t - test")
        print("i - session info")
        print('n - new page with chords')
        
        
        
    #change to live session report ...
    def registeredControls(controls):
        """
        Prints all the chords and controls loaded in this session 
        
        """

        print("\n")
        print("--- CONTROLS registered for controller messages this session ---")
        for c in controls:     
        
            print("control name: \t", c.name())   
            print("\t triggered: \t", c._triggers)
            print("\t note_cc: \t\t", c._cc_note)

            #print("\n")
        
        #print("\n")
  
    
    def classname(self): return __class__.__name__
    
    #def isControlChange(msg):
    #    return msg.type == 'control_change'
    
    #def isNote(msg):
    #    return msg.type == 'note_on' or msg.type == 'note_off'
    #    #return msg.type in ('note_on', 'note_off') # alternative
    
    def undefined_CC():
        t1=" Undefined MIDI CC List"

        t2="CC 3 "
        t3="CC 9 "
        t4="CC 14-15 "
        t5="CC 20-31 "
        t6="CC 85-87 "
        t7="CC 89-90 "
        t8="CC 102-119 "
        return t1+t2+t3+t4+t5+t6+t7+t8
        
        
    def listClassMembers(theObject):
        
        for property, value in vars(theObject).items():
            print(property, ":", value)
    
    def printUserprotertiesClass(clas):
        print([ m for m in dir(clas) if not m.startswith('__')])
    
    def clearSpyderTerminal():
        print("\033[H\033[J")  
        
    def printLogo():
        print('')
        print('───╔╗──♬─────╔╗╔═╗─────╔╦═══╗')
        print('───║║────────║║║╔╝─────║║╔═╗║')
        print('╔══╣╚═╦══╦═╦═╝╠╝╚╦╦═╗╔═╝║╚═╝║')
        print('║╔═╣╔╗║╔╗║╔╣╔╗╠╗╔╬╣╔╗╣╔╗║╔╗╔╝')
        print('║╚═╣║║║╚╝║║║╚╝║║║║║║║║╚╝║║║╚╗')
        print('╚══╩╝╚╩══╩╝╚══╝╚╝╚╩╝╚╩══╩╝╚═╝')
    

    def printTitle(mido, rt, sys, ver, title): # the app's name .... 
 
     ### a testing function ... shall be removed and replaced with Chord-Service  
        print("Title: \t\t\t\t" , title)
        print("Python installed: \t", str(sys.version_info[0]) + '.' + str(sys.version_info[1]))
        print("Mido version:   \t", mido.__version__)
        print("Backend version RT:\t", rt.__version__)
        print("Chordial version: \t", ver)
     
    def scaleinfo():
        pass
        
        
    #                 Interval Reference
    #         C played with ... is a(n) ...
    #         C Db D  Eb E  F Gb G Ab A  Bb B  C
    #         1 m2 M2 m3 M3 4 b5 5 m6 M6 m7 M7 8
    #         | |  |  |  |  | |  | |  |  |  |  Octave
    #         | |  |  |  |  | |  | |  |  |  Major Seventh
    #         | |  |  |  |  | |  | |  |  Minor Seventh
    #         | |  |  |  |  | |  | |  Major Sixth
    #         | |  |  |  |  | |  | Minor Sixth
    #         | |  |  |  |  | |  Perfect Fifth
    #         | |  |  |  |  | Flatted Fifth (Or Augmented Fourth)
    #         | |  |  |  |  Perfect Fourth
    #         | |  |  |  Major Third
    #         | |  |  Minor Third
    #         | |  Major Second
    #         | Minor Second
    #         Unison
            
    #              Major triad  M3\m3
    #              Minor triad  m3\M3
    #         Diminished triad  m3\m3
    #          Augmented triad  M3\M3
    
    #        Major Seven  M3\m3\M3
    #     Dominant Seven  M3\m3\m3
    #        Minor Seven  m3\M3\m3
    # Minor (Major Seven) m3\M3\M3 
     
        
     
# Classification of MIDI messages:

#                                                ----- voice messages
#                    ---- channel messages -----|
#                   |                            ----- mode messages
#                   |
# MIDI messages ----| 
#                   |                            ---- common messages
#                    ----- system messages -----|---- real-time messages
#                                                ---- exclusive messages     
     
     
     
    def overviewChords():
        return """
                    https://www.pianochord.org/c5.html
            
            C - C major (C△)
            Cm - C minor
            C7 - C dominant seventh
            Cm7 - C minor seventh
            
            Cmaj7 - C major seventh (C△7)
            CmM7 - C minor major seventh
            
            C6 - C major sixth
            Cm6 - C minor sixth
            C6/9 - C sixth/ninth (sixth added ninth)
            
            C5 - C fifth   (interval - 2 notes)
            
            C9 - C dominant ninth
            Cm9 - C minor ninth
            Cmaj9 - C major ninth
            
            C11 - C eleventh
            Cm11 - C minor eleventh
            
            C13 - C thirteenth
            Cm13 - C minor thirteenth
            Cmaj13 - C major thirteenth
            
            Cadd - C add
            C7-5 - C seven minus five
            C7+5 - C seven plus five
            Csus - C suspended
            
            Cdim - C diminished (C°)
            Cdim7 - C diminished seventh (C°7)
            Cm7b5 - C minor seventh flat five (Cø)
            
            Caug - C augmented (C+)
            Caug7 - C augmented seventh
        """


#from sessionclass import SessionMain

class AllMidoMessages:
    
    # rewrite mid.new -> mido.Message

    # mido.Message('note_off', channel=0, note=0, velocity=0, time=0)
    # mido.Message('note_on', channel=0, note=0, velocity=0, time=0)
    # mido.Message('polytouch', channel=0, note=0, value=0, time=0)
    # mido.Message('control_change', channel=0, control=0, value=0, time=0)
    # mido.Message('program_change', channel=0, program=0, time=0)
    # mido.Message('aftertouch', channel=0, value=0, time=0)
    # mido.Message('pitchwheel', channel=0, value=0, time=0)
    # mido.Message('sysex', data=(), time=0)
    # mido.Message('undefined_f1', time=0)
    # mido.Message('songpos', pos=0, time=0)
    # mido.Message('song', song=0, time=0)
    # mido.Message('undefined_f4', time=0)
    # mido.Message('undefined_f5', time=0)
    # mido.Message('tune_request', time=0)
    # mido.Message('sysex_end', time=0)
    # mido.Message('clock', time=0)
    # mido.Message('undefined_f9', time=0)
    # mido.Message('start', time=0)
    # mido.Message('continue', time=0)
    # mido.Message('stop', time=0)
    # mido.Message('undefined_fd', time=0)
    # mido.Message('active_sensing', time=0)
    # mido.Message('reset', time=0)
    
    pass   

# https://users.cs.cf.ac.uk/dave/Multimedia/node158.html




import os

#must be completed , a fun that show which file(s) your keywords are found 
def searchfiles(word):
  
    
    folderpath  = r'C:\Users\rolfe\Desktop\chord_program_code\code'
    print(folderpath)
    
    # iterate each file in a directory
    
    
    for(path, dirs, files) in os.walk(folderpath, topdown=True):
        for filename in files:
            filepath = os.path.join(path, filename)
            with open(filepath, 'r',  errors="ignore") as currentfile:
                for line in currentfile:
                    if word in line:
                        print('Found the word in ' + filename + ' in line ' + line)
                        

      


    
'''
callbackBass -  control_change channel=3 control=1 value=19 time=0
callbackBass -  control_change channel=3 control=1 value=17 time=0
callbackBass -  control_change channel=3 control=1 value=16 time=0
callbackBass -  control_change channel=3 control=1 value=15 time=0
callbackBass -  control_change channel=3 control=1 value=14 time=0
callbackBass -  control_change channel=3 control=1 value=13 time=0
callbackBass -  control_change channel=3 control=1 value=11 time=0
callbackBass -  control_change channel=3 control=1 value=10 time=0
callbackBass -  control_change channel=3 control=1 value=9 time=0
callbackBass -  control_change channel=3 control=1 value=7 time=0



callbackBass -  control_change channel=3 control=64 value=127 time=0
callbackBass -  control_change channel=3 control=64 value=0 time=0
callbackBass -  control_change channel=3 control=64 value=127 time=0
callbackBass -  control_change channel=3 control=64 value=0 time=0
callbackBass -  control_change channel=3 control=64 value=127 time=0



'''  