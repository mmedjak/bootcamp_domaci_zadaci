# 0.1. Napisati program kojim se prevodi temperatura iz Celzijusove skale u Farenhajtovu skalu,
# ako je odgovaraju´ca formula oblika T [◦F] = T [◦C] · 1.80 + 32. Na ulazu se unosi vrednost
# temperature u stepenima Celzijusa (realan broj) a ispisuje se vrednost temperature u stepenima
# Farenhajta.

def temp_f (temp_c):
    return temp_c * 1.80 + 32


#0.2. Napisati program koji za uneti redni broj dana u nedelji (od 1 do 7) ispisuje naziv tog
# dana (ponedeljak - nedelja). Ukoliko je unet broj koji nije izmed¯u 1 i 7, ispisati Pogresan
# unos.

def dan_u_nedelji(redni_broj):
    if redni_broj < 1 or redni_broj > 7:
        return 'Pogresan unos'
    elif redni_broj == 1:
        return 'Ponedeljak'
    elif redni_broj == 2:
        return 'Utorak'
    elif redni_broj == 3:
        return 'Sreda'
    elif redni_broj == 4:
        return 'Četvrtak'
    elif redni_broj == 5:
        return 'Petak'
    elif redni_broj == 6:
        return 'Subota'
    elif redni_broj == 7:
        return 'Nedelja'


# DRUGI NACIN:

dani = ['Ponedeljak', 'Utorak', 'Sreda', 'Četvrtak', 'Petak', 'Subota', 'Nedelja']

def dayofweek (redni_broj):
    if redni_broj < 1 or redni_broj > 7:
        return 'Pogresan unos'
    else:
        return dani[redni_broj -1]


# 0.3. Napisati program koji racuna najveci negativni element u listi.

def najveci_negativni (lista):
   
    for l1 in lista:
        if l1 < 0:
            x = l1
    for l2 in lista:
        if l2 < 0 and l2 > x:
            x = l2 
    return (x)


# 0.5. Napisati program koji racuna broj parnih elemenata date liste.

def parni (lista):
    brojac = 0
    for l in lista:
        if l % 2 == 0:
            brojac += 1
    return (brojac)


# 0.6. Napisati program koji racuna sume elemenata liste celih brojeva koji su deljivi sa 2 odnosno
# sa 3.

# dva zbira
def zbir (lista):
    zbir1 = 0
    zbir2 = 0
    for l1 in lista:
        if l1 % 2 == 0:
            zbir1 += l1
        
    for l2 in lista:
        if l2 % 3 == 0:
            zbir2 += l2
    return (zbir1, zbir2)


#jedan zbir
def zbir (lista):
    zbir = 0
    for l1 in lista:
        if l1 % 2 == 0:
            zbir += l1
        
    for l2 in lista:
        if l2 % 3 == 0:
            zbir += l2
    return zbir
