ilk=int(raw_input("ilk sayiyi girin: "))
ikinci=int(raw_input("ikinci sayiyi girin: "))
try:
	sonuc=float(ilk)/(ikinci)
	print sonuc

except ZeroDivisionError:
	print "sifira bolme tanimli degil"

except ValueError:
	print "Harf degil sayi girin"
