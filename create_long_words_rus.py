#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 21:43:43 2020

@author: ivanmankos
"""

words = open('rus.txt','r').readlines()
long_words = []
for word in words:
    if len(word) > 8:
        long_words.append(word)

with open('long_words_rus.txt','w+') as lw:
    for word in long_words:
        lw.write(word)
lw.close()
