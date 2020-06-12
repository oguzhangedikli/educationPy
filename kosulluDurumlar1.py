#Kosullu Durumlar
'''Pyhon çalışma mantığı'''
a=1
b=2
c=3
print(a+b+c)

'''
İF BLOĞU
Girintiyle oluşturulur
Koşul sağlanınca(TRUE) çalışır. Bu hizadaki her işlem if bloğuna aittir.
Koşul sağlanmazsa if bloğu çalışmaz
'''

#18 yaş hesaplaması
yas=int(input("Yaşınızı giriniz:\n"))

if yas<18:
    print("Bu mekana giremezsiniz")

a=input("Adınız Oğuzhan mı?\n")
if "evet":
    print ("Doğru cevap")


'''
ELSE Bloğu
Girintiyle oluşturulur.
İf bloğu çalışmadığı zaman çalışır.
'''
yass=int(input("Yaşınızı giriniz:\n"))

if yass<18:
    print("Bu mekana giremezsiniz")

else:
    print("Mekana Hoşgeldiniz!")



    
sayi=int(input("Bir sayı giriniz:\n"))

if (sayi < 0):
    print ("negatif sayı")
else:
    print("pozitif sayı")
