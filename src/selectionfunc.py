'''
Implementing Greedy Algorithm for Constructing Doctor Recommendation List for Telemedicine App
Author : Andhita Naura Hariyanto - 13522060
'''

import pandas as pd
import numpy as np
import random

def fungsiKelayakan(data, specialization, time_start, time_end) :
    '''
    Fungsi Kelayakan
    '''
    df = df[df['Specialization'] == specialization]
    df = df[(df['Availability Start'] <= time_start) & (df['Availability End'] >= time_end)]
    return df

def importcsvtodictionary(df) :
    '''
    Import CSV to Dictionary
    '''
    return df.to_dict()

def greedyByFee(df, specialization, time_start, time_end) :
    '''
    Greedy Algorithm for Constructing Doctor Recommendation List for Telemedicine App
    Greedy by Fee
    '''
    df = df[df['Specialization'] == specialization]
    df = df[(df['Availability Start'] <= time_start) & (df['Availability End'] >= time_end)]
    df = df.sort_values(by='Fee', ascending=True)
    return df
        


def greedyByRating(df, time) :
    pass

def greedyByExperience(df, time) :
    pass

def greedyByAvailability(df, time) :
    pass

def greedyByDensity(df, time) :
    pass
