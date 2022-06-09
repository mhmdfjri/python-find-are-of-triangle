import math
def luas(alas, tinggi):
    a = 1/2 * alas * tinggi
    print(f'Luas segitiga: {a:,.2f} cm2')
def keliling(alas, tinggi):
    miring = math.sqrt(alas**2 + tinggi**2)
    x = alas + tinggi + miring
    print(f'Keliling segitiga: {x:,.2f} cm')




