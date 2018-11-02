from math import tan, sin, log, radians, inf

def vypocet_x(R, v):
    """Výpočet x-kových súradníc v mierke 1:1 pre vš. zobrazenia.
    Vstup: polomer telesa a súradnica."""
    return R * radians(v)


def vypocet_y_A(R, u):
    """Výpočet y-vých súradníc v mierke 1:1 pre Marinovo zobrazenie.
    Vstup: polomer telesa a súradnica."""
    return R * radians(u)


def vypocet_y_B(R, u):
    """Výpočet y-vých súradníc v mierke 1:1 pre Braunovo zobrazenie.
    Vstup: polomer telesa a súradnica."""
    return 2 * R * (tan(radians(u) / 2))


def vypocet_y_L(R, u):
    """Výpočet y-vých súradníc v mierke 1:1 pre Lambertovo zobrazenie.
    Vstup: polomer telesa a súradnica."""
    return R * sin(radians(u))


def vypocet_y_M(R, u):
    """Výpočet y-vých súradníc v mierke 1:1 pre Mercatorovo zobrazenie.
    Vstup: polomer telesa a súradnica."""
    if abs(u) == 90:
        return float(inf)
    else:
        return R*log(1/tan(radians(90-u)/2))


def prevod_na_cm(vstup, M):
    """Podľa mierkového čísla prevod výsledku výpočtu na súradnice na mape v cm.
    Vstup: hodnota a mierka, Výstup: hodnota v danej mierke v cm """
    return vstup / M * 100000


def generovanie_x(M, R):
    """Ukladanie mapových súradníc x do zoznamu. Vstup: mierkové číslo a polomer telesa.
    Výstup: Zoznam súradníc "x" v zozname po 10° od -180° do 180°, prevedený na centimetre pri danej mierke na
    zobrazovacú plochu """
    x = []
    for i in range(-180, 190, 10):
        x.append(prevod_na_cm(vypocet_x(R, i), M))
    return x


def generovanie_y(zobrazenie, M, R):
    """Ukladanie mapových súradníc y do zoznamu. Vstup: zobrazenie (podľa dokumentácie, mierkové číslo a polomer telesa.
    Výstup: Zoznam súradníc "y" v zozname po 10° od -90° do 90°, prevedené na centimetre pri danej mierke na
    zobrazovacú plochu """
    y = []
    for i in range(-90, 100, 10):
        if "A" in zobrazenie:
            y.append(prevod_na_cm(vypocet_y_A(R, i), M))
        elif "B" in zobrazenie:
            y.append(prevod_na_cm(vypocet_y_B(R, i), M))
        elif "L" in zobrazenie:
            y.append(prevod_na_cm(vypocet_y_L(R, i), M))
        else:
            y.append(prevod_na_cm(vypocet_y_M(R, i), M))
    return y


def vypis_suradnic(x, y):
    """Zaokrúhlenie hodnôt súradníc na 1 desatinné miesto a nahradenie hodnôt pomlčkou pri presiahnutí určitej hodnoty.
    Výpis súradnic.
    Vstup: zoznamy x a y po 10 stupňoch. """
    x_2desatinne = [round(elem, 1) for elem in x]
    y_2desatinne = [round(elem, 1) for elem in y]
    x_vypis = []
    y_vypis = []
    for i in range(0, 37):
        if 100 >= x_2desatinne[i] >= -100:
            x_vypis.append(x_2desatinne[i])
        else:
            x_vypis.append("-")

    for i in range(0, 19):
        if 100 >= y_2desatinne[i] >= -100:
            y_vypis.append(y_2desatinne[i])
        else:
            y_vypis.append("-")
    print("Rovnobežky:", *y_vypis)
    print("Poludníky: ", *x_vypis)


