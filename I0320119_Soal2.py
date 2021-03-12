# Nama
namaLengkap = ("Aji Manarul Aziz")
print("Halo teman-teman perkenalkan nama saya ", namaLengkap)

namaPanggilan = ("Aji")
print("\nSaya biasa dipanggil ", namaPanggilan, "oleh orang-orang")

# Umur
tanggalLahir = 13
bulanLahir = 4
tahunLahir = 2002
tanggalSekarang = 13
bulanSekarang = 3
tahunSekarang = 2021

if bulanSekarang == 1 or bulanLahir == 1:
    jumlahTanggal = 31
elif bulanSekarang == 2 or bulanLahir == 2:
    jumlahTanggal = 28
elif bulanSekarang == 3 or bulanLahir == 3:
    jumlahTanggal = 31
elif bulanSekarang == 4 or bulanLahir == 4:
    jumlahTanggal = 30
elif bulanSekarang == 5 or bulanLahir == 5:
    jumlahTanggal = 31
elif bulanSekarang == 6 or bulanLahir == 6:
    jumlahTanggal = 30
elif bulanSekarang == 7 or bulanLahir == 7:
    jumlahTanggal = 31
elif bulanSekarang == 8 or bulanLahir == 8:
    jumlahTanggal = 31
elif bulanSekarang == 9 or bulanLahir == 9:
    jumlahTanggal = 30
elif bulanSekarang == 10 or bulanLahir == 10:
    jumlahTanggal = 31
elif bulanSekarang == 11 or bulanLahir == 11:
    jumlahTanggal = 30
else:
    jumlahTanggal = 31

if tanggalSekarang-tanggalLahir < 0:
    tanggalUmur = tanggalSekarang - tanggalLahir + jumlahTanggal
    if bulanSekarang - bulanLahir < 0:
        bulanUmur = bulanSekarang - bulanLahir + 12
        tahunUmur = tahunSekarang - tahunLahir - 1
    else: 
        bulanUmur = bulanSekarang - bulanLahir
        tahunUmur = tahunSekarang - tahunLahir
else:
    tanggalUmur = tanggalSekarang - tanggalLahir
    if bulanSekarang - bulanLahir < 0:
        bulanUmur = bulanSekarang - bulanLahir + 12
        tahunUmur = tahunSekarang - tahunLahir - 1
    else: 
        bulanUmur = bulanSekarang - bulanLahir
        tahunUmur = tahunSekarang - tahunLahir

print("\nUmur saya adalah", tahunUmur, "tahun", bulanUmur, "bulan", tanggalUmur, "hari")

# Tinggi Badan dan Berat Badan
tinggi = 1.7
berat = 70.2
imt = berat / (tinggi ** 2)
if imt < 18.5:
    golongan = "underweight"
elif 18.5 <= imt <= 24.99:
    golongan = "normal"
elif 25 <= imt <= 29.99:
    golongan = "overweight"
elif 30 <= imt <= 34.99:
    golongan = "Obese class 1"
elif 35 <= imt <= 39.99:
    golongan = "Obese class 2"
else:
    golongan = "Obese class 3"

print("\nTinggi badan saya adalah", tinggi, "meter","\nBerat badan", berat,"kg", "\nIndeks massa tubuh tergolong", golongan)

# Ukuran Sepatu
ukuran_Eur = 41
ukuran_UK = 7.5
ukuran_cm = 25.7
print("\nUkuran sepatu saya dalam konversi ukuran Eropa adalah", ukuran_Eur, "\natau dalam konversi UK adalah", ukuran_UK, "\natau diubah dalam centimeter adalah", ukuran_cm, "cm") 

alamat = " Sekar Kemuning I Gg. Al-Hidayah No. 98 Kelurahan Karyamulya, Kecamatan Kesambi, Kota Cirebon, Provinsi Jawa Barat\n"
print("\nSaya bertempat tinggal di alamat", alamat)