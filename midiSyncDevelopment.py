# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 13:24:48 2023

@author: rolfe
"""

import time 

...

#Clock events are sent at a rate of 24 pulses per quarter note. T

#MIDI beat clock differs from MIDI timecode in that MIDI beat clock is tempo-dependent.



#clock (decimal 248, hex 0xF8)
#start (decimal 250, hex 0xFA)
#continue (decimal 251, hex 0xFB)
#stop (decimal 252, hex 0xFC)


# Recall!
# TYROS Midi settings TRANSMIT CLOCK = ON

# Novation-Launchkey-37-MK3 can send MIDI-CLOCK 


# http://little-scale.blogspot.com/2008/05/how-to-deal-with-midi-clock-signals-in.html

class MidiClock:
    byte_midi_start = 0xfa
    byte_midi_stop = 0xfc
    byte_midi_clock = 0xf8
    byte_midi_continue = 0xfb
    
    


play_flag = 0

BPM=120
bpm = BPM
clock_period_in_microseconds = 60_000_000 / (24 * BPM)

# number of seconds in a beat
beat_seconds = 60 / bpm

clocks_per_click =1000 # my wild guess


# number of seconds in a quarter note
quarter_note_seconds = beat_seconds / 4 

# number of seconds in a MIDI clock tick
tick_seconds = quarter_note_seconds / clocks_per_click

# MIDI time to second conversion
seconds = time * tick_seconds



# from MIDO manual , the default cloks pr click = 24
# clocks_per_click 0..255 24

# https://forums.cherryaudio.com/viewtopic.php?t=1534
# Now MIDI clock runs at 24 PPQN so at a
# tempo of 120 BPM there's 120 * 24 / 60 = 48 clocks 
# being sent every second. 3125 / 48 is just over 65. 
# So a clock pulse has to fit in to a window of 65 slots. 
# So there's a a fair amount of jitter even when nothing else is being transmitted.


'''
a very basic MIDI capable sequencer will count 24 'pulses' per quarter note or ppq. A 16 step sequencer would have a 'step' (a 1/16 note) every 6 pulses. The 'clock period' would be the number of microseconds between each individual pulse.
You were on the right track with a timer. When the clock period has elapsed 6 times, the sequencer step increments by 1, wrapping back around at the 16th step.
you can set the clock period of a 24 ppq clock like this:
    
clock_period_in_microseconds = 60000000 / (24 * BPM) # = 24 ppq 
'''

'''
file:///C:/Users/rolfe/Desktop/chord_program_code/MIDI%20sync%20data/Could%20use%20some%20help%20with%20coding%20a%20sequencer%20_%20synthdiy.html

import time
import board
import digitalio
import adafruit_midi

# Set up MIDI input
midi_in = adafruit_midi.MIDIIn(board.MIDI)
clock_msg = adafruit_midi.ControlChange(0, 0x08, 0)

# Set up counter and step list
step_count = 0
steps = [0, 1, 2, 3, 4, 5, 6, 7]

# Loop to read MIDI clock messages and send note messages
while True:
    msg = midi_in.receive()
    if isinstance(msg, adafruit_midi.Clock):
        # Increment the counter on each MIDI clock message
        step_count += 1
        # Check if the counter matches a step in the sequence
        if step_count in steps:
            # Send a note message for the current step
            note_msg = adafruit_midi.NoteOn(0, 60, 127)
            midi_out.send(note_msg)
    # Wait a short time to avoid overwhelming the system with messages
    time.sleep(0.001)
'''





while True:
    for msg1 in input_hw.iter_pending():
        if not msg1.type == "clock":
            print(msg1)

        # Play the note if the note has been triggered
        if msg1.type == 'note_on' or msg1.type == 'note_off' and msg1.velocity > 0:
            out.send(msg1)
            
            

# file:///C:/Users/rolfe/Desktop/chord_program_code/MIDI%20sync%20data/little-scale_%20How%20to%20Deal%20with%20MIDI%20Clock%20Signals%20in%20Arduino.html

#1. Add the following code to the start of the code:
counter = 0
relayPin = 2


#2. Add the following where the code says do something for every MIDI Clock pulse when the sequencer is running":

if(counter < 384):
        counter = counter + 1;
        digitalWrite(relayPin, 1 - (counter / 192));

else:
    counter = 0;


# read about callback midi syncs 
# file:///C:/Users/rolfe/Desktop/chord_program_code/MIDI%20sync%20data/How%20can%20I%20integrate%20Python%20mido%20and%20asyncio_%20-%20Stack%20Overflow.html
# file:///C:/Users/rolfe/Desktop/chord_program_code/MIDI%20sync%20data/Could%20use%20some%20help%20with%20coding%20a%20sequencer%20_%20synthdiy.html
  





  
# syncing your MIDI controller to a MIDI clock signal can improve its accuracy and help it stay in sync with other MIDI devices.
# file:///C:/Users/rolfe/Desktop/chord_program_code/MIDI%20sync%20data/Could%20use%20some%20help%20with%20coding%20a%20sequencer%20_%20synthdiy.html
            

    # #vNew messages are created with mido.new() or mido.Message().
    # #vValid arguments are:

    # mido.new('note_off', channel=0, note=0, velocity=0, time=0)
    # mido.new('note_on', channel=0, note=0, velocity=0, time=0)
    # mido.new('polytouch', channel=0, note=0, value=0, time=0)
    # mido.new('control_change', channel=0, control=0, value=0, time=0)
    # mido.new('program_change', channel=0, program=0, time=0)
    # mido.new('aftertouch', channel=0, value=0, time=0)
    # mido.new('pitchwheel', channel=0, value=0, time=0)
    # mido.new('sysex', data=(), time=0)
    # mido.new('undefined_f1', time=0)
    # mido.new('songpos', pos=0, time=0)
    # mido.new('song', song=0, time=0)
    # mido.new('undefined_f4', time=0)
    # mido.new('undefined_f5', time=0)
    # mido.new('tune_request', time=0)
    # mido.new('sysex_end', time=0)
    # mido.new('clock', time=0)
    # mido.new('undefined_f9', time=0)
    # mido.new('start', time=0)
    # mido.new('continue', time=0)
    # mido.new('stop', time=0)
    # mido.new('undefined_fd', time=0)
    # mido.new('active_sensing', time=0)
    # mido.new('reset', time=0)
    
    
    

# Yes, syncing your MIDI controller to a MIDI clock signal can improve its accuracy and help it stay in sync with other MIDI devices.

# To accomplish this, you'll need to use the incoming MIDI clock signal to keep track of the tempo and then send out MIDI messages accordingly. Here's one approach you could take:

# Use the time.monotonic()
# function to keep track of the time that has passed since the last MIDI clock signal was received.

# When a MIDI clock signal is received, update your tempo value based on the number of clock signals received since the last beat, and reset your timer.

# Use the current tempo value to determine the duration of each step, and send out the appropriate MIDI note message when the timer reaches the appropriate point.

# Here's an example implementation in CircuitPython:
# file:///C:/Users/rolfe/Desktop/chord_program_code/MIDI%20sync%20data/Could%20use%20some%20help%20with%20coding%20a%20sequencer%20_%20synthdiy.html
# import time
# import board
# import usb_midi
# import adafruit_midi
# from adafruit_midi.timing_clock import TimingClock

# midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[0], out_channel=0)
# clock = TimingClock(midi_out=usb_midi.ports[0])

# # Set the initial tempo to 120 BPM
# tempo = 500000
# step_time = 0

# while True:
#     # Wait for a MIDI clock signal
#     clock.receive()

#     # Update the tempo based on the number of clock signals received
#     tempo *= clock.factor
#     if clock.tick_count == 24:
#         # The tempo should be updated every quarter note
#         tempo //= 24
#         clock.tick_count = 0

#     # Calculate the duration of each step based on the current tempo
#     step_duration = tempo / 1000000

#     # Check if it's time to send a note message
#     step_time += step_duration
#     if step_time >= 1.0:
#         # Send a note message
#         midi.note_on(60, 127)
#         step_time -= 1.0
        
        
        
        

# # https://www.reddit.com/r/synthdiy/comments/102kbob/could_use_some_help_with_coding_a_sequencer/


# # https://alsa-devel.alsa-project.narkive.com/hOlNI08p/pyalsa-synchronizing-queue-with-midi-clock-events


# class MidiProcessor(object):

#     def run(self):
#     # This is simplified to only show the general logic
#         while True:
#             events = self.sequencer.receive_events(
#                                 timeout=RECEIVE_TIMEOUT, maxevents=1)
            
#             for event in events:
#                 if event.type == SEQ_EVENT_CLOCK:
#                         self.sync_queue(event)
#                 else:
#                     # do other MIDI processing / routing
#                     pass
                    
    
#     def sync_queue(self, event):
#         """Sync queue tempo to incoming MIDI clock events."""
#         # list to collect the timestamps of the last few ticks
#         lt = self._last_ticks
#         lt.append(time.time())
#         ltlen = len(lt)
        
#         if ltlen > 1:
#             # calculate & set bpm: calculate difference between
#             # the times the last few ticks were received and average
#             # all results
#             avg_delta = sum(
#             [y-x for x,y in zip(lt, lt[1:])]) / (ltlen-1)
#             # tick length is a 24th of a quarter note
#             bpm = round(60 / avg_delta / 24)
        
#         if bpm != self.bpm:
#             self.bpm = bpm
#             self.sequencer.queue_tempo(self.queue,
#             tempo=int(6e7 / self.bpm), ppq=self.ppq)
#             # only remember last 24 received ticks
#             # (length of a quarter note)
#         if ltlen > 24:
#             lt.pop(0)
            
            
#  # https://stackoverflow.com/questions/60182510/mido-how-to-get-midi-data-in-realtime-from-different-ports

           

# import rtmidi as md

# mtcin = md.MidiIn()
# mout = md.MidiOut()
# mtcin.ignore_types(sysex=False, timing=False)
# mtcin.open_port(0)
# mout.open_port(3)
# event_list = [(0,123),(0.13,234,45),(1.5,345,56),(3,14)]
# ind = 0
# timecode = -1
# mout.send_message((0xf0, 0x7f, 127, 6, 2, 0xf7))
# while ind < len(event_list):
#     msg = mtcin.get_message()
#     if msg:
#         timecode += 1
#     if event_list[ind][0] <= timecode/100.0:
#         print event_list[ind][1:]
#         ind += 1
#     time.sleep(0.001)
# mout.send_message((0xf0, 0x7f, 127, 6, 1, 0xf7))
# mout.send_message((0xf0, 0x7f, 127, 6, 0x44, 6, 1, 32, 0, 0, 0, 0, 0xf7))       
            
            
            
#         https://github.com/ElliotGarbus/MidiClockGenerator/releases
            
#         https://github.com/ElliotGarbus/MidiClockGenerator   
            
            
#             https://pypi.org/project/miditime/
            
#         import time
# import rtmidi as md
# mtcin = md.MidiIn()
# mout = md.MidiOut()
# mtcin.ignore_types(sysex=False, timing=False)
# mtcin.open_port(0)
# mout.open_port(3)
# event_list = [(0,123),(0.13,234,45),(1.5,345,56),(3,14)]
# ind = 0
# timecode = -1
# mout.send_message((0xf0, 0x7f, 127, 6, 2, 0xf7))
# while ind < len(event_list):
#     msg = mtcin.get_message()
#     if msg:
#         timecode += 1
#     if event_list[ind][0] <= timecode/100.0:
#         print event_list[ind][1:]
#         ind += 1
#     time.sleep(0.001)
# mout.send_message((0xf0, 0x7f, 127, 6, 1, 0xf7))
# mout.send_message((0xf0, 0x7f, 127, 6, 0x44, 6, 1, 32, 0, 0, 0, 0, 0xf7))    
            

# #https://github.com/ElliotGarbus/MidiClockGenerator/blob/master/main.py


            
# from time import perf_counter, sleep, time
# from multiprocessing import Process, Value, set_start_method, freeze_support
# import mido
# import mido.backends.rtmidi  # required for pyinstaller to create an exe


# class MidiClockGen:
#     def __init__(self):
#         self.shared_bpm = Value('i', 60)
#         self._run_code = Value('i', 1)  # used to stop midiClock from main process
#         self.midi_process = None

#     @staticmethod
#     def _midi_clock_generator(out_port, bpm, run):
#         # print(f'__name__: {__name__}')
#         midi_output = mido.open_output(out_port)
#         clock_tick = mido.Message('clock')
#         while run.value:
#             pulse_rate = 60.0 / (bpm.value * 24)
#             midi_output.send(clock_tick)
#             t1 = perf_counter()
#             if bpm.value <= 3000:
#                 sleep(pulse_rate * 0.8)
#             t2 = perf_counter()
#             while (t2 - t1) < pulse_rate:
#                 t2 = perf_counter()

#     def launch_process(self, out_port):
#         if self.midi_process:  # if the process exists, close prior to creating a new one
#             self.end_process()
#         else:                  # if this is the first time, start flashing the panel led
#             app = App.get_running_app()
#             app.flash_led_on(None)
#         self._run_code.value = 1
#         self.midi_process = Process(target=self._midi_clock_generator,
#                                     args=(out_port, self.shared_bpm, self._run_code),
#                                     name='midi-background')
#         self.midi_process.start()

#     def end_process(self):
#         self._run_code.value = 0
#         self.midi_process.join()
#         self.midi_process.close()


# if __name__ == '__main__':
#     freeze_support()  # for pyinstaller on Windows
 
#     from configstartup import window_left, window_height, window_top, window_width
#     from kivy.app import App
#     from kivy.clock import Clock
#     from kivy.core.window import Window
#     from kivy.metrics import Metrics
#     from kivy.properties import ListProperty, BooleanProperty
#     from kivy.uix.textinput import TextInput
#     from kivy.uix.spinner import Spinner
#     from kivy.uix.button import Button
#     from kivy.utils import platform

#     set_start_method('spawn')  # required for mac prior to Python 3.8

#     class IntegerInput(TextInput):
#         def insert_text(self, substring, from_undo=False):
#             s = substring if substring.isdigit() else ''
#             return super().insert_text(s, from_undo=from_undo)

#         def on_text_validate(self):
#             if int(self.text) < 47:
#                 self.text = '47'
#             if int(self.text) > 6000:
#                 self.text = '6000'
#             app = App.get_running_app()
#             app.root.ids.bpm_slider.value = int(self.text)
#             return super().on_text_validate()


#     class RangeSpinner(Spinner):
#         range = {'47-500': (47, 500), '400-1000': (400, 1000), '1200': (47, 6000),
#                  '1500': (47, 6000), '2000': (47, 6000), '3000': (47, 6000), '6000': (47, 6000)}

#         def set_min_max(self):
#             p = App.get_running_app().root.ids.bpm_slider
#             p.min, p.max = self.range[self.text]
#             if self.text in ['1200', '1500', '2000', '3000', '6000']:
#                 p.value = int(self.text)


#     class TapButton(Button):
#         def __init__(self, **kwargs):
#             self.start_time = 0
#             self.tap_num = 0
#             self.beats = []
#             self.timer = None
#             self.time_limit = 1.5
#             super().__init__(**kwargs)

#         def process_tap(self, bpm, range_select):
#             range_select.text = '47-500'
#             if self.tap_num == 0:
#                 self.start_time = time()
#                 self.tap_num += 1
#                 self.timer = Clock.schedule_once(self.tap_time_out, self.time_limit)

#             elif self.tap_num == 1:
#                 self.timer.cancel()
#                 t1 = time()
#                 self.beats.append(t1 - self.start_time)
#                 self.start_time = t1
#                 self.tap_num += 1
#                 bpm.value = int(60/self.beats[0])
#                 self.timer = Clock.schedule_once(self.tap_time_out, self.time_limit)

#             elif self.tap_num == 2:
#                 self.timer.cancel()
#                 t1 = time()
#                 new_beat = t1 - self.start_time
#                 self.start_time = t1
#                 avg = sum(self.beats)/len(self.beats)
#                 if 1.2 < avg/new_beat > 0.8:
#                     bpm.value = int(60 / new_beat)
#                     self.beats.clear()
#                     self.beats.append(new_beat)
#                 else:
#                     self.beats.append(new_beat)
#                     avg = sum(self.beats) / len(self.beats)
#                     bpm.value = int(60/avg)
#                 self.timer = Clock.schedule_once(self.tap_time_out, self.time_limit)

#         def tap_time_out(self, _):
#             self.start_time = 0
#             self.tap_num = 0
#             self.beats.clear()

#     class MidiClockApp(App):
#         midi_ports = ListProperty([])
#         mcg = MidiClockGen()
#         panel_led = BooleanProperty(False)

#         def flash_led_off(self, _):
#             self.panel_led = self.root.ids.bpm_slider.value >= 667
#             rate = (60 / int(self.root.ids.bpm_slider.value)) * .75
#             Clock.schedule_once(self.flash_led_on, rate)

#         def flash_led_on(self, _):
#             self.panel_led = True
#             rate = (60 / int(self.root.ids.bpm_slider.value)) * .25
#             Clock.schedule_once(self.flash_led_off, rate)

#         def build_config(self, config):
#             config.setdefaults('Window', {'width': window_width,
#                                           'height': window_height})
#             config.setdefaults('Window', {'top': window_top,
#                                           'left': window_left})

#         def open_settings(self, *largs):
#             pass

#         def get_application_config(self):
#             if platform == 'win':
#                 s = '%(appdir)s/%(appname)s.ini'
#             else:  # mac will not write into app folder
#                 s = '~/.%(appname)s.ini'
#             return super().get_application_config(defaultpath=s)

#         def build(self):
#             self.title = 'MidiClock'
#             self.icon = 'images/quarter note.png'
#             Window.minimum_width = window_width
#             Window.minimum_height = window_height
#             self.use_kivy_settings = False
#             Window.bind(on_request_close=self.window_request_close)

#         def window_request_close(self, win):
#             # Window.size is automatically adjusted for density, must divide by density when saving size
#             config = self.config
#             config.set('Window', 'width', int(Window.size[0] / Metrics.density))
#             config.set('Window', 'height', int(Window.size[1] / Metrics.density))
#             config.set('Window', 'top', Window.top)
#             config.set('Window', 'left', Window.left)
#             return False

#         def on_start(self):
#             self.midi_ports = mido.get_output_names()
#             # Set Window to previous size and position
#             config = self.config
#             width = config.getdefault('Window', 'width', window_width)
#             height = config.getdefault('Window', 'height', window_height)
#             Window.size = (int(width), int(height))
#             Window.top = int(float(config.getdefault('Window', 'top', window_top)))
#             Window.left = int(float(config.getdefault('Window', 'left', window_left)))

#         def on_stop(self):
#             if self.mcg.midi_process:
#                 self.mcg.end_process()
#             self.config.write()


#     MidiClockApp().run()
    
    

# ================================= C-code    
    
# byte midi_start = 0xfa;
# byte midi_stop = 0xfc;
# byte midi_clock = 0xf8;
# byte midi_continue = 0xfb;
# int play_flag = 0;
# byte data;

# void setup() {
#  Serial.begin(31250);
# }

# void loop() {
#  if(Serial.available() > 0) {
#  data = Serial.read();
#  if(data == midi_start) {
#  play_flag = 1;
#  } else if(data == midi_continue) {
#  play_flag = 1;
#  } else if(data == midi_stop) {
#  play_flag = 0;
#  } else if((data == midi_clock) && (play_flag == 1)) {
#  Sync();
#  }
#  } 
# }

# void Sync() {
#  // do something for every MIDI Clock pulse when the sequencer is running
# }



# ==================
# import time
# import rtmidi as md
# mtcin = md.MidiIn()
# mout = md.MidiOut()
# mtcin.ignore_types(sysex=False, timing=False)
# mtcin.open_port(0)
# mout.open_port(3)
# event_list = [(0,123),(0.13,234,45),(1.5,345,56),(3,14)]
# ind = 0
# timecode = -1
# mout.send_message((0xf0, 0x7f, 127, 6, 2, 0xf7))
# while ind < len(event_list):
#     msg = mtcin.get_message()
#     if msg:
#         timecode += 1
#     if event_list[ind][0] <= timecode/100.0:
#         print event_list[ind][1:]
#         ind += 1
#     time.sleep(0.001)
# mout.send_message((0xf0, 0x7f, 127, 6, 1, 0xf7))
# mout.send_message((0xf0, 0x7f, 127, 6, 0x44, 6, 1, 32, 0, 0, 0, 0, 0xf7))

# ...
# ========================================
# ...




# Pitchwheel is a 14 bit signed integer
PITCHWHEEL_MIN = -8192
PITCHWHEEL_MAX = 8191


Spec = namedtuple('Spec', ('status_byte', 'type', 'args', 'size'))

_MSG_SPECS = [
    #
    # MIDI message specifications
    #
    # This is the authorative definition of message types.
    #

    #
    # Channel messages
    #
    # pitchwheel value is a signed integer in the range -8192 - 8191
    #
    Spec(0x80, 'note_off',        ('channel', 'note',    'velocity'), 3),
    Spec(0x90, 'note_on',         ('channel', 'note',    'velocity'), 3),
    Spec(0xa0, 'polytouch',       ('channel', 'note',    'value'),    3),
    Spec(0xb0, 'control_change',  ('channel', 'control', 'value'),    3),
    Spec(0xc0, 'program_change',  ('channel', 'program',),   3),
    Spec(0xd0, 'aftertouch',      ('channel', 'value',),    3),
    Spec(0xe0, 'pitchwheel',      ('channel', 'value',),    3),

    #
    # System common messages
    #
    # songpos.pos is 14 bit unsigned int,
    # seralized as lsb msb
    #
    # Todo: rename song to song_select?
    #
    # Sysex messages have a potentially infinite size.
    #
    Spec(0xf0, 'sysex',         ('data',),          float('inf')),
    Spec(0xf1, 'undefined_f1',  (),                 1),
    Spec(0xf2, 'songpos',       ('pos',),           3),
    Spec(0xf3, 'song',          ('song',),          2),
    Spec(0xf4, 'undefined_f4',  (), 1),
    Spec(0xf5, 'undefined_f5',  (), 1),
    Spec(0xf6, 'tune_request',  (), 1),
    Spec(0xf7, 'sysex_end',     (), 1),

    #
    # System realtime messages These can interleave other messages but
    # they have no data bytes, so that's OK
    #
    Spec(0xf8, 'clock',          (), 1),
    Spec(0xf9, 'undefined_f9',   (), 1),
    Spec(0xfa, 'start',          (), 1),
    # Note: 'continue' is a keyword in python, so is
    # is bound to protomidi.msg.continue_
    Spec(0xfb, 'continue',       (), 1),
    Spec(0xfc, 'stop',           (), 1),
    Spec(0xfd, 'undefined_fd',   (), 1),
    Spec(0xfe, 'active_sensing', (), 1),
    Spec(0xff, 'reset',          (), 1),
]

# Dictionary for looking up Channel messages have status byte keys for
# all channels. This means there are keys for all bytes in range
# range(128, 256).
_SPEC_LOOKUP = {}  # Filled in by _init()

def assert_databyte(value):
    """
    Raise
    """
    if not (isinstance(value, int) and (0 <= value < 128)):
        raise ValueError('data byte must be and int in range(0, 128)')


class Message(object):
    """
    MIDI message class.

    New messages are created with mido.new() or mido.Message().
    Valid arguments are:

    mido.new('note_off', channel=0, note=0, velocity=0, time=0)
    mido.new('note_on', channel=0, note=0, velocity=0, time=0)
    mido.new('polytouch', channel=0, note=0, value=0, time=0)
    mido.new('control_change', channel=0, control=0, value=0, time=0)
    mido.new('program_change', channel=0, program=0, time=0)
    mido.new('aftertouch', channel=0, value=0, time=0)
    mido.new('pitchwheel', channel=0, value=0, time=0)
    mido.new('sysex', data=(), time=0)
    mido.new('undefined_f1', time=0)
    mido.new('songpos', pos=0, time=0)
    mido.new('song', song=0, time=0)
    mido.new('undefined_f4', time=0)
    mido.new('undefined_f5', time=0)
    mido.new('tune_request', time=0)
    mido.new('sysex_end', time=0)
    mido.new('clock', time=0)
    mido.new('undefined_f9', time=0)
    mido.new('start', time=0)
    mido.new('continue', time=0)
    mido.new('stop', time=0)
    mido.new('undefined_fd', time=0)
    mido.new('active_sensing', time=0)
    mido.new('reset', time=0)
    """

    def __init__(self, type_or_status_byte, **kw):

        try:
            spec = _SPEC_LOOKUP[type_or_status_byte]
        except KeyError:
            fmt = '{!r} is an invalid type name or status byte'
            raise ValueError(fmt.format(type_or_status_byte))

        self.__dict__['spec'] = spec
        self.__dict__['type'] = self.spec.type

        #
        # Set default values for attributes
        #
        self.__dict__['time'] = 0
        for name in self.spec.args:
            if name == 'data':
                self.__dict__['data'] = ()
            elif name == 'channel':
                # This is a channel message, so if the first
                # arguent to this function was a status_byte,
                # the lower 4 bits will contain the channel.
                if isinstance(type_or_status_byte, int):
                    self.__dict__['channel'] = type_or_status_byte & 0x0f
                else:
                    self.__dict__['channel'] = 0
            else:
                self.__dict__[name] = 0

        #
        # Override attibutes with keyword arguments
        #
        for name, value in kw.items():
            try:
                setattr(self, name, value)
            except AttributeError:
                fmt = '{!r} is an invalid keyword argument for this message'
                raise ValueError(fmt.format(name))

    def copy(self, **override):
        """
        Return a copy of the message. Attributes can
        be overriden by passing keyword arguments.

        msg = Message('note_on', note=20, velocity=64)  # Create a note_on
        msg2 = msg.copy(velocity=32)  # New note_on with softer velocity
        """

        # Get values from this object
        kw = {'time': self.time}
        for name in self.spec.args:
            kw[name] = getattr(self, name)

        # Override
        kw.update(override)

        return Message(self.type, **kw)

    def __setattr__(self, name, value):
        # Todo: validation

        if name in self.spec.args or name == 'time':
            if name == 'time':
                if not (isinstance(value, int) or isinstance(value, float)):
                    raise ValueError('time must be a number')

            elif name == 'channel':
                if not (isinstance(value, int) and (0 <= value < 16)):
                    raise ValueError('channel must be an int in range(0, 16)')

            elif name == 'pos':
                if not (isinstance(value, int) and (0 <= value < 32768)):
                    raise ValueError('pos must be an int in range(0, 32768)')

            elif name == 'value' and self.type == 'pitchwheel':
                if not (isinstance(value, int) and
                        (PITCHWHEEL_MIN <= value <= PITCHWHEEL_MAX)):
                    fmt = 'pitchwheel value must be an int in range({}, {})'
                    raise ValueError(fmt.format(PITCHWHEEL_MIN,
                                                PITCHWHEEL_MAX))

            elif name == 'data':
                value = tuple(value)  # Make the data bytes immutable
                for byte in value:
                    assert_databyte(byte)
            else:
                assert_databyte(value)

            self.__dict__[name] = value
        else:
            fmt = '{} message has no {!r} attribute'
            raise AttributeError(fmt.format(self.type, name))

    def __delattr__(self, name):
        raise AttributeError('Message attributes can\'t be deleted')

    def _get_status_byte(self):
        """
        Compute and return status byte.  For channel messages, the
        channel will be added to the status_byte.
        """

        # Add channel to status byte.
        sb = self.spec.status_byte
        if sb <= 0xf0:
            sb |= self.channel
        return sb

    status_byte = property(fget=_get_status_byte)
    del _get_status_byte

    def bytes(self):
        """
        Encode message and return as a list of bytes.
        """

        b = [self.status_byte]

        for name in self.spec.args:
            if name == 'channel':
                continue  # We already have this

            elif name == 'data':
                b.extend(self.data)

            elif self.type == 'pitchwheel' and name == 'value':
                value = self.value + (2 ** 13)
                lsb = value & 0x7f
                msb = value >> 7
                b.append(lsb)
                b.append(msb)

            elif self.type == 'songpos' and name == 'pos':
                # Convert 14 bit value to two 7-bit values
                # Todo: check if this is correct
                lsb = self.pos & 0x7f
                b.append(lsb)

                msb = self.pos >> 7
                b.append(msb)
            else:
                # Ordinary data byte
                b.append(getattr(self, name))

        if self.type == 'sysex':
            # Append a sysex_end
            b.append(0xf7)

        return b

    def bin(self):
        """
        Encode message and return as a bytearray().
        """

        # Todo: bytearray() or bytes()
        return bytearray(self.bytes())

    def hex(self, sep=' '):
        """
        Encode message and return as a string of hex numbers,
        separated by the string sep. The default separator is
        a single space.
        """

        return sep.join(['{:02X}'.format(byte) for byte in self.bytes()])

    def __repr__(self):
        args = [repr(self.type)]
        args.extend('{}={!r}'.format(name, getattr(self, name))
                    for name in list(self.spec.args))
        args.append('time')
        args = ', '.join(args)
        return 'mido.Message({})'.format(args)

    def __eq__(self, other):
        """
        Compares message type and message specific attributes. (For
        example (msg.type, msg.channel, msg.note, msg.velocity). The
        time, spec and status_byte attributes are not compared.
        """

        if not isinstance(other, Message):
            raise TypeError('comparison between Message and another type')

        def key(msg):
            """
            Return a key for comparison. The key for 'note_on'
            is (msg.type, msg.channel, msg.note, msg.velocity).
            """

            k = tuple([msg.type] + [getattr(msg, a) for a in msg.spec.args])
            return k

        return key(self) == key(other)


def build_signature(spec, include_type=True):
    """
    Builds a contructor signature for a message.

    This is used to create documentation.
    """

    if include_type:
        parts = [repr(spec.type)]
    else:
        parts = []

    for name in spec.args + ('time',):
        if name == 'data':
            parts.append('data=()')
        else:
            parts.append(name + '=0')

    sig = '(' + ', '.join(parts) + ')'

    return sig


def _print_signatures():
    """
    Print arguments for mido.new() for all supported message types.

    This will be used to generate documentation.
    """

    for spec in _MSG_SPECS:
        sig = build_signature(spec)
        print('mido.new {}'.format(sig))

def _init():
    """
    Initialize the module.

    This build a lookup table for message specs
    with keys for every valid message type and
    status byte.
    """

    for spec in _MSG_SPECS:
        if spec.status_byte < 0xf0:
            # Channel message.
            # The upper 4 bits are message type, and
            # the lower 4 are MIDI channel.
            # We need lookup for all 16 MIDI channels.
            for channel in range(16):
                _SPEC_LOOKUP[spec.status_byte | channel] = spec
        else:
            _SPEC_LOOKUP[spec.status_byte] = spec

        _SPEC_LOOKUP[spec.type] = spec

_init()