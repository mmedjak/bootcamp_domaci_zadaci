# 1. Napisati funkciju get_even_positions(data: tuple) -> tuple koja vraća elemente torke koji se nalaze na parnim indeksima (0, 2, 4...).
# Input: (10, 20, 30, 40, 50, 60)
# Output: (10, 30, 50)

def get_even_positions(data: tuple) -> tuple:
    even_positions = []
    for i in range (0, len(data), 2):
        even_positions.append(data[i])
    return (tuple(even_positions))


# 2. Napisati funkciju find_exclusive_students(group1: set, group2:set) -> set koja vraća studente koji se nalaze u prvoj grupi, ali ne i u drugoj.

# Input: {'Ana','Marko','Jovan','Milica'},{'Marko','Milica','Petar'}
# Output: {'Ana','Jovan'}

def find_exclusive_students(group1: set, group2:set) -> set:
    return (group1 - group2)


# 3. Napisati funkciju clean_tags(text: str) -> str koja obrađuje tekst sa tagovima. Potrebno je:
#     Razdvojiti tagove koji su odvojeni karakterom |
#     Ukloniti početne i krajnje razmake svakog taga
#     Sva slova pretvoriti u mala slova
#     Spojiti tagove karakterom -

# Input: ' Python | DATA | SQL ' 
# Output: 'python-data-sql'

def clean_tags(text: str) -> str:
    clean_text = text.strip().lower().split('|')
    tags = []
    for i in clean_text:
        tags.append(i.strip())
    return ('-'.join(tags))


# 4. Napisati funkciju count_products(csv_lines: list) -> dict koja analizira porudžbine iz CSV podataka i vraća ukupan broj naručenih proizvoda.
# Svaki red sadrži ime kupca, naziv proizvoda i količinu, razdvojene zarezom. Prvi red predstavlja zaglavlje i treba ga zanemariti. Ako se isti proizvod pojavljuje u više redova, sabrati njegove
# količine.

# Input: ['customer,product,quantity','Alice,laptop,2','Bob,mouse,3','Alice,laptop,1','Charlie,keyboard,2','Bob,mouse,1']
# Output: {'laptop': 3, 'mouse': 4, 'keyboard': 2}

def count_products(csv_lines: list) -> dict:
  items = []
  csv_lines_relevant = csv_lines[1:]
  for i in csv_lines_relevant:
    items.append(i.split(','))
  product_count = {}
  for x in items:
    if x[1] not in product_count:
        product_count[x[1]] = int(x[2])
    else:
        product_count[x[1]] += int(x[2])
  return(product_count)
