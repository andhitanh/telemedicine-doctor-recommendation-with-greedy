import csv
from data_dokter import *
from fungsi_seleksi import *

filename = 'data/tes.csv'

print("Selamat datang di Simulasi Pembuatan Daftar Rekomendasi Dokter untuk Aplikasi Telemedisin!")

nama = input("Agar bisa melakukan pelayanan dengan lebih baik, masukkan nama Anda: ")

print()
print("Selamat datang,", nama, "!")
print("Kami akan membantu Anda menemukan dokter yang sesuai dengan kebutuhan Anda.\n")
print("Berikut adalah spesialisasi yang tersedia: ")
print("1. Dokter Umum\n2. Anak\n3. Penyakit Dalam\n4. Mata\n")
specialization = int(input("Masukkan nomor spesialisasi yang Anda butuhkan (1/2/3/4): "))

if (specialization == 1) :
    specialization_choice = "Dokter Umum"
elif (specialization == 2) :
    specialization_choice = "Spesialis Anak"
elif (specialization == 3) :
    specialization_choice = "Spesialis Penyakit Dalam"
else :
    specialization_choice = "Spesialis Mata"

print()
print("Anda memilih pelayanan dengan", specialization_choice, "\n")

day = input(("Masukkan hari konsultasi yang Anda inginkan: "))

print("Anda hanya dapat memilih waktu konsultasi antara pukul 08:00 hingga 21:00")
print("Masukkan jangka waktu konsultasi yang Anda inginkan: ")
hour_start, minute_start = map(int, input("Masukkan jangka awal konsultasi dengan format JJ:MM (misal 08:00): ").split(':'))
hour_end, minute_end = map(int, input("Masukkan jangka akhir konsultasi dengan format JJ:MM (misal 21:00): ").split(':'))

print()
doctor_number = int(input("Masukkan jumlah maksimal dokter yang Anda inginkan dalam daftar rekomendasi: "))

print()
print("Berikut adalah pilihan metode pengurutan dokter yang dapat Anda pilih:")
print("1. Pengurutan berdasarkan harga\n2. Pengurutan berdasarkan rating\n3. Pengurutan berdasarkan pengalaman\n4. Generator rekomendasi dokter secara menyeluruh\n")
greedy_method = int(input("Masukkan nomor metode pengurutan yang Anda inginkan (1/2/3/4): "))

if greedy_method == 4 :
    doctor_list = density_selection_function(filename)
    result = greedy_by_density(doctor_list, specialization_choice, hour_start, minute_start, hour_end, minute_end, day, doctor_number)
else :
    result = greedy_by_not_density(filename, greedy_method, specialization_choice, hour_start, minute_start, hour_end, minute_end, day, doctor_number)

if (result) :
    print()
    print("Berikut adalah daftar rekomendasi dokter yang sesuai dengan kriteria Anda: ")
    for i in range(len(result)):
        print(f"{i+1}. {result[i].name} (Jadwal: {result[i].start_hour:02}:{result[i].start_minute:02}-{result[i].end_hour:02}:{result[i].end_minute:02})")
        print(f"Rating : {result[i].rating}, Pengalaman : {result[i].years_experience} tahun, Biaya Konsultasi : Rp {result[i].fee}")