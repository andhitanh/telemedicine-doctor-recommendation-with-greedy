import csv
from data_dokter import *

filename = 'data/tes.csv'

doc = csv_to_doctor_list(filename)
for d in doc:
    print(d.name)
    print(d.specialization)
    print(d.years_experience)
    print(d.rating)
    print(d.fee)
    print(d.start_hour)
    print(d.start_minute)
    print(d.end_hour)
    print(d.end_minute)
    print(d.days_available)
    print()
