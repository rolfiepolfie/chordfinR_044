# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 15:51:41 2023

@author: rolfe
"""

class Palette_normal1:
        
    def __new__(cls): return [1,22,3]
        
    
class Palette_normal2:
        
    def __new__(cls): return [11,222,33]

class Palette_advanced1:
         
    def __new__(cls): return [111,2222,3333]



class PaletteSelector():
    
    MAX_VALUE = 126
   
    def __init__(self, controls1 : list, controls2 : list, controls3 : list):
   
        self.arr1 = controls1 # array with controls that evoke chords  
        self.arr2 = controls2
        self.arr3 = controls3
       
        self.palette = self.arr1
       
       
    def palette(self): return self.actual
              
    def _control1(self, param=None):
        self.palette = self.arr1
   
    def _control2(self, param=None):
        self.palette = self.arr2
   
    def _control3(self, param=None):
        self.palette = self.arr3
      
    def scan(self, param : int): #param is some CC message from a callback message
   
        if param in range(0, 40):
            self._control1(param)
           
        if param in range(40, 80):
            self._control2(param)
       
        if param in range(80, __class__.MAX_VALUE):
           self. _control3(param)
                   
        return self.palette            
    
    
normal1=Palette_normal1()
normal2=Palette_normal2() 
advanced=Palette_advanced1()
     
t=PaletteSelector(normal1, normal2, advanced)


#ff=[testrange]
pp=[2,22,33,45, 70, 0, 90, -33]

for p in pp:
    print(t.scan(p))