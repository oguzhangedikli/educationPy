print("Kitap kaydetme uygulaması")

kitapadı =input("Kitap adı:")
yazar=input("Yazar Adı:")
kitapevi =input("Kitap evi:")
basımyılı =int(input("Basım Yılı:"))
sayfasayisi =int(input("Sayfa Sayısı:"))
                

kitapbilgisi=[kitapadı,yazar,kitapevi,basımyılı,sayfasayisi]

print("Kitap Bilgileri Kaydediliyor...")


print("Kitabın adı: {}\nKitabın Yazarı: {}\nBasım yeri: {}\nBasım Yılı: {}\nSayfa Sayısı: {}\n".format(kitapbilgisi[0],kitapbilgisi[1],kitapbilgisi[2],kitapbilgisi[3],kitapbilgisi[4]))

print("Kitap Bilgileri Kaydedildi")
