kata = "ini adalah metode untuk membuat huruf kapital"
print(f"{kata.upper()}")
print ("============================================")

kata2 = "INI ADALAH METODE UNTUK MEMBUAT SEMUA HURUF MENJADI KECIL"
print(kata2.lower())
print ("============================================")

# ini digunakan untuk mentukan true atau false sebuah kata diawal kalimat
print(kata2.startswith("ini"))
print ("============================================")

# ini digunakan untuk menentukan true atau false sebuah kata diakhir kalimat
print(kata2.endswith("KECIL"))
print ("============================================")

# metode join()
print(' ' 'makan' ' ' .join(['aku' , 'mie']))
print ("============================================")

# metode strip()
pernyataan = "Deepleo deep"
print (pernyataan) 
print ("\n")
print (pernyataan.strip("Deep"))
print ("============================================")

# metode split()
pernyataan2 = "ini adalah metode split"
print (pernyataan2)
print ("============================================")

# split huruf a
print ( pernyataan2.split("a"))
print ("\n")
print ("============================================")

# metode repleace()
print ("ini adalah metode repleace()")
print (pernyataan)
print(pernyataan.replace("deep", "Creation"))
print ("\n")
print ("============================================")

# metode isupper dan islower
updanlow = "AKU adalah Deep"
print(updanlow.isupper())
print(updanlow.islower())
print ("============================================")

# metode isalpha()
print('ini adalah alphabet'.isalpha())
print('iniadalahalphabet'.isalpha())
print('ini adalah alphabet?'.isalpha())
print ("============================================")

# metode isnum()
print("tes")
print('3267487213487'.isalnum())
print('326 748721 3487'.isalnum())
print('326748721.3487'.isalnum())
print ("============================================")

# metode isdecimal()
print('324681764817624'.isdecimal())
print('3246817648176204'.isdecimal())
print ("============================================")

# metode istitle()
print('Ini adalah judul'.istitle())
print('Ini Adalah Judul'.istitle())
print ("============================================")
print ("============================================")
print ("============================================")
# contoh program sederhana
# while True :
#     program= input("masukkan nomor anda :")
#     (program.split("3"))
#     if program.isdecimal() :
#         print ("nomor anda adalah" ,program)
#         break
    
#     print('silahkan masukkan nomor dengan benar'.upper())



# penggunaan zfill()

    # Contoh 1: Penggunaan zfill 5 pada angka satuan
angka = 5
print (str(angka).zfill(5));
    # Contoh 2: Penggunaan zfill 5 pada angka ratusan
angka = 300
print (str(angka).zfill(5));
    # Contoh 3: Penggunaan zfill 5 pada angka desimal negatif (memiliki koma)
angka = -0.45
print (str(angka).zfill(5));
    # Contoh 4: Penggunaan zfill 7 pada angka desimal negatif (memiliki koma)
angka = -0.45
print (str(angka).zfill(7));

    # Contoh 1
kata = 'aku'
print (kata.zfill(5));
    # Contoh 2
kata = 'kamu'
print (kata.zfill(5));
    # Contoh 3
kata = 'dirinya'
print (kata.zfill(5));


# contoh ljust(), rjust(), dan center()
print("ini adalah contoh kiri".ljust(29 ,'!'))
print("ini adalah contoh kanan".rjust(29 ,'!'))
print("ini adalah contoh tengah".center(29 ,'!'))

