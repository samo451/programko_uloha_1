#Dokumentácia k DÚ è. 1
#Kalkulátor vybranıch valcovıch zobrazení

##Charakteristika programu:
Program slúi na vıpis súradníc zadaného valcového zobrazenia, pri zadanej 
mierke a polomere telesa po desiatich stupòoch pre poludníky i rovnobeky. 
Podobne môe, pod¾a vôle pouívate¾a, vypísa súradnice zadané pouívate¾om 
aj na mape.
##Beh programu:
1)	Po spustení sa program opıta na mierkové èíslo. Zadáva sa celoèíselnı 
	vstup. V prípade, e zadanı vstup nie je celé èíslo, program sa domáha 
	jeho zadania.
2)	Po zadní mierkového èísla si program vyiada polomer telesa v kilometroch. 
	V prípade zadania èísla „0“ sa pouije preddefinovanı polomer pre planétu 
	Zem 6371,11 km. V prípade zadania neèíselného vstupu sa program domáha 
	jeho zadania a zároveò zobrazuje nápovedu oh¾adom èísla 0.
3)	Ïalej program poaduje zobrazenie. Zobrazenia sú nasledovné: 
	A = Marinovo zobrazenie, B = Braunovo zobrazenie, L = Lanbertovo zobrazenie 
	a M = Mercatorovo zobrazenie. V prípade chybného zadania vypíše program 
	chybovú hlášku s monosou nápovedi, ktorá sa zadáva písmenom H.
4)	Program vypíše hodnoty pre rovnobeky aj poludníky za sebou, oddelené 
	medzerou. V prípade, e hodnota presahuje hodnotu 100, resp. -100, 
	vypíše sa pomlèka.
5)	Následne program ponúka monos na ukonèenie programu (stlaèením klávesy 
	enter), alebo monosou zadania vlastnıch súradníc (zadanie do vstupu S), 
	ktorım urèí ich polohu na mape.
6)	Uívate¾ zadá hodnoty geografickej šírky a dåky, prièom program 
	kontroluje, èi zadáva èíslo a zároveò, èi nepresahuje 90, resp. 180 stupòov 
	a upozoròuje na chybu.
7)	Vypíšu sa hodnoty zadanıch súradníc a zároveò i ich ekvivalent na mape. 
	Následne pokraèuje program bodom è. 5.

###Rovnice zobrazení:

#####Pre všetky zobrazenie:
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
v = geografická dåka
u = geografická šírka
