#Dokument�cia k D� �. 1
#Kalkul�tor vybran�ch valcov�ch zobrazen�

##Charakteristika programu:
Program sl��i na v�pis s�radn�c zadan�ho valcov�ho zobrazenia, pri zadanej 
mierke a polomere telesa po desiatich stup�och pre poludn�ky i rovnobe�ky. 
Podobne m��e, pod�a v�le pou��vate�a, vyp�sa� s�radnice zadan� pou��vate�om 
aj na mape.
##Beh programu:
1)	Po spusten� sa program op�ta na mierkov� ��slo. Zad�va sa celo��seln� 
	vstup. V pr�pade, �e zadan� vstup nie je cel� ��slo, program sa dom�ha 
	jeho zadania.
2)	Po zadn� mierkov�ho ��sla si program vy�iada polomer telesa v kilometroch. 
	V pr�pade zadania ��sla �0� sa pou�ije preddefinovan� polomer pre plan�tu 
	Zem 6371,11 km. V pr�pade zadania ne��seln�ho vstupu sa program dom�ha 
	jeho zadania a z�rove� zobrazuje n�povedu oh�adom ��sla 0.
3)	�alej program po�aduje zobrazenie. Zobrazenia s� nasledovn�: 
	A = Marinovo zobrazenie, B = Braunovo zobrazenie, L = Lanbertovo zobrazenie 
	a M = Mercatorovo zobrazenie. V pr�pade chybn�ho zadania vyp�e program 
	chybov� hl�ku s mo�nos�ou n�povedi, ktor� sa zad�va p�smenom H.
4)	Program vyp�e hodnoty pre rovnobe�ky aj poludn�ky za sebou, oddelen� 
	medzerou. V pr�pade, �e hodnota presahuje hodnotu 100, resp. -100, 
	vyp�e sa poml�ka.
5)	N�sledne program pon�ka mo�nos� na ukon�enie programu (stla�en�m kl�vesy 
	enter), alebo mo�nos�ou zadania vlastn�ch s�radn�c (zadanie do vstupu S), 
	ktor�m ur�� ich polohu na mape.
6)	U��vate� zad� hodnoty geografickej ��rky a d�ky, pri�om program 
	kontroluje, �i zad�va ��slo a z�rove�, �i nepresahuje 90, resp. 180 stup�ov 
	a upozor�uje na chybu.
7)	Vyp�u sa hodnoty zadan�ch s�radn�c a z�rove� i ich ekvivalent na mape. 
	N�sledne pokra�uje program bodom �. 5.

###Rovnice zobrazen�:

#####Pre v�etky zobrazenie:
x = R * v

#####A � Marinovo zobrazenie:
y = R * u

#####B � Braunovo zobrazenie:
y = 2R * tg(u/2)

#####L � Lambertovo zobrazenie:
y = R * sin(u)

#####M � Mercatorovo zobrazenie:
y = R * ln(1/tan(u/2))

######Vysvetlivky:
R = polomer telesa
v = geografick� d�ka
u = geografick� ��rka
