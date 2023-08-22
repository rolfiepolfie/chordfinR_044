# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 21:37:29 2023

@author: rolfe
"""

from abc import ABC, abstractmethod

############################################################################

class IObserver_Note(ABC):
    
    def __init__(self):
        self._triggers = ['note_on', 'note_off']
        
    def name(self): return self.__class__.__name__  
    
    
    @abstractmethod
    def _execute(self, message, args): pass
        

    @abstractmethod
    def execute(self, message, args): pass

############################################################################
                
class IObserver_CC(ABC):
    
    def __init__(self):        
        self._triggers = ['control_change']
        
    def name(self): return self.__class__.__name__  

    @abstractmethod
    def _execute(self, message, args): pass

    
    @abstractmethod  
    def execute(self, message, args): pass    
    
############################################################################

class IObserver_PC(ABC):
    
    def __init__(self):        
        self._triggers = ['program_change']
        
    def name(self): return self.__class__ .__name__  

    @abstractmethod
    def _execute(self, message, args): pass

    
    @abstractmethod  
    def execute(self, message, args): pass    
    
############################################################################

class IObserver_Sustain(ABC):
    
    def __init__(self):
        self._triggers = ['control_change']
        self._cc_note = [64]
        
            
    def name(self): return self.__class__.__name__  
    
    
    # idea: to call a control trough the callback 
    def attachCallback(self, callbackControl): pass
    
    @abstractmethod
    def _execute(self, message, args): pass
        

    @abstractmethod
    def execute(self, message, args): pass


 ############################################################################

class IObserver_Control_1(ABC):
    
    def __init__(self):
        self._triggers = ['control_change']
        self._cc_note = [1]
        
            
    def name(self): return self.__class__.__name__  
    
    
    # idea: to call a control trough the callback 
    def attachCallback(self, callbackControl): pass
    
    @abstractmethod
    def _execute(self, message, args): pass
        

    @abstractmethod
    def execute(self, message, args): pass   

 ############################################################################

class IObserver_Control_5(ABC):
    
    def __init__(self):
        self._triggers = ['control_change']
        self._cc_note = [5]
        
            
    def name(self): return self.__class__.__name__  
    
    
    # idea: to call a control trough the callback 
    def attachCallback(self, callbackControl): pass
    
    #@abstractmethod
    #def _execute(self, message, args): pass
        

    @abstractmethod
    def execute(self, message, args): pass   


    @abstractmethod
    def _execute(self, trigtype, message, args=None): pass




