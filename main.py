#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 23:34:23 2018

@author: tumi
"""

import gli
from isword import createList

get_chars = input("Enter letters to form a word from: ")

get_letters = list(get_chars)
returned_words = gli.gLi(get_letters)
createList(returned_words)

