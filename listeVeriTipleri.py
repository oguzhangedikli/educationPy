#Listeye eleman ekleme
liste=[1,2,3,4,5,6,7]
liste.append(25)

#Listeden Eleman Çıkartma
print (liste)
liste.pop(4)

#Listeyi Sıralama
print(liste)
liste=[34,2,1,6,23,78,12,8]
liste.sort()
print(liste)

#Listeyi tersten Sıralama
liste.sort(reverse = True)
print(liste)

#Alfabetik Sıralama
liste=["oguzhan","gedikli","c","javascript","python"]
liste.sort()
print (liste)

#Alfabetik tersten sıralama
liste.sort(reverse=True)
print (liste)

#İç içe listeler
liste=[1,2],[3,4],[5,6]
print(liste)
