a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

delta = b**2-4*a*c

x=(-b-delta**0.5)/(2*a)
y=(-b+delta**0.5)/(2*a)

print ("Birinci kök: {}\nİkinci kök: {}\n".format(x,y))

