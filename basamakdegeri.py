#! /usr/bin/env python
# -*- coding: UTF-8 -*-
x = input("sayi: ")
yuzlerbas = (x/100)
onlarbas = (x-(yuzlerbas*100))/10
birlerbas = (x-(yuzlerbas)*100-(onlarbas)*10)
if ((yuzlerbas+onlarbas+birlerbas)/3)*3 == (yuzlerbas+onlarbas+birlerbas):
    print "Tam bölünür"
if ((yuzlerbas+onlarbas+birlerbas)/3)*3 != (yuzlerbas+onlarbas+birlerbas):
    print "Tam bölünmez"
