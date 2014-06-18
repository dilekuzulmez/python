sayi=3
asaltoplam=2
while sayi<50:
	for i in range(2,sayi):
		kontrol=0
		if sayi%i==0:
			kontrol=1
			break
		else:
			kontrol=0
	if kontrol==0:
		asaltoplam=asaltoplam+sayi
	sayi=sayi+1	
print asaltoplam
