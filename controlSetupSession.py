# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 00:47:16 2023

@author: rolfe
"""


class BlackStar(): #is this needed?
    '''
    store info about the hardware device
    
    '''
    def getMidiMessages(self): #notes and CC in an array or dict that will be sent 
        class typ:
            message=''
            note_cc=0
            
            
        m1= typ()
        m1.message=['note_on', 'note_off']
        m1.note_cc=[21]
        
        
        m2= typ()
        m2.message=['control_change']
        m2.note_cc=[22]


        return [m1, m2]        

        

        
    '''    
        One easy way to achieve this is by using defaultdict:

from collections import defaultdict

data_dict = defaultdict(list)
All you have to do is replace

data_dict[regNumber] = details
with

data_dict[regNumber].append(details)
        
        
        pass
    
'''
class ControlSetupSession:
    '''
    1. provide chord strucutures or setups 
        that can be selected during session
    
    2. 
    
    '''
    
    class Palette:
        NORMAL1=1
        NORMAL2=2
    
    
    def attacDev(device):
        pass
    
    def _generateControlPaletteSetup1():
        '''
        Normal1 - based Blackstar with 2 pedals
            
        '''
        pass
    
    def _generateControlPaletteSetup2():
        pass
    
    
    def _generateControlPaletteSetup3():
        pass    
    
    
    
    def selectControlPalettes(palette) -> None: #selected during session 
        pass
    
    
    def getCurrentPalette(): # called after a palette i chosen 
       
    
        pass
    
    
###     idea, during session we select a another palette of controls

# attachDev(blackstar)

## ControlSetupSession.selectControlPalettes(Palette.NORMAL2)
# getCurrentPalette

## ControlSetupSession.selectControlPalettes(Palette.NORMAL1)
# getCurrentPalette