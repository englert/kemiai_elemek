#Év;Elem;Vegyjel;Rendszám;Felfedező
# 0   1     2       3         4
with open('felfedezesek.csv', 'r', encoding = 'latin2') as file:
    elsosor = file.readline()
    lista   = [sor.strip().replace(u'\xa0', u' ').split(';') for sor in file ]

# 3. 

print(f'3. feladat: Elemek száma: { len(lista) }' )

# 4. 


okor_db = sum(1 for sor in lista if sor[0] == 'Ókor')
print(f'4. feladat: Felfedezések száma az ókorban: { okor_db }' )

# 5. 

while True:
    vegyjel = input('5. feladat: Kérek egy vegyjelet: ')
    if (0 < len(vegyjel) <3) and vegyjel.isalpha():
        vegyjel = vegyjel.upper()
        break

# 6. #

print('6. feladat: Keresés')

vegyjelek = [ sor[2].upper() for sor in lista ]
if vegyjel in vegyjelek:
    i = vegyjelek.index(vegyjel)
    print( f'        Az elem vegyjele: { lista[i][2] }' )
    print( f'        Az elem neve:     { lista[i][1] }' )
    print( f'        Rendszáma:        { lista[i][3] }' ) 
    print( f'        Felfedezés éve:   { lista[i][0] }' )
    print( f'        Felfedező:        { lista[i][4] }' )
else:
    print( f'        Nincs ilyen elem az adatforrásban!') 

# 7. #

évek = [ int(sor[0]) for sor in  lista if sor[0] != 'Ókor']        
dif  = [ évek[i+1] - évek[i] for i, év in enumerate(évek) if i < len(évek)-1 ]
print('7. feladat:', max(dif), 'év volt a leghosszabb időszak két elem felfedezése között.' )

# 8. #

statisztika = dict()

for év in évek:
    statisztika[év] = statisztika.get(év, 0) + 1

print(        f'8. feladat: Statisztika')
res = [ print(f'        {év} - {elemek_száma} db') for év, elemek_száma in statisztika.items() if elemek_száma > 3]