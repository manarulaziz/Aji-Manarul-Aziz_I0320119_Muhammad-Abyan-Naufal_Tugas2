# Menu
def menu():
    print ("Pilih Aktivitas")
    print
    print ("1. Menghitung Luas Persegi Panjang")
    print ("2. Menghitung Luas Lingkaran")
    print ("3. Menghitung Luas Kubus")
    print ("4. Konversi Celcius ke Fahrenheit")
    print ("5. Konversi Reamur ke Kelvin")
    print ("6. Keluar")

def persegi():
    print ("Menghitung luas persegi panjang")
    p = float(input("Masukkan panjang: "))
    l = float(input("Masukkan lebar: "))
    luas = p * l
    print("Luas persegi panjang adalah ", luas)
    print
    print("Coba lagi [Y/N]?")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()

def lingkaran():
    print ("Menghitung luas lingkaran")
    radius = float(input("Masukkan jari-jari: "))
    pi = 22 / 7
    luas = pi * (radius ** 2)
    print("Luas lingkaran adalah ", luas)
    print
    print("Coba lagi [Y/N]?")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()

def kubus():
    print ("Menghitung luas permukaan kubus")
    s = float(input("Masukkan sisi: "))
    luas = 6 * (s ** 2)
    print("Luas permukaan kubus adalah ", luas)
    print
    print("Coba lagi [Y/N]?")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()

def celcius():
    print ("Konversi suhu Celcius ke Fahrenheit")
    celcius = float(input('Masukkan temperatur = '))
    print("Dengan temperatur", celcius, "celcius")
    fahrenheit = ((9/5) * celcius) + 32
    print("temperatur dalam fahrenheit adalah", fahrenheit, "fahrenheit")
    print
    print("Coba lagi [Y/N]?")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()
            
def reamur():
    print ("Konversi suhu Reamur ke kelvin")
    reamur = float(input('Masukkan temperatur = '))
    print("Dengan temperatur", reamur, "reamur")
    kelvin = ((5/4) * reamur) + 273
    print("temperatur dalam kelvin adalah", kelvin, "kelvin")
    print
    print("Coba lagi [Y/N]?")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()

# Program Menghitung Luas
print("Selamat Datang di Hasil Program Tugas 2")
print("----------------------------------")
print
menu()

while 1:
    # Input
    pilih = int(input("Masukkan yang ingin dilihat Mas Abyan: "))

    if pilih == 1:
        persegi()
    elif pilih == 2:
        lingkaran()
    elif pilih == 3:
        kubus()
    elif pilih == 4:
        celcius()
    elif pilih == 5:
        reamur()
    elif pilih == 6:
        print("\n"*100)
        break
    else:
        print("Maaf pilihan yang Mas Abyan masukkan tidak terdaftar :)")
        print("Coba lagi [Y/N] ?")
        coba = input().upper()
        if coba == "Y":
            menu()
        else:
            print("\n")*100
            break



