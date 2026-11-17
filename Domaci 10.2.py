import numpy as np

# 1. Sistem beleži broj aktivnih korisnika tokom 12 uzastopnih sati.
# Potrebno je:
#   Prikazati broj korisnika za peti sat.
#   Prikazati broj korisnika za poslednja četiri sata.
#   Izračunati ukupan broj aktivnih korisnika kroz svih 12 sati.
#   Izračunati prosečan broj korisnika po satu.
#   Pronaći sat sa najvećim brojem korisnika.


aktivni_korisnici = np.array([127, 120, 113, 130, 129, 150, 106, 109, 99, 54, 45, 6])
zeljeni_sat = 5
n = zeljeni_sat - 1

print(f'Broj korisnika za {zeljeni_sat}. sat: {aktivni_korisnici[n]}.')
print(f'Broj korisnika za poslednja četiri sata: {aktivni_korisnici[-4:]}.')
print(f'Ukupan broj aktivnih korisnika kroz svih 12 sati: {aktivni_korisnici.sum()}.')
print(f'Prosečan broj aktivnih korisnika po satu: {aktivni_korisnici.mean()}.')
print(f'Sat sa najvećim brojem korisnika: {(aktivni_korisnici.argmax() + 1)}. sat, sa {aktivni_korisnici.max()} aktivnih korisnika.')

# 2. Sistem beleži CPU, RAM i disk usage za pet različitih servera.
# Redovi predstavljaju servere, a kolone CPU, RAM i disk usage.
# Potrebno je:
#   Prikazati dimenzije matrice.
#   Prikazati broj servera i broj metrika.
#   Izračunati prosečnu vrednost svake metrike.
#   Izračunati prosečnu potrošnju resursa za svaki server.
#   Pronaći server sa najvećom prosečnom potrošnjom resursa.


system_log = np.array([
[45, 60, 70],
[55, 65, 80],
[40, 50, 75],
[60, 70, 85],
[65, 70, 70]
])

print(f'Dimenzije matrice su: {system_log.shape}.')
print(f'Broj servera je: {system_log.shape[0]}, a broj metrika je: {system_log.shape[1]}.')
print(f'Prosečne vrednosti metrika su: {np.mean(system_log, axis = 0)}.')
print(f'Prosečna potrošnja resura za svaki server je: {np.round(np.mean(system_log, axis=1),2)}.')
print(f'Server sa najvećom prosečnom potrošnjom resursa: {(np.mean(system_log, axis=1)).argmax()+1}, sa potrošnjom od {(np.round(np.mean(system_log, axis=1),2).max())}.')


# 3. Sistem beleži vreme izvršavanja 15 različitih procesa u sekundama. Potrebno je:
#   Pronaći sve procese koji su trajali duže od 100 sekundi.
#   Pronaći procese koji su trajali između 40 i 100 sekundi.
#   Izbrojati procese koji su trajali kraće od 50 sekundi.
#   Pronaći indekse procesa koji su trajali duže od 100 sekundi.
#   Izračunati prosečno vreme izvršavanja svih procesa.

execution_times = np.array([12, 45, 67, 120, 34, 89, 150, 23, 56, 200, 156, 112, 23, 67, 190])

print(f'Sledeći procesi su trajali duže od 100 sekundi: {np.where(execution_times > 100)[0]+1}, a trajali su: {execution_times[execution_times > 100]}.')
print(f'Sledeći procesi su trajali između 40 i 100 sekundi: {np.where((execution_times >= 40) & (execution_times <= 100))[0]+1}, a trajali su: {execution_times[(execution_times >= 40) & (execution_times <= 100)]}.')
print(f'Postoji {np.count_nonzero(execution_times < 50)} procesa koji su trajali kraće od 50 sekundi.')
print(f'Indeksi procesa koji su trajali duže od 100 sekundi: {np.where(execution_times > 100)[0]}.')
print(f'Prosečno vreme izvršavanja svih procesa je: {execution_times.mean()}.')


# 4. Prodavnica beleži prihode od četiri različite kategorije proizvoda tokom šest meseci. Redovi predstavljaju kategorije proizvoda, a kolone mesece. Potrebno je:
#   Izračunati ukupan prihod svake kategorije proizvoda.
#   Izračunati ukupan prihod za svaki mesec.
#   Pronaći kategoriju proizvoda sa najvećim ukupnim prihodom.
#   Pronaći mesec sa najvećim ukupnim prihodom.
#   Izračunati prosečan prihod po kategoriji proizvoda.
#   Izračunati prosečan mesečni prihod svih kategorija.

products_sales = np.array([
    [230, 340, 450, 220, 450, 550],
    [630, 550, 766, 545, 650, 750],
    [102, 142, 151, 102, 145, 155],
    [1123, 1234, 1145, 1222, 1045, 1055]
])

prihod_proizvod = np.sum(products_sales, axis=1)
print(f'Ukupan prihod svake kategorije proizvoda: {prihod_proizvod}.')
prihod_mesec = np.sum(products_sales, axis=0)
print(f'Ukupan prihod za svaki mesec: {prihod_mesec}.')
print (f'Kategorija proizvoda sa najvećim ukupnim prihodom: {prihod_proizvod.argmax()+1}')
print(f'Mesec sa najvećim ukupnim prihodom: {prihod_mesec.argmax()+1}')
print(f'Prosečan prihod po kategoriji proizvoda: {np.round(np.mean(products_sales, axis=1), 2)}')
print(f'Prosečan mesečni prihod svih kategorija: {np.round(np.mean(products_sales, axis=0), 2)}')


# 5. Sistem beleži prosečne dnevne temperature tokom 15 dana. Neki podaci nedostaju ili nisu validni.
# Validna temperatura mora biti između -20 i 50 stepeni.
# Potrebno je:
    # Identifikovati nedostajuće vrednosti.
    # Identifikovati nevalidne temperature (vrednosti manje od -20 ili veće od 50).
    # Pronaći indekse nevalidnih vrednosti.
    # Izračunati broj nedostajućih i nevalidnih vrednosti.
    # Izračunati procenat nevalidnih i nedostajućih zapisa zajedno.
    # Kreirati novi niz koji sadrži samo validne temperature.
    # Izračunati prosečnu temperaturu bez nedostajućih i nevalidnih vrednosti.

temperatures = np.array([37, -15, 13, -31, np.nan, 36, 3, 2, -9, 61, np.nan, 56, 48, 29, 69])


print(f'Nedostaju temperature za dane: {np.where(np.isnan(temperatures))[0]+1}')

print(f'Nevalidne zebeležene temperature su: {temperatures[(temperatures < -20) | (temperatures > 50)]}')

print(f'Indeksi nevalidnih zebeleženih temperatura su: {np.where((temperatures < -20) | (temperatures > 50))[0]}')

print(f'Ukupan broj nedostajućih i nevalidnih vrednosti je {np.count_nonzero(np.isnan(temperatures)) + np.count_nonzero((temperatures < -20) | (temperatures > 50))}.') 

print(f'Nevalidni i nedostajući zapisa zajedno čine {(np.count_nonzero(np.isnan(temperatures)) + np.count_nonzero((temperatures < -20) | (temperatures > 50))) / len(temperatures) *100}%.')

print (f'Validne temperature su: {temperatures[(~np.isnan(temperatures)) & (temperatures >= -20) & (temperatures <= 50)]}.')
temperatures_valid = temperatures[(~np.isnan(temperatures)) & (temperatures >= -20) & (temperatures <= 50)]

print(f'Prosečna temperatura bez nedostajućih i nevalidnih vrednosti iznosi: {np.mean(temperatures_valid)}.')