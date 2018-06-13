#fname = raw_input("Enter file name: ")
#Otwiera źródłowy plik tekstowy. Zastępuje powyższą formułę typu input.
fh = open("romeo.txt.txt")
#Tworzy listę 'words'
words = list()
#Warunek
for line in fh:
#Do listy 'words' dodaj podzielone formułą '.split()' słowa 'line'
    words = words + line.split()
#Posortuj słowa z listy 'words' za pomocą formuły '.sort()'
    words.sort()
#tworzy nową listę 'words2'
words2=[]
#Warunek 2 dla wszystkich elementów 'word' na liście 'words'
for word in words:
#Przegląda obydwie listy i sprawdza, czy argument 'word' jest na liście "words2"
	if word not in words2:
#Jeśli go nie ma, togo dopisuje.
		words2.append(word)
#Tym samym unikamy podwójnych słów na liście 'words2', które były na 'words'.
print (words2)
