#Karşılaştırma oparatörleri

'''
== : İki değer birbirine eşitse sonuç True döner. Eşit değilse False döner
!= : Eşit değil mi? İki değer birbirine eşit değilse True döner. Eşitse False
>  : Soldaki değer sağdakinden büyükse True döner. Değilse False
<  : Soldaki değer sağdakinden küçükse True döner. Değilse False
>= : Soldaki değer sağdaki değerden büyük veya eşitse True döner. Değilse False
<= : Soldaki değer sağdaki değerden küçük veya eşitse True döner. Değilse False
'''

a="Merhaba"=="Merhaba"
print (a)
#True

b="Merhaba"=="Selam"
print(b)
#False

c="Oguzhan"!="Mehmet"
print(c)
#True

c="Oguzhan"!="Oguzhan"
print(c)
#False

d=25>20
print(d)
#True

d=25>30
print(d)
#False

e=20<25
print(e)
#True

e=20<15
print(e)
#False

f=50>=50
print(f)
#True

f=50>=45
print(f)
#True

f=50>=60
print(f)
#False

g=50<=50
print(g)
#True

g=50<=60
print(g)
#True

g=50<=45
print(g)
#False

'''
Stringlerde alfabedeki sıraya göre. Önce gelen daha küçük.
'''
a="araba"<"zula"
print(a)
#True

b="Mekan">"oguzhan"
print(b)
#false
