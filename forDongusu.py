#Döngü yapıları

'''
For Döngüleri

'''

'''İn operatörü=bir elemanın başka bir listede veya stringte
olup olmadığını kontrol ediyor'''

a=5 in [1,2,3,4]
b=2 in [1,2,3,4]
print(a)
print(b)

c="p" in "python"
print(c)

d=not 4 in [1,2,3]
print(d)

#for döngüsü

oguzhan=[1,2,3,4,5,6,7,8,9,10]
for i in oguzhan:
    print(i)

toplam = 0
liste = [1,2,3,4,5,6,7,8,9,10]
for a in liste:
    toplam = toplam+a
    print("toplam: {} a: {}".format(toplam,a))
print(toplam)

#çift sayı bulma
liste=[1,2,3,4,5,6,7,8,9,10]
for i in liste:
    if (i%2==0):
        print(i)

#demetlerde for

demet=[(7,8),(9,10),(11,12)]
for i in demet:
    print(i)
       
demet=[(78,154,35),(158,459,78),(152,365,498)]
for a,b,c in demet:
    print("a:{},b:{},c:{}".format (a,b,c))
    print(a * b * c)


'''
SÖZLÜKLER ÜZERİNDE GEZİNMEK
'''

sözlük = {"oguzhan":1,"Ahmet":2,"Müge":3,"muzaffer":4}

for i,j in sözlük.items():
    print("Anahtar:",i,"Değer:",j)
    