def zadanie_zobrazenia():
    """Vstup pre typ zobrazenia od použivateľa aj s nápovedou."""
    while True:
        zobrazenie = input("Zadaj zobrazenie: ")
        if zobrazenie == "H":
            print("Určite medzi nasledovnými valcovými zobrazeniami:\nA = Marinovo zobrazenie\nB = Braunovo "
                  "zobrazenie\nL = Lanbertovo zobrazenie\nM = Mercatorovo zobrazenie")
        elif zobrazenie == "A" or zobrazenie == "B" or zobrazenie == "L" or zobrazenie == "M":
            break
        else:
            print("Chybný vstup! Pre nápovedu zadaj do vstupu 'H'")
    return zobrazenie


def zadanie_R():
    """Vstup pre polomer telesa. V prípade zadania nuly sa za teleso považuje Zem o polomer 6371.11 km, chybné
    zadania vracia."""
    while True:
        vstup = input("Zadaj polomer telesa [km]: ")
        try:
            R = float(vstup)
            if R == 0:
                R = 6371.11
                break
            elif R <= 0:
                print("Zadali ste záporné číslo!")
            else:
                break
        except:
            print("Nezadali ste číslo! V prípade, že chcete predefinovaný polomer, zadajte 0")
    return R


def zadanie_M():
    """Vstup pre mierkové číslo. Chybné zadania vracia."""
    while True:
        vstup = input("Zadaj mierkové číslo: ")
        try:
            M = int(vstup)
            if M <= 0:
                print("Zadali ste záporné číslo!")
            else:
                return M
        except:
            print("Nezadali ste celé číslo!")


def zadanie_suradnice(typ):
    """ Vstup pre zadanie súradníc. Nečíselne zadania vracia.
    V prípade chybného čísla, ktoré neodpovedá súradniciam, vracia. """
    if typ == "šírky":
        max_stupne = 90
    else:
        max_stupne = 180
    while True:
        suradnica = input("Zadajte súradnicu geografickej {:s}: ".format(typ))
        try:
            suradnica = float(suradnica)
            if abs(suradnica) <= max_stupne:
                return suradnica
            else:
                print("Zadajte platný údaj! Pre geografické {:s} maximálne +/- {:d}°".format(typ, max_stupne))
        except:
            print("Nezadali ste číslo!")


def vypis_suradnic_xy(x, y, zobrazenie, M, R):
    """Výpočet súradnic x a y pri zadanej mierke, polomeru telesa a zobrazenia v centimetroch.
    Opravuje chybne zadané vstupy (podľa dokumentácie).
    Vstup: Súradnice x a y [float], zobrazenie (podľa dokumentácie), mierka [int] a polomer telesa [float].
    Výstup: Vypísané súradnice na mape v cm. """
    x_mapa = prevod_na_cm(vypocet_x(R, x), M)
    if "A" in zobrazenie:
        y_mapa = prevod_na_cm(vypocet_y_A(R, y), M)
    elif "B" in zobrazenie:
        y_mapa = prevod_na_cm(vypocet_y_B(R, y), M)
    elif "M" in zobrazenie:
        y_mapa = prevod_na_cm(vypocet_y_M(R, y), M)
    else:
        y_mapa = prevod_na_cm(vypocet_y_L(R, y), M)
    print("Súradnice {:.2f}° {:.2f}° sa zobrazia na mape v cm: [{:.1f}, {:.1f}]".format(y, x, y_mapa, x_mapa))


# Zadanie počiatočných údajov
M = zadanie_M()
R = zadanie_R()
zobrazenie = zadanie_zobrazenia()

# Výpis poludníkov a rovnobežiek
vypis_suradnic(generovanie_x(M, R), generovanie_y(zobrazenie, M, R))

while True:
    # Na konci programu možnosť vypísania polohy vlastných súradníc na mape + ukončenie programu
    print("\nPre zadanie vlastných súradníc, zadajte S")
    vstup = input("Pre ukončenie programu stlačte enter: \n")
    if vstup != "S":
        quit()
    y = zadanie_suradnice("šírky")
    x = zadanie_suradnice("dĺžky")
    vypis_suradnic_xy(x, y, zobrazenie, M, R)
