import pandas as pd

R = '/Volumes/bootcamp/northern_star/raw_2025_26/'
m = pd.read_parquet(R + 'matches_2025_26.parquet')

# 1. Analiza rezultata utakmica
#   1.Pronaći sve utakmice u kojima su oba tima postigla bar po jedan gol.
#   2.Pronaći sve utakmice u kojima je domaćin pobedio sa tačno jednim golom razlike.
#   3.Koliko utakmica je završeno rezultatom 0:0?
#   4.Prikazati 10 utakmica sa najviše ukupno postignutih golova.


#   1.Pronaći sve utakmice u kojima su oba tima postigla bar po jedan gol:

m.loc[(m['home_goals'] > 0) & (m['away_goals'] > 0)]


# len(m.loc[(m['home_goals'] > 0) & (m['away_goals'] > 0)])
# Ima ukupno 178 takvih utakmica

#  2.Pronaći sve utakmice u kojima je domaćin pobedio sa tačno jednim golom razlike.

m.loc[m['home_goals'] - m['away_goals'] == 1]

# len(m.loc[m['home_goals'] - m['away_goals'] == 1])
# Ima ukupno 105 takvih utakmica

#   3.Koliko utakmica je završeno rezultatom 0:0?

len(m.loc[(m['home_goals'] == 0) & (m['away_goals'] == 0)])
#26 utakmica je završeno rezultatom 0:0

#   4.Prikazati 10 utakmica sa najviše ukupno postignutih golova.

m['total_goals'] = m['home_goals'] + m['away_goals']
m.sort_values('total_goals', ascending=False).head(10)


# 2. Analiza jednog tima
# Za tim po izboru:
#   1.Prikazati sve utakmice u kojima je učestvovao.
#   2.Koliko je puta pobedio, izgubio i odigrao nerešeno?
#   3.Koliko je golova postigao kao domaćin, a koliko kao gost?
#   4.Pronaći utakmicu u kojoj je postigao najviše golova.

# team: 'BRU'

#   1.Prikazati sve utakmice u kojima je učestvovao.

# utakmice u kojima je učestvovao tim "BRU"
m.loc[(m['home_team'] == 'BRU') | (m['away_team'] == 'BRU')]

#len(m.loc[(m['home_team'] == 'BRU') | (m['away_team'] == 'BRU')])
# Tim je odigrao ukupno 38 utakmica

#   2.Koliko je puta pobedio, izgubio i odigrao nerešeno?
# team: 'BRU'

# Dodata nova kolona 'outcome' koja prati ishod utakmice
m['outcome'] = 'Draw'
m.loc[m['home_goals'] - m['away_goals'] > 0, 'outcome'] ='Home Win'
m.loc[m['home_goals'] - m['away_goals'] < 0, 'outcome'] ='Away Win'

#Utakmice tima BRU u kojima je pobedio kao domacin ili gost:
m.loc[((m['home_team'] == 'BRU') & (m['outcome'] == 'Home Win')) | ((m['away_team'] == 'BRU') & (m['outcome'] == 'Away Win'))]

len(m.loc[((m['home_team'] == 'BRU') & (m['outcome'] == 'Home Win')) | ((m['away_team'] == 'BRU') & (m['outcome'] == 'Away Win'))])
# BRU je pobedio ukupno u 10 utakmica.

len(m.loc[(((m['home_team'] == 'BRU') | (m['away_team'] == 'BRU')) & (m['outcome'] == 'Draw'))])
# Nereseno je bilo u 12 utakmice BRU tima.

len(m.loc[((m['home_team'] == 'BRU') & (m['outcome'] == 'Away Win')) | ((m['away_team'] == 'BRU') & (m['outcome'] == 'Home Win'))])
# BRU je izgubio u ukupno 16 utakmica.

#   3.Koliko je golova postigao kao domaćin, a koliko kao gost?
# team: 'BRU'

# Golovi tima kao domacina:
m.loc[m['home_team'] == 'BRU', 'home_goals'].sum()
# Ukupno 23 gola kao domacin

# Golovi tima kao gosta:
m.loc[m['away_team'] == 'BRU', 'away_goals'].sum()
# Ukupno 16 golova kao gost

#   4.Pronaći utakmicu u kojoj je postigao najviše golova.

m.loc[m['home_team'] == 'BRU'].nlargest(3, 'home_goals') 
# 3 gola kao domacin protiv TBF

m.loc[m['away_team'] == 'BRU'].nlargest(3, 'away_goals') 
# 4 gola kao gost protiv TBF predstavlja najvise postignutih golova u jednoj utakmici.


# 3. Analiza stadiona
#   1.Prikazati sve različite stadione na kojima su odigrane utakmice.
#   2.Pronaći stadion na kojem je odigrano najviše utakmica.
#   3.Za svaki stadion izračunati prosečnu posećenost.
#   4.Prikazati pet stadiona sa najvećom prosečnom posećenošću.

#   1.Prikazati sve različite stadione na kojima su odigrane utakmice.
#   2.Pronaći stadion na kojem je odigrano najviše utakmica.

m['stadium'].unique() # ili isto kao i 2)

m['stadium'].value_counts().sort_values(ascending=False)
# Na svim stadionima je odigrano po 19 utakmica

#   3.Za svaki stadion izračunati prosečnu posećenost.
m.groupby('stadium')['attendance'].mean().round(2)

#   4.Prikazati pet stadiona sa najvećom prosečnom posećenošću.
m.groupby('stadium')['attendance'].mean().round(2).sort_values(ascending=False).head(5)