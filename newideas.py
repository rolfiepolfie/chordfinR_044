# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 08:16:24 2023

@author: rolfe
"""


# class OuterClass:
#     def __init__(self):
#         self.outer_data = "Outer data"
#         self.inner_instance = self.InnerClass()

#     def show_info(self):
#         print("OuterClass data:", self.outer_data)
#         print("InnerClass data:", self.inner_instance.inner_data)

#     class InnerClass:
#         def __init__(self):
#             self.inner_data = "Inner data"
            
#         def show_inner_info(self):
#             print("InnerClass data:", self.inner_data)

# # Creating an instance of OuterClass
# outer_instance = OuterClass()

# # Accessing data from OuterClass and InnerClass
# outer_instance.show_info()

# # Accessing data from a specific InnerClass instance
# inner_instance = outer_instance.InnerClass()
# inner_instance.show_inner_info()

# # Accessing InnerClass using the instance of the OuterClass
# outer_instance2 = OuterClass()
# inner_instance2 = outer_instance2.inner_instance
# inner_instance2.show_inner_info()

# In this example, there is an `OuterClass` that has an `InnerClass` nested within it. We create instances of both classes and access their data. The `outer_instance.show_info()` method shows data from both classes, while the `inner_instance.show_inner_info()` method shows data only from the `InnerClass`.





    class ghostBass(Control):
        '''
        we need several notes , an octave ....
        
        here we need an extra keyboard or similar to play silent bass-notes
        
        it will not be used often , the effort is:
            
            input a different bassnote for the chord (silent) 
            while you are playing another (loud) bassnote 
        
        '''
        
        def __init__(self, note_cc): #make constructor on all classes?
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')

            """
            Freeze, means that the bass input do not change the root 
            of the cord
            These Controls classes got a optional constructor, but also have the 
            note_cc=value as a default value 
            """
            self.name = "ghostBass_control - " + self.__name__
            self.msgtype=[MidimsgType.note_on, MidimsgType.note_off]
            self.note_cc=note_cc
            self.action=Actiontype.momentary

   
        def function(self, arg=None):
            
            print("evoked: ", self.name)
            
            
            
            

class CommentsIdeas:
    '''
    
    # new idea: make a function: change chord function codepage
    # exp: a device get a new selection of chords 2 -3 of them should be enough
    
    # use logging instead of print 
    
    # make a check function, iterating trough all functions in a session
    # reporting if a control_function needs a listener() or other functionalities 
    
    # launchkey pad's got aftertouch ... poly and channel
    
    # -- global objects, later to be compiled into a session object     
    
    
    #typing.Callable is the right hint for a callback.
    #Also see the Callable section of PEP 484:
    #Frameworks expecting callback functions of specific signatures 
    # might be type hinted using Callable[[Arg1Type, Arg2Type], ReturnType]
    # from typing import Callable
    # def my_function(func: Callable):
        
    
    
    ''' 
    
    
    # #def getControlArray_chordUse(self, Chords):
    #     '''
    #     Use this for setting up the device as a "chord input"
    #     we got 6+ chord qualities , can have another live logic 
    #     with the minor and add7 on the other 
    #     + make a function for importing several chord-templates 
        
    #     ### fcb chords - conclusion 17.01
    #     #### C_maj,   C_aug,  Cdim,   ,C6,      C9
    #     #### C_major, C_sus2, C_minor, C7_minor, C7    
    #     # in addition functions: root_freeze , add7,  convertMinor
        
    #     Chord template-1
    #     1-2-3-4-5-6
        
    #     1.major
    #     2.minor
    #     3.sus2
    #     4.septim_minor
    #     5.maj7
    #     6.dim
    #     ##### 7.6'th - not much used , make alternative template ?
        
        
    #     live-logic nr2
    #     -------------------------------------------------------------------
        
    #     Control
    #     1-2-3-4-5-6
    #     maybe sustain on nr1? 
    #     1. root_on/off
    #     2. minor_convert
    #     3. add7
    #     4. add7_sharp
    #     5. extra control 1
    #     6. extra control 2
        
    #     -------------------------------------------------------------------
        
    #     app name: Live Logic Midi control 
    #     notes are: 12, 14, 16, 17, 19, 21 - pr06.07.23
    #     '''
        
    #  "   chords=[Chords.major([12]), Chords.minor([14]),Chords.sus4([16]),
    #  "           Chords.minor7([17]), Chords.maj7([19]), Chords.dim([21])]
        
        
    #  "   return chords        
    
