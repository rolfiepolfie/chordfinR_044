# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 11:12:41 2023

@author: rolfe
"""


class Ports:
    """         
    """
    def __init__(self, mido):
        
        # a port corresponds to a physical device
       
        self._inPort_bass_name=None
        self._inPort_chords_name=None
        self._inPort_control_name=None
        
       
        self._inPort_bass = None
        self._inPort_chord = None
        self._inPort_control = None
        
        self._outPort = [] #Fix
        self._inport_piano = None # thinking of recieving sustain-pedal controls
        self._outputNames = mido.get_output_names()
        self._inputNames = mido.get_input_names()
        self._mido=mido
        
    def classname(self): return __class__.__name__

    
    #before using these , make sure they are not None ....
    def bassIsOpen(self):
        return not self._inPort_bass.closed
    
    def controlIsOpen(self):
        return not self._inPort_control.closed
    
    def chordIsOpen(self):
        return not self._inPort_chord.closed
        
        
    def report_devices(self):
          
            print(" --- OUTPUTS --- ")
            for i in self._outputNames:
                print('{} - {}'.format(i[:-1].ljust(30), "index: " + i[-1]))
                
            print('\n')       
            
            print(" --- INPUTS --- ") 
            for i in self._inputNames:
                print('{} - {}'.format(i[:-1].ljust(30), "index: " + i[-1]))
                
            print('\n')
            

    def report(self): 
        #print("report_port_status")
        
        # these lists may got devices not assigned, they will have a None value 
       
        ports = [self._inPort_bass, self._inPort_control, self._outPort]
        #print("all ports: ", ports)
        #port_names=[self._inPort_bass_name, self._inPort_chords_name, self._inPort_control_name, "outname"]
        
        #remove entries with None values (None = not assigned devices)
        #port_names=[i for i in port_names if i != None]
        ports=[i for i in ports if i != None]
        #print("all ports which is not None: ", ports)

        
        print("\n - list port status -")  
        try:
            for i, port in enumerate(ports):
                
                if not port.closed:
                    
                    print("{} - {} {}".format(i, port.name[:-1].ljust(30), "\t open"))
                else:
                    
                    print("{} - {} {}".format(i, port.name[:-1].ljust(30), "\t closed "))
                    
        except Exception as e:
            print("error - report_port_status: " + str(e)) 
            
        print('\n')
        
    
    
    def checkIfPortsEmpty(self):
        """ 
        Detect if there are no ports.
        The purpose is to warn the user/app that there is no point going further
        """
        input_names = self._inputNames
        return len(input_names) == 0
    
    def openInport_bass(self, index):
        input_names = self._inputNames
            
        try:
            self._inPort_bass_name = input_names[index]
            self._inPort_bass=self._mido.open_input(input_names[index]) 
        except Exception as e:
           print("error - openInport_bass - : " + str(e)) 
           
           
    def openInport_control(self, index):
        
        input_names = self._inputNames
        try:
            self._inPort_control_name = input_names[index]
            
            #if not self._inPort_control.closed: print("port control is already open!!")
            self._inPort_control=self._mido.open_input(input_names[index])             
        except Exception as e:
           print("error - openInport_controls - : " + str(e)) 

    
    def openOutPort(self, nr): #opens everything at the moment 
        out_names=self._outputNames
        try:
            name = out_names[nr]
            self._outPort = self._mido.open_output(name)            
        except Exception as e:
            print("error - openOutPort: " + str(e))
    
    def closeAllPorts(self):
        #global original, ports
        original=[self._outPort, self._inPort_chord, self._inPort_bass, self._inPort_control]
        #print("closeAllPorts - all ports : ", original)
        ports = [i for i in original if i is not None] 
        #print("ports not None is: ", ports)
        try:         
            for i , port in enumerate(ports): 

                port.close()
                
                    
        except Exception as e:
            print("closeallports: - error: "+ str(e))
            #return
            #print("ports closed")
        
    