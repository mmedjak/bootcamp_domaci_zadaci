# 16. Написати функцију count_lines(path: str) -> int која враћа број непразних редова у фајлу
# Input: 'data/raw/teams.csv'
# Output: 5

import csv

def count_lines(path: str) -> int:

    with open (path, 'r') as f:
        reader = csv.reader(f)
        lines = 0
        for row in reader:
            if row:
                lines += 1
    
    return (lines)


# 17. Написати функцију read_column(path: str, column: str) -> list која враћа све вредности једне колоне CSV фајла
# Input: 'data/raw/teams.csv', 'city'
# Output: ['Bela Palanka', 'Niš', 'Beograd, Rakovica', 'Kraljevo']
# Ако колона не постоји, вратити празну листу []

import csv
    # for- petlja
def read_column(path:str, column: str) -> list:
    with open (path, 'r') as f:
        teams = list(csv.DictReader(f))
        column_values = []
        for team in teams:
            if column in team:
                column_values.append(team[column])
        
    return (column_values)


    #list comprehension
def read_column(path:str, column: str) -> list:
    with open (path, 'r') as f:
        teams = list(csv.DictReader(f))

        column_values = [team[column] for team in teams if column in team]

    return (column_values)


# 18. Написати функцију write_key_value(path: str, data: dict, headers: list) -> None која
# речник уписује у CSV фајл са две колоне
# Input: 'data/processed/summary.csv', {'rows': 10, 'valid': 6}, ['metric', 'value']
# Садржај фајла након позива:
#     metric,value
#     rows,10
#     valid,6

import csv

def write_key_value(path: str, data: dict, headers: list) -> int:
    data_lista = list(data.items())
    data_lista.insert(0,(headers))
    
    with open(path, 'w') as f:
        csv.writer(f).writerows(data_lista)
    
    return len(data_lista)


# 19. Написати функцију get_header(path: str) -> list која враћа заглавље CSV фајла
# Користити csv.reader и next()
# Input: 'data/raw/teams.csv'
# Output: ['team', 'city', 'points']

import csv

def get_header(path: str) -> list:
    with open (path, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
    return (header)


# 20. Написати функцију read_rows(path: str) -> list која враћа све редове CSV фајла без заглавља, као листу листи
# Користити csv.reader
# Input: 'data/raw/teams.csv'
# Output: [['FK Jedinstvo', 'Bela Palanka', '34'], ['FK Radnički', 'Niš', '41'], ['FK Rakovica', 'Beograd, Rakovica', '28'], ['FK Sloga', 'Kraljevo', '19']]

import csv

def read_rows(path: str) -> list:
    with open (path, 'r') as f:
        reader = csv.reader(f)
        rows = []
        for row in reader:
            rows.append(row)
    return(rows[1:])


# 21. Написати функцију total_points(path: str) -> int која враћа збир бодова свих тимова
# Користити csv.DictReader
# Input: 'data/raw/teams.csv'
# Output: 122

import csv

def total_points(path: str) -> int:
    with open (path, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
        points_rows = rows[1:]
        points = 0
        for row in points_rows:
            points += int(row[2])

    return(points)


# 22. Написати функцију write_rows(path: str, rows: list) -> None која листу листи уписује у CSV фајл
# Input: 'data/processed/people.csv', [['name', 'age'], ['Ana', 20], ['Marko', 22]]
# Садржај фајла након позива
    # name,age
    # Ana,20
    # Marko,22

def write_rows(path: str, rows: list) -> None:
    
    with open(path, 'w') as f:
        writer = csv.writer(f).writerows(rows)