#! /usr/bin/env python
# -*- coding: UTF-8 -*-
sayi1 = input("Birinci sayiyi girin: ")
sayi2 = input("İkinci sayiyi girin: ")
sayi3 =input("Ucuncu sayiyi girin: ")
enkucuksayi = sayi1
if sayi2 < enkucuksayi:
   enkucuksayi = sayi2
if sayi3 < enkucuksayi:
   enkucuksayi = sayi3
elif sayi1 == sayi3 == sayi3:
   print "Uc sayi birbirine esittir"
print enkucuksayi
