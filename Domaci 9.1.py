# 1. Napisati funkciju safe_divide(a: float, b: float) -> float | None koja vraća rezultat deljenja dva broja.
# Ako je deljenje moguće, funkcija vraća rezultat.
# Ako pokušamo da delimo nulom, funkcija vraća None.
# Koristiti try i except.
# Primer: safe_divide(10, 2) # 5.0
# safe_divide(10, 0) # None

def safe_divide(a: float, b: float) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        return None


# 2. Napisati funkciju safe_int(value: str) -> int | None koja pokušava da prosleđeni string pretvori u ceo broj. Ako string predstavlja ispravan ceo broj, funkcija vraća taj broj.
# Ako konverzija nije moguća, funkcija vraća None.
# Primer: 
    # safe_int('25') # 25
    # safe_int('-10') # -10
    # safe_int('abc') # None

def safe_int(value: str) -> int | None:
    try:
        return int(value)
    except ValueError:
        return None


# 3. Napisati funkciju get_grade(grades: dict, student: str) -> int | None koja vraća ocenu studenta iz rečnika. Ako student postoji u rečniku, funkcija vraća njegovu ocenu.
# Ako student ne postoji, funkcija vraća None. Koristiti try i except.
# Primer: get_grade({'Ana': 5, 'Marko': 4, 'Jovana': 5}, 'Marko') # 4
# get_grade({'Ana': 5, 'Marko': 4, 'Jovana': 5}, 'Petar') # None

def get_grade(grades: dict, student: str) -> int | None:
    try:
        return(grades[student])
    except KeyError:
        return None


# 4. Napisati funkciju read_file(path: str) -> str koja čita i vraća kompletan sadržaj tekstualnog fajla.
# Ako fajl ne postoji, funkcija vraća poruku 'File not found.'.

# Koristiti try i except.
# Za otvaranje fajla koristiti with open().

def read_file(path: str) -> str:
    try:
        with open(path, 'r') as f:
            return f.read()
            
    except FileNotFoundError:
        return (f'File not found {path}')


# 5.Napisati funkciju sum_numbers(values: list) -> float koja vraća zbir svih elemenata liste koji mogu da se pretvore u brojeve. Elemente liste potrebno je pretvoriti u float.
# Ako neki element nije moguće pretvoriti u broj, preskočiti ga.
# Koristiti try i except.
# Primer: sum_numbers(['10','5.5','abc','3','hello']) #18.5

def sum_numbers(values: list) -> float:
    numbers_total = 0
    for v in values:
        try:
            numbers_total += float(v)
        except ValueError:
            continue
    return numbers_total


# 6.Napisati funkciju get_age(csv_line: str) -> int | None koja iz CSV reda izdvaja i vraća godine osobe.
# Pretpostaviti da CSV red sadrži ime i godine, razdvojene zarezom.
# Ako red nema podatak o godinama ili godine nisu ispravan ceo broj, funkcija vraća None.
# Koristiti try i except.
# Primer:
#     get_age('Ana,22') # 22
#     get_age('Marko,abc') # None
#     get_age('Jovana') # None

def get_age(csv_line: str) -> int | None:
    parts = csv_line.split(',')
    try:
        return int(parts[1])
    except (ValueError, IndexError):
        return None
