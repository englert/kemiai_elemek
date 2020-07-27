'''
Év; Elem; Vegyjel; Rendszám; Felfedező
 0    1      2        3           4
Ókor;Arany;Au;79;Ismeretlen
1250;Arzén;As;33;Albertus Magnus
'''
import sqlite3

def sql(c, sql_parancs, *args):
    c.execute(sql_parancs, *args)
    return c.fetchall()

conn = sqlite3.connect('data.db')
c = conn.cursor()

sql(c, " DROP TABLE IF EXISTS tb ")
sql(c, """
    CREATE TABLE IF NOT EXISTS tb
    (ev        INTEGER,
    elem       TEXT,
    vegyjel    TEXT,
    rendszam   INTEGER,
    felfedezo  TEXT)
""")
conn.commit()

with open('felfedezesek.csv', encoding='latin2') as f:
    fejlec = f.readline().strip()
    for sor in f:
        ev, elem, vegyjel, rendszam, felfedezo  = sor.strip().replace(u'\xa0', u' ').split(';')
        ev = 0 if ev == 'Ókor' else int(ev)
        vegyjel = vegyjel.upper()
        sql(c, " INSERT INTO tb VALUES (?,?,?,?,?) ", ( ev, elem, vegyjel, rendszam, felfedezo ) )
conn.commit()

#3. Hány elem van az állományban?

darab = sql(c, " SELECT count() FROM  tb ")[0][0]     
print( f'3. feladat: Elemek száma:{ darab } ' )

#4. felfedezések száma az ókorban?

darab = sql(c, " SELECT count() FROM  tb WHERE ev==0 ")[0][0]    
print( f'4. feladat: Felfedezések száma az ókorban: { darab }' )

#5. Kérjen be egy vegyjelet

while True:
    be = input('5. feladat: Kérek egy vegyjelet: ')
    if (0 < len(be) <3) and be.isalpha():
        vegyjel = be.upper()
        break

#6.

darab = sql(c, " SELECT COUNT(vegyjel) felfedezo FROM  tb WHERE vegyjel ==? ", (vegyjel,) )[0][0]

if darab == 1:
    res = sql(c, " SELECT vegyjel, elem, rendszam, ev, felfedezo FROM  tb WHERE vegyjel ==? ", (vegyjel,) )
    vegyjel, elem, rendszam, ev, felfedezo    = res[0]
    if ev == 0:
        ev = 'Ókor'
    print( f'6. feladat: Keresés' )
    print( f'        Az elem vegyjele: { vegyjel   }' )
    print( f'        Az elem neve: {     elem      }' )
    print( f'        Rendszáma: {        rendszam  }' )
    print( f'        Felfedezés éve: {   ev        }' )
    print( f'        Felfedező: {        felfedezo }' )
else:
    print( f'        Nincs ilyen elem az adatforrásban!')
    
#7. Hány év volt a leghosszabb időszak két elem felfedezése között.

r = sql(c, " SELECT  ev FROM  tb WHERE ev != 0 ")
dif  = [ r[i+1][0] - r[i][0] for i in range(len(r)-1) ]
print(f'7. feladat: { max(dif) } év volt a leghosszabb időszak két elem felfedezése között.' )

# 8. #

r = sql(c, " SELECT  ev, COUNT(elem)  FROM  tb   GROUP BY ev HAVING ev!=0   ORDER BY COUNT(elem) DESC ")[:3] 
print(   f'8. feladat: Statisztika')
[ print( f'        { i[0] }: { i[1] } db')  for i in r]








