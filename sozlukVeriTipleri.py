'''

Söllük Oluşturma

'''

sozluk1 = {"bir":1,"iki":2,"üç":3,"dört":4}
print(type(sozluk1))
print(sozluk1)

sozluk2 = dict()
print(sozluk2)

'''
Sözlük içinde veriye ulaşma
'''
print(sozluk1["bir"])
print(sozluk1["üç"])
print(sozluk1["dört"])

a={"bir":[1,2,3,4], "iki" : [[1,2],[3,4],[5,6],[7,8]]}
print(a["bir"])
print(a["iki"])
print(a["iki"][1])
print(a["iki"][1][0])

'''
Sözlüğe Eleman Ekleme
'''
sozluk1["beş"]=5
print(sozluk1)

'''
Sözlük Değer değiştirme
'''
sozluk1["iki"] = 7
print(sozluk1)

sozluk1["dört"] +=1
print(sozluk1)

'''
Sözlük Metodları
'''
print(sozluk1)
print(sozluk1.keys())

print(sozluk1.values())

print(sozluk1.items())

for a in sozluk1.items():
    print(a)