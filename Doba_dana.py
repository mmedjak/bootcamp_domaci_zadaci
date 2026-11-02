# 1. Određivanje doba dana
# Napisati Python program koji za svaki sat u toku dana(od 0 do 23) ispisuje odgovarajuće doba dana:

#         noć (od 22 do 6 časova),
#         jutro (od 6 do 12 časova),
#         popodne (od 12 do 18 časova) ili
#         veče (od 18 do 22 časa).

# Sačuvati program u fajlu doba_dana.py u lokalnom repozitorijumu naziv_po_želji, a zatim izvršiti commit i push iz VS Code-a.

timeofday = None

for hour in range(24):
    if hour >= 22 or hour < 6:
        timeofday = 'noć'
    elif hour >= 6 and hour < 12:
        timeofday = 'jutro'
    elif hour >= 12 and hour < 18:
        timeofday = 'popodne'
    elif hour >= 18 and hour < 22:
        timeofday = 'veče'
    print(f'{hour} časa: {timeofday}')


       