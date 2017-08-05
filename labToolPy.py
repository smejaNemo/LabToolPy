#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 22:49:36 2017

@author: kot
"""

import numpy as np



class ProgNote:
    def __init__(self):
        self.code = []
    def addCommand(self,command):
        self.code.append(command)
    def delCommand(self):
        del self.code[-1]
    def printCommands(self):
        for l in self.code:
            print(l)
    def genOutputLine(self):
        outLine = ''
        for l in self.code:
            outLine += l
        return outLine
    def run(self,repetitions):
        outLine = ''
        for l in self.code:
            outLine += l
        for i in range(repetitions):
            print(outLine)
    def check(self):
        ok = True
        return ok
    

class ThMotor:
    def __init__(self,notebook):
        self.notebook = notebook
    def MoveTo(self,position):
        command = 'MOVE ' + str(position) + '|'
        self.notebook.addCommand(command)
        return command
    def SelectDev(self,devNumber):
        command = 'SELECT_DRV ' + str(devNumber) + '|'
        self.notebook.addCommand(command)
        return command
    def SetVelocity(self,velocity):
        command = 'VELOCITY ' + str(velocity) + '|'
        self.notebook.addCommand(command)
        return command
    def Move(self,value):
        """value <+|-> example: Mevo(+5) go to current position +/- value"""
        command = 'MOVE ' + str(velocity) + '|'
        self.notebook.addCommand(command)
        return command
    

class LecOsc:
    def __init__(self,notebook):
        self.notebook = notebook
    def OscConnect(self,ipAdress):
        command = 'OSCI_CONNECT ' + str(ipAdress) + '|'
        self.notebook.addCommand(command)
        return command
    def OscDisconnct(self):
        command = 'OSCI_DISCONNECT ' + '|'
        self.notebook.addCommand(command)
        return command 
    def OscScreen(self):
        command = 'OSCI_SCREEN ' + '|'
        self.notebook.addCommand(command)
        return command 
    def OscStore(self,fileName):
        command = 'OSCI_STORE ' + str(fileName) + '|'
        self.notebook.addCommand(command)
        return command
    def OscCmd(self,cmd):
        command = 'OSCI_CMD' + str(cmd) + '|'
        self.notebook.addCommand(command)
        return command

class LabTool:
    def __init__(self):
        self.notebook = ProgNote()
        self.code = ''
        self.ThDev = ThMotor(self.notebook)
        self.LecOsc = LecOsc(self.notebook)
    def run (self,repetitions):
        self.notebook.run(repetitions)

l = LabTool()
l.ThDev.MoveTo(0)
l.ThDev.MoveTo(10)
l.ThDev.MoveTo(100)
l.LecOsc.OscScreen()
l.LecOsc.OscConnect('192.168.1.104')
l.notebook.printCommands()
#print(l.notebook.genOutputLine().split('|'))
l.notebook.run(10)
help(l.ThDev.Move)
        
