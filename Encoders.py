#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 10:33:50 2020

@author: jack
"""

DigitEncoders={}
DigitEncoders['L'] = {}
DigitEncoders['R'] = {}
DigitEncoders['G'] = {}

DigitEncoders['L'][0] = [0,0,0,1,1,0,1]
DigitEncoders['L'][1] = [0,0,1,1,0,0,1]
DigitEncoders['L'][2] = [0,0,1,0,0,0,1]
DigitEncoders['L'][3] = [0,1,1,1,1,0,1]
DigitEncoders['L'][4] = [0,1,0,0,0,1,1]
DigitEncoders['L'][5] = [0,1,1,0,0,0,1]
DigitEncoders['L'][6] = [0,1,0,1,1,1,1]
DigitEncoders['L'][7] = [0,1,1,1,0,1,1]
DigitEncoders['L'][8] = [0,1,1,0,1,1,1]
DigitEncoders['L'][9] = [0,0,0,1,0,1,1]

for i in range(10):
    DigitEncoders['R'][i] = [int(i == 0) for i in DigitEncoders['L'][i]]
    DigitEncoders['G'][i] = [int(i == 0) for i in DigitEncoders['L'][i]]
    DigitEncoders['G'][i].reverse()
# %%

CodeStructures = {}
CodeStructures[0] = 'LLLLLLRRRRRR'
CodeStructures[1] = 'LLGLGGRRRRRR'
CodeStructures[2] = 'LLGGLGRRRRRR'
CodeStructures[3] = 'LLGGGLRRRRRR'
CodeStructures[4] = 'LGLLGGRRRRRR'
CodeStructures[5] = 'LGGLLGRRRRRR'
CodeStructures[6] = 'LGGGLLRRRRRR'
CodeStructures[7] = 'LGLGLGRRRRRR'
CodeStructures[8] = 'LGLGGLRRRRRR'
CodeStructures[9] = 'LGGLGLRRRRRR'
    