#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 23:50:42 2018

@author: tumi
@description: gli.py - get letters input

"""
import math as m
import itertools 
import random 

def gLi(get_letters):
    
    print("Number of possible word combinations: {}".\
          format(m.factorial(len(get_letters))))
  
    possible_combinations = m.factorial(len(get_letters))
    return_list = []
    how_many_letters = len(get_letters)

    for x in range(possible_combinations):
        random.shuffle(get_letters, random.random)
        for i in range(how_many_letters):
            for word in itertools.permutations(get_letters[:(how_many_letters - i)]):
               w =  ''.join(word)
               return_list.append(w)
       
    return list(set(return_list))

    
    
