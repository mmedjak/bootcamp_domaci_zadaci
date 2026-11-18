import requests

# 1. Informacije o svemirskoj stanici
# Napisati funkciju get_space_station() -> dict koja preko Open Notify API-ja (http://api.open-notify.org/iss-now.json) preuzima trenutnu poziciju Međunarodne svemirske stanice (ISS) i vraća rečnik koji sadrži:
    # geografsku širinu (latitude),
    # geografsku dužinu (longitude)

def get_space_station() -> dict:
    url = 'http://api.open-notify.org/iss-now.json'
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()
     
    position = {
        'latitude': data['iss_position']['latitude'],
        'longitude': data['iss_position']['longitude'] 
    }
    
    return position

# 2. Pretraga univerziteta
# Napisati funkciju get_universities(country: str) -> list koja preko Hipolabs API-ja (http://universities.hipolabs.com/search) preuzima univerzitete iz zadate države i vraća listu njihovih naziva.
# Koristiti params={'country' : country} za prosleđivanje naziva države API-ju.

def get_universities(country: str) -> list:
    url = 'http://universities.hipolabs.com/search'
    r = requests.get(url, params={'country': country})
    r.raise_for_status()
    data = r.json()
    result = []
    for uni in data:
        result.append(uni['name'])

    return result


# 3. Informacije o kursu valuta
# Napisati funkciju get_exchange_rate(base: str, target: str) -> float koja preko Frankfurter API-ja (https://api.frankfurter.dev/v1/latest) preuzima kurs između dve valute.
# Funkcija treba da vrati koliko jedinica ciljne valute (target) se dobija za jednu jedinicu početne valute (base).

# Input: get_exchange_rate("EUR", "RSD")
# Output: 117.2

def get_exchange_rate(base: str, target: str) -> float:
    params={
        'base': base,
        'symbols':  target
    }
    url = 'https://api.frankfurter.dev/v1/latest'
    r = requests.get(url, params=params)
    r.raise_for_status()
    rate = r.json()
    return (rate['rates'][target])