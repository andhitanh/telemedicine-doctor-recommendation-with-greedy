import csv

class Doctor :
    def __init__(self, name, specialization, years_experience, rating, fee, start_hour, start_minute, end_hour, end_minute, days_available):
        self.name = name
        self.specialization = specialization
        self.years_experience = years_experience
        self.rating = rating
        self.fee = fee
        self.start_hour = start_hour
        self.start_minute = start_minute
        self.end_hour = end_hour
        self.end_minute = end_minute
        self.days_available = days_available

def csv_to_doctor_list(filename) :
    with open(filename, mode='r') as file:
        csvFile = csv.DictReader(file, delimiter=';')
        doctor_list = []
        for lines in csvFile:
            start_hour, start_minute = lines['Jam Awal Aktif'].split(':')
            end_hour, end_minute = lines['Jam Akhir Aktif'].split(':')
            hari_aktif = lines['Hari Aktif'].split(', ')
            doctor = Doctor(lines['Nama'], lines['Spesialisasi'], lines['Pengalaman'], lines['Rating'], lines['Harga'], int(start_hour), int(start_minute), int(end_hour), int(end_minute), hari_aktif)
            doctor_list.append(doctor)
    return doctor_list