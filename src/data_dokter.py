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

    @staticmethod
    def fungsiKelayakan(data, specialization, time_start, minute_start, time_end, minute_end, days) :
        if data.specialization == specialization :
            if data.start_hour >= time_start and data.start_minute >= minute_start and data.end_hour <= time_end and data.end_minute <= minute_end and days in data.days_available:
                return True
            else : 
                return False
        else :
            return False

def df_to_doctor_list(df):
    doctor_list = []
    for index, row in df.iterrows():
        start_hour, start_minute = row['Jam Awal Aktif'].split(':')
        end_hour, end_minute = row['Jam Akhir Aktif'].split(':')
        hari_aktif = row['Hari Aktif'].split(', ')
        doctor = Doctor(row['Nama'], row['Spesialisasi'], int(row['Pengalaman']), int(row['Rating']), int(row['Harga']), 
                        int(start_hour), int(start_minute), int(end_hour), int(end_minute), hari_aktif)
        doctor_list.append(doctor)
    return doctor_list
