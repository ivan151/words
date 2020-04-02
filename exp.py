#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 00:14:17 2020

@author: ivanmankos
"""

from langdetect import detect


def whether_exists(word):
    lang = detect(word)
    if lang == 'en':
        word = word.lower() + '\n'
        with open('words.txt', 'r') as file:
            words = file.readlines()
            if word in words:
                return (True, word)
            else:
                return (False, word)
    else:
        word = word.lower() + '\n'
        with open('rus.txt', 'r') as file:
            words = file.readlines()
            print(words[:40])
            if word in words:
                return (True, word)
            else:
                return (False, word)