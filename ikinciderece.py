#! /usr/bin/env python
# -*- coding: UTF-8 -*-
a = input("x karesinin katsayisini girin: ")
b = input("xin katsayisini girin: ")
c = input("sabit terimi girin: ")
delta = b*b-4*a*c
if delta < 0:
   print "Reel kok yok"
if delta == 0:
   kok = -b/2*a
   print kok
if delta > 0:
   kok1 = -b+(delta)**1.0/2
   kok2 = -b-(delta)**1.0/2
   print kok1, kok2
