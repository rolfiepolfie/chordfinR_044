# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 17:43:15 2023

@author: rolfe
"""
from typing import Any, List

class GmSounds():
    
    def _class_to_list(the_object: Any) -> List[str]:
        """
        gets the public attributes of an object, if possible 
        the creation order is preserved
        this funtion's name starts with _ to not get inlcuded in the output
        """
        if hasattr(the_object, '__dict__'):
            fields = the_object.__dict__.keys()
        elif hasattr(the_object, '__slots__'):
            fields = the_object.__slots__
        else:
            fields = dir(the_object)
        fields = [field for field in fields if not field.startswith('_')]
        return fields
    
    AcousticGrandPiano = 0
    BrightAcousticPiano = 1
    lectricGrandPiano =2
    Honky_tonkPiano = 3
    ElectricPiano=4
    ElectricPiano=5
    Harpsichord=6
    Clavi=7
    Celesta=8
    Glockenspiel=9
    MusicBox=10
    Vibraphone=11
    Marimba=12
    Xylophone=13
    TubularBells=14
    Dulcimer=15
    DrawbarOrgan=16
    PercussiveOrgan=17
    RockOrgan=18
    ChurchOrgan=19
    
    ReedOrgan=20
    Accordion=21
    Harmonica=22
    TangoAccordion=23
    AcousticGuitar_nylon=24
    AcousticGuitar_steel=25
    Electric_Guitar_jazz=26
    Electric_Guitar_clean=27
    Electric_Guitar_muted=28
    Overdriven_Guitar=29
    Distortion_Guitar=30
    Guitar_harmonics=31
    AcousticBass=32
    ElectricBass_finger=33
    Electric_Bass_pick=34
    Fretless_Bass=35
    SlapBass_1 =36
    SlapBass_2=37
    SynthBass_1=38
    SynthBass_2=39
    Violin=40
    Viola=41
    Cello=42
    Contrabass=43
    TremoloStrings=44
    Pizzicato_Strings=45
    OrchestralHarp=46
    Timpani=47
    String_Ensemble1=48
    String_Ensemble2=49
    SynthStrings1=50
    SynthStrings2=51
    ChoirAahs=52
    VoiceOohs=53
    SynthVoice=54
    OrchestraHit=55
    Trumpet=56
    Trombone=57
    Tuba=58
    MutedTrumpet=59
    FrenchHorn=60
    BrassSection=61
    SynthBrass1=62
    SynthBrass2=63
    SopranoSax=64
    AltoSax=65  
    TenorSax=66
    BaritoneSax=67
    Oboe=68
    EnglishHorn=69
    Bassoon=70
    Clarinet=71
    Piccolo=72
    Flute=73
    Recorder=74
    PanFlute=75
    BlownBottle=76
    Shakuhachi=77
    Whistle=78
    Ocarina=79
    Lead1square =80
    Lead2sawtooth=81
    Lead3calliope=82
    Lead4chiff=83
    Lead5charang=84
    Lead6voice=85
    Lead7fifths=86
    Lead8basslead=87
    Pad1newage=88
    Pad2warm=89
    Pad3polysynth=90
    Pad4choir=91
    Pad5bowed=92
    Pad6metallic=93
    Pad7halo=94
    Pad8sweep=95
    FX1rain=96
    FX2soundtrack=97
    FX3crystal=98
    FX4atmosphere=99
    FX_5_brightness = 100
    FX6_goblins = 101
    FX7_echoes = 102
    FX8_sci_fi = 103
    Sitar=104
    Banjo=105
    Shamisen=106
    Koto=107
    Kalimba=108
    Bagpipe=109
    Fiddle=110
    Shanai=111
    TinkleBell=112
    Agogo=113
    SteelDrums=114
    Woodblock=115
    TaikoDrum=116
    MelodicTom=117
    SynthDrum=118
    ReverseCymbal=119
    GuitarFretNoise=120
    BreathNoise=121
    Seashore=122
    BirdTweet=123
    TelephoneRing=124
    Helicopter=125
    Applause=126
    Gunshot=127