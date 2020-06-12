#Mantıksal Bağlaçlar

#Karşılaştırma işlemlerinin kontrolünde kullanılır.
#"and,or veya not" ile karşılaştırır.

'''And Operatörü
İkisinin sonucu da True ise, True döner.
Diğer durumlarda False döner.
'''

a=3>1 and "Oguzhan" == "Oguzhan"
print(a)
#True

a=1<2 and "Mehmet" > "pırasa"
print (a)
#False

a= "zurna" > "Kalem" and "Oguzhan">"Ahmet"
print(a)
#True

a= 27!=30 and 45>=45
print(a)
#True

a= 33!=33 and 50<1000 
print(a)
#False

'''OR OPERATÖRÜ
Genel sonucun herhangi biri True ise True döner
False çıkması için bütün değerlerin False olması gerekiyor
'''
a=3>1 or "Oguzhan" == "Oguzhan"
print(a)
#True

a=2<1 or "Mehmet" > "pırasa"
print (a)
#False

a= "zurna" > "Kalem" or "Oguzhan"<"Ahmet"
print(a)
#True

a= 27!=30 or 45>=50
print(a)
#True

a= 33!=33 or 50<30
print(a)
#False


'''Not Operatörü
Sonucun tam zıttı döner
'''

a=not "oguzhan"=="oguzhan"
print(a)
#False

a= not 33!=33
print(a)
#true

#OPERATÖRLERİ KULLANMA

a=not "oguzhan"=="oguzhan" and 3<5 or 33!=33
print(a)
#false
