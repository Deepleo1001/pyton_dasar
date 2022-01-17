print("\n")
print("**********************************")
print("KALKULATOR LINUX By Deep")
print("********************************** ")
angkaI = int (input("Masukkan Angka Pertama >>>>\t"))
angkaII = int (input("Masukkan Angka Kedua >>>>>\t "))
tambah = angkaI + angkaII
bagi = angkaI / angkaII
kurang = angkaI - angkaII
kali = angkaI * angkaII

print(
    "==================================================== \n"
    "SILAHKAN PILIH NOMOR OPSI YANG ANDA INGIN LAKUKAN \n"
    "==================================================== \n"
    
    "1. Tambah \t 2. Kurang""\n"
    "3. Bagi \t 4. Kali" "\n"
    "5. Keterangan\n"
)

print("==================================================================")
opsi = int(input("SILAHKAN PILIH NOMOR OPSI YANG ANDA INGIN LAKUKAN >>>>>\t"))
print("================================================================== \n")

if opsi==1 :
    print ("hasil penjumlahan dari %d dan %d adalah %d" %(int(angkaI),int(angkaII),int(tambah)))
elif opsi ==2 :
    print("hasil penjumllahan dari %d dan $%d adalah %d" %(int(angkaI), int(angkaII), int(kurang)))
elif opsi ==3 :
    print("hasil dari pembagian dari %d dan %d adalah %d" %(int(angkaI), int(angkaII), int(bagi)))
elif opsi == 4 :
    print ("hasil dari perkalian dari %d dan %d adalah %d" %(int(angkaI), int(angkaII), int(kali)))
else :
    print("program ini dibuat dengan harapan dapat mempermudah anda dalam melakukan penjumlahan \n"
    "pengurangan, perkalian, pembagian. Sehingga, apabila terdapat hal-hal yang tidak memuaskan \n"
    "atau membuat anda merasa tidak nyaman, MOHON DIMAAFKAN"
    "\n""\n"
    "Creator By D.Leo"
)