# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 10:55:44 2023

@author: rolfe
"""
# rename chordindex -> chordindexes
from chordindex import ChordIndex #chord-notes or notes 


from abc import ABC, abstractmethod

class Chord(ABC): 
    """
    Base class for all user defined chords
    IN USE 
    
    Functions as a common type identificator 
    """
    
    index = None
    name = __qualname__ #move to parent class? No 
    alternations = [None]
    
    # implement abstract methods in future version 
    # the app is dependent on these functions always present 
    
    # @abstractmethod
    # def getNotes(): pass

    # @abstractmethod
    # def getName(): pass

    # @abstractmethod
    # def getAlternations(): pass 

        
class Chords:

    class major(Chord):
        
        index = ChordIndex.C_major
        name = __qualname__ #move to parent class? No 
        alternations = [None]
        
    class sus2(Chord):

        index = ChordIndex.C_sus2
        name = __qualname__
        alternations = [None] # new idea to help algorithm def function(self, arg=None): pass
               
    class sus4(Chord):
        
        index = ChordIndex.C_sus4
        name = __qualname__
        alternations = [ChordIndex.C_sus2] # new idea to help algorithm def function(self, arg=None): pass

    class minor(Chord):

        index = ChordIndex.C_minor
        name = __qualname__
        alternations = [None]

    class normal_7th(Chord):  #not the maj7 or sharped 7

        index = ChordIndex.C_7_major
        name = __qualname__
        alternations = [None]
    
    class normal_6th(Chord):  #not the maj7 or sharped 7

        index = ChordIndex.C_6_major
        name = __qualname__
        alternations = [None]
        
    class maj7(Chord): #sharpen 7th

        index = ChordIndex.C_maj_major
        name = __qualname__
        alternations = [None]
    
    class minor7(Chord):

        index=ChordIndex.C_7_minor
        name = __qualname__
        alternations = [None]

    class dim(Chord):  
            
        index = ChordIndex.C_dim #lacking a 9 at the end , self.index
        name = __qualname__
        alternations = [None] #we could add a seven as major-dim not making sense

    class sus_aug(Chord):

        index= ChordIndex.C_aug
        name = __qualname__
        alternations = [None]
                    
    class nine9(Chord):

        index = ChordIndex.C_9_major
        name = __qualname__
        alternations = [None]
        
    class cm7_plus_2: #d-f-a-c, and take a G in base
    
        index = ChordIndex.D_m7_slash_c
        name = __qualname__
        alternations = [None]
    
        # must freeze the chord ?
        
        
    ## sus 2 + 7 = 9th chord
    
    
    def printall(Object):
        print("\n -- chords class structure, chords that can be invoked if  assigned to a midi message: ") 
        i=0
        for property, value in (vars(Object).items()):
            if not property.startswith('__'): 
                if not property.startswith('printall'): 
                    i=i+1
                    print("{}\t {} ".format(i, property.ljust(15)))
                    
        print('\n')