#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 21:42:39 2020

@author: ivanmankos
"""
import random 

with open('rus.txt','r') as file:
    word = random.choice(file.readlines())
print(word)