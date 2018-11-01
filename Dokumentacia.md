#Dokumentácia k DÚ č. 1
#Kalkulátor vybraných valcových zobrazení

##Charakteristika programu:
Program slúži na výpis súradníc zadaného valcového zobrazenia, pri zadanej 
mierke a polomere telesa po desiatich stupňoch pre poludníky i rovnobežky. 
Podobne môže, podľa vôle používateľa, vypísať súradnice zadané používateľom 
aj na mape.
##Beh programu:
1)	Po spustení sa program opýta na mierkové číslo. Zadáva sa celočíselný 
	vstup. V prípade, že zadaný vstup nie je celé číslo, program sa domáha 
	jeho zadania.
2)	Po zadní mierkového čísla si program vyžiada polomer telesa v kilometroch. 
	V prípade zadania čísla „0“ sa použije preddefinovaný polomer pre planétu 
	Zem 6371,11 km. V prípade zadania nečíselného vstupu sa program domáha 
	jeho zadania a zároveň zobrazuje nápovedu ohľadom čísla 0.
3)	Ďalej program požaduje zobrazenie. Zobrazenia sú nasledovné: 
	A = Marinovo zobrazenie, B = Braunovo zobrazenie, L = Lanbertovo zobrazenie 
	a M = Mercatorovo zobrazenie. V prípade chybného zadania vypíše program 
	chybovú hlášku s možnosťou nápovedi, ktorá sa zadáva písmenom H.
4)	Program vypíše hodnoty pre rovnobežky aj poludníky za sebou, oddelené 
	medzerou. V prípade, že hodnota presahuje hodnotu 100, resp. -100, 
	vypíše sa pomlčka.
5)	Následne program ponúka možnosť na ukončenie programu (stlačením klávesy 
	enter), alebo možnosťou zadania vlastných súradníc (zadanie do vstupu S), 
	ktorým určí ich polohu na mape.
6)	Užívateľ zadá hodnoty geografickej šírky a dĺžky, pričom program 
	kontroluje, či zadáva číslo a zároveň, či nepresahuje 90, resp. 180 stupňov 
	a upozorňuje na chybu.
7)	Vypíšu sa hodnoty zadaných súradníc a zároveň i ich ekvivalent na mape. 
	Následne pokračuje program bodom č. 5.

###Rovnice zobrazení:

#####Pre všetky zobrazenia:
x = R * v

#####A – Marinovo zobrazenie:
y = R * u

#####B – Braunovo zobrazenie:
y = 2R * tg(u/2)

#####L – Lambertovo zobrazenie:
y = R * sin(u)

#####M – Mercatorovo zobrazenie:
y = R * ln(1/tan(u/2))

######Vysvetlivky:
R = polomer telesa
v = geografická dĺžka
u = geografická šírka
