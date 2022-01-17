# program ini dibuat untuk tujuan latihan penerapan list, tupple, dan dictionary
import sys, time
surat_dictionary={
    "Nama": "",
    "Kelas": "",
    "Absen" : "",
    "NISN" : "",fsaf
    "Isi" : "",
}

# loading spin
def spin():
    try:
        L="/-\\|"
        for q in range (100):
            time.sleep(0.1)
            sys.stdout.write("\r["+L[q % len(L)]+"]")
            sys.stdout.flush()
    except:
            exit()

# Teks Berjalan
def ketik(text):
    for i in text + "\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)


print("=============================================")
print("=======SEND DATA TO SOMEONE BY EMAIL=========")
ketik("=============Creator By D.Leo================")
print('\n')

while True :
    
    N = input("[1] Masukkan Nama >>>> \t \t")
    K = input("[2] Masukkan Kelas >>>> \t")
    A = int (input("[3] Masukkan Nomor Absen >>>> \t"))
    NI = int (input("[4] Masukkan Nomor NISN >>>> \t"))
    I = str (input("[5] Masukkan Isi Surat >>>> \t"))
    Q = str(input("Apakah Data-Data Yang Anda Masukkan Sudah Benar ?  n/y \t"))
    if Q == "y" :
        break



baru= {
    "Nama": f"{N} \n",
    "Kelas":  f"{K} \n",
    "Absen" :  f"{A} \n",
    "NISN" : f"{NI} \n",
    "Isi" : f"{I} \n",
}   
surat_dictionary.update(baru)
print('\n')
print('\n')
print("=============================================")
ketik("=============Creator By D.Leo================")
print("=============================================")
print(f"{surat_dictionary}")
print('\n')


kirimd = str(input("Kirim Data? n/y \t"))
if kirimd == "y":
    
        nmr=str(input("[!]Masukkan Alamat Email[!] \t"))
        ketik("=============================================")
        kirimdd = str(input("Kirim Data Ke Alamat Email Tersebut? (n/y) \t"))
        ketik("=============================================")
        if kirimdd=="y" :
            spin()
            ketik("Data Berhasil Dikirim By D.leo Project")
        else :
            while True :
                kirimddd=str (input ("Ketikkan Ulang Alamat Email Tujuan anda (y/n)"))
                ketik("=============================================")
                if kirimddd=="y" :
                    nmrr=str(input("[!] Masukkan Alamat Email [!] \t"))
                    ketik("=============================================")
                    spin()
                    ketik("Data Berhasil Dikirim By D.leo Project")
                    ketik("=============================================") 
                break
                
else :
    print("Data yang sudah anda masukkan sudah DIHAPUS secara otomatis")
    ketik("From D.Leo we said Thank You")


