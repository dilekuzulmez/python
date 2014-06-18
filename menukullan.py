def eposta():
        print 'size eposta ile ulasilacak'
def eposta():
        print 'size mektup ile ulasilacak'
def eposta():
	print 'size web sayfasi ile ulasilacak'
okunan=''
while okunan <>'C':
	print "size hangi yolla bildirimde bulunulsun?"
	print "[E]posta, [M]ektup, [W]eb, [C]ikis"
	okunan = raw_input()
	menu={'E': 'eposta',
		'M': 'mektup',
        	'W': 'web',
        	'C': 'cikis'}	
	menu[okunan]()


