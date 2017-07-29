#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 22:49:36 2017

@author: kot
"""

import numpy as np

class ThMotor:
    def __init__(self):
        self.code = ''
    def MoveTo(position):
        command = 'MOVE ' + str(position) + '|'
        self.code = command
        return command

class LabTool:
    def __init__(self):
        self.code = ''
        self.thDev = ThMotor()
    def Thorlabs(self,existing = True):
        
        self.code = self.code + thDev.MoveTo
    def run (self):
        print(self.code)

l = LabTool()
l.thDev.MoveTo(0)
        
