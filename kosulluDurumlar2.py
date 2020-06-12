#İF ELİF ELSE BLOKLARI

'''
Elif yada anlamına gelmektedir
'''

işlem=input("İşlem giriniz:\n")

if işlem == "1":
    print ("İşlem 1 seçildi")
elif işlem == "2":
    print ("İşlem 2 seçildi")
elif işlem == "3":
    print ("İşlem 3 seçildi")
elif işlem == "4":
    print ("İşlem 4 seçildi")
elif işlem == "5":
    print ("İşlem 5 seçildi")
else:
    print ("Geçersiz İşlem!")

'''
KOŞULUN İLK AŞAMASI İF OLMAK ZORUNDA
'''

#NOT HESAPLAMA

note=float(input("Notunuzu girin:"))
if note>=90:
    print("AA")
elif note>=85:
    print("BA")
elif note>=80:
    print("BB")
elif note>=75:
    print("CB")
elif note>=70:
    print("CC")
elif note>=65:
    print("DC")
elif note>=60:
    print("DD")
else:
    print("KALDINIZ!!!")

