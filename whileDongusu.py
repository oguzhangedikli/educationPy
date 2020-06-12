#Döngü yapıları

'''
while döngüler
'''
a=0

while(a <= 10):
    print("a'nın değeri:",a)
    a+=1

'''
While döngüsü ile liste gezme
'''

liste=["oguzhan","nurcan","sema","ayşe","mehmet"]

a=0

while (a<len(liste)):
    print("Sırası:",a,"Listedeki değeri",liste[a])
    a+=1


    
demet=[("oguzhan",124235,"nurcan"),("sema",1245334,"ayşe"),("Kamuran","mehmet",123)]

a=0
while (a<len(demet)):
    print("Demetteki yeri:",a,"Demetteki değeri:",demet[a])
    a+=1

cevap=input('Faktöriyelini hesaplamak istediğiniz sayıyı giriniz: ')
sonuc=1
sayi=int(cevap)
while sayi>0:
    sonuc=sonuc*sayi
    sayi-=1
print ('Klavyeden girdiğiniz '+str(cevap)+' sayısının faktöriyeli '+str(sonuc)+'  dır')
