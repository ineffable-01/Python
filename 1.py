from random import choices
from string import ascii_letters
from string import digits
from string import punctuation

adet=(int(input("Kaç adet şifre istiyorsunuz:")))
karakter=(int(input("Kaç karakterden oluşsun:")))
for _ in range(adet):
    print("".join(choices(ascii_letters+digits+punctuation, k=karakter)))

