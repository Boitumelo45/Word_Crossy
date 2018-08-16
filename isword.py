#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 00:31:47 2018

@author: tumi
"""

list_of_words = []

def createList(returned_words):
    """
        get words: ['son', 'sno', 'osn', 'ons', 'nso', 'nos']
        return valid words found in words.txt file
    """
    
    filename = "words.txt"
    
    with open(filename, 'r') as wf:
        for line in wf:
            list_of_words.append((line.strip()).lower())
    

    valid_words = []
        
    get_all_words = []
    
    for word in returned_words:
        if word in list_of_words:
            valid_words.append(word)
    
    print("Here is a list of valid words found in words.txt: ")
    print(valid_words)
    return valid_words

