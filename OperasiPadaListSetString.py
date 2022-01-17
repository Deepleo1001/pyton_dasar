# len  berfungsi untuk menghitung jumlah data
from typing import Counter


list1=[1,2,3,4,5,6,7,7,42,1,3,4,3,4,43]
list2=["PYTHON"]
list3=["Deepleo", "coba", "tanyakan", "kita"]

print(len(list1))
# max berfungsi untuk melihat nilai terbanyak
print(max(list1))
# min berfungsi untuk melihat nilai terkecil
print(min(list1))
# count() digunakan untuk melihat berapa kali nilai muncul
print(list1.count(1))
string1 ="penerapan pada string"
print(string1.count("a"))

# replikasi
rep=list2*2
print (rep)


# in dan not in
string2 = "belajar python sangat menyenangkan"
print('deep' in string2)
print('belajar' in string2)

# short untuk mengurutkan
list1.sort()
print(list1)

list3.sort()
print(list3)

list3.sort(reverse=True)
list3.sort(key=str.lower)
print (list3)
