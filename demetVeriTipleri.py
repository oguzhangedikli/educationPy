'''
Demet Oluşturma
'''
demet=(1,2,3,4,5,6,7,8)
print(demet)

'''
Demetin elemanına erişme
'''
print(demet[4])
print(demet[-1])
print(demet[0])
print(demet[:4])

'''
Demet Fonksiyonları
'''
#Count Fonksiyonu
demet2=(1,1,2,2,5,5,7,7,7,7,7,8,9,9,9,10)

'''
Demetin içinde kaç defa geçiyor
'''
print(demet2.count(1))
print(demet2.count(7))
print(demet2.count(20))

#İndeks Fonksiyonu
'''
Demette index fonksiyonu. Girilen İndex'in
Demetin içinde kaçıncı sırada olduğunu veriyor
'''
demet3=("ali","php","html","python")
print(demet3.index("php"))
print(demet3.index("python"))

