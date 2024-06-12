from data_dokter import *
import pandas as pd
import numpy as np
import random

# fungsi seleksi untuk metode greedy by fee, greedy by rating, dan greedy by experience
def greedy_by_not_density(filename, greedy_method, specialization, time_start, minute_start, 
                       time_end, minute_end, days, doctor_number) :
    df = pd.read_csv(filename, delimiter=';')
    if greedy_method == 1 :
        df = df.sort_values(by='Harga', ascending=True)
    elif greedy_method == 2 :
        df = df.sort_values(by='Rating', ascending=False)
    else :
        df = df.sort_values(by='Pengalaman', ascending=False)

    doctor_list = df_to_doctor_list(df)
    number_of_doctors = len(doctor_list)

    solution_list = []
    while len(solution_list) < doctor_number and len(doctor_list) > 0:
        doctor = doctor_list.pop(0)
        if Doctor.fungsiKelayakan(doctor, specialization, time_start, minute_start, 
                                  time_end, minute_end, days) :
            solution_list.append(doctor)
    
    if len(solution_list) == 0 :
        print("Tidak ada dokter yang memenuhi kriteria Anda. Coba lagi dengan kriteria yang berbeda!")
    else :
        return solution_list

# fungsi seleksi untuk metode greedy by overall aspect (density)
def density_selection_function(filename) :
    df = pd.read_csv(filename, delimiter=';')
    df = df.sort_values(by='Rating', ascending=False)
    doctor_list = df_to_doctor_list(df)
    number_of_doctors = len(doctor_list)

    density_sorted_doctor_list = []
    while len(density_sorted_doctor_list) < number_of_doctors :
        doctor = doctor_list.pop(0)
        density = (doctor.rating + doctor.years_experience)/doctor.fee
        density_sorted_doctor_list.append((doctor, density))

    density_sorted_doctor_list = sorted(density_sorted_doctor_list, key=lambda x: x[1], reverse=True)

    return density_sorted_doctor_list

def greedy_by_density(doctor_list, specialization, time_start, minute_start, time_end, minute_end, days, doctor_number) :
    solution_list = []
    while len(solution_list) < doctor_number and len(doctor_list) > 0 :
        doctor = doctor_list.pop(0)
        if Doctor.fungsiKelayakan(doctor[0], specialization, time_start, minute_start, 
                                  time_end, minute_end, days) :
            solution_list.append(doctor[0])
    
    if len(solution_list) == 0 :
        print("Tidak ada dokter yang memenuhi kriteria Anda. Coba lagi dengan kriteria yang berbeda!")
    else :
        return solution_list