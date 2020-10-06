# Tablice są obecne praktycznie w każdym języku programowania (C, C++, C#, JAVA, Java Script)
# Dzięki tablicom możemy w bardzo łatwy sposób agregować dane - umieszczać je w szufladach
# Adres każdej tablicy zaczyna się od zera np. tablica[0]. Kolejny element to tablica[1], tablica[2]
# Poniżej kilka przykładów wykorzystania tablic

jPolskiOceny = [5,6,4,3,5] # Tworzenie tablicy z jednoczesnym przypisaniem wartości

print("Moją pierwszą oceną z języka polskiego jest:", jPolskiOceny[0], " - dostałem ją za recytację wiersza")
print("Drugą oceną jest:", jPolskiOceny[1], " - dostałem ją za aktywność na lekcji")

# Na tablicach możemy wykonywać różne metody np. możemy sortować wartości, możemy dodawać lub usuwać nowe wartości

# Dodawanie nowych ocen - metoda append (dodaj)
jPolskiOceny.append(2)

#Wyświetlanie całej tablicy, zwróć uwagę na ocenę 2 na końcu
print("Wszystkie oceny z języka polskiego:",jPolskiOceny)

#Możemy dodać kilka ocen - metoda extend (rozszerz)
jPolskiOceny.extend([5,6,4,6])
print("Wszystkie oceny z języka polskiego, po dodaniu [5,6,4,6]:",jPolskiOceny)

#Możemy dodać wartości w określonej pozycji załóżmy że chcemy dodać po pierwszych dwóch ocenach - metoda insert
jPolskiOceny.insert(2, 2) # czyli na 3 pozycji dodajemy ocenę 2
print("Wszystkie oceny z języka polskiego, po dodaniu 2 na indeksie 2 (3 pozycja - 0-1-2):",jPolskiOceny)

#Teraz usuwamy ocenę 4, która ma index 3: jPolskiOceny[3] - metoda pop
jPolskiOceny.pop(3)
print("Wszystkie oceny z języka polskiego, po usunięciu oceny 4:",jPolskiOceny)

#Możemy też usunąć z tablicy określone element, który maja wartość np. 5 - usuwamy pierwszą piątkę :) - metoda remove
jPolskiOceny.remove(5)
print("Wszystkie oceny z języka polskiego, po usunięciu pierwszej napotkanej piątki:",jPolskiOceny)

#Sortujemy wszystkie oceny od najmniejszej do największej - metoda sort
jPolskiOceny.sort()
print("Posortowane oceny od najmniejszej:",jPolskiOceny)

jPolskiOceny.sort(reverse=True)
print("Posortowane oceny od największej:",jPolskiOceny)

#Przykład obliczania średniej ocen

sumaOcenJpolski = 0 # tworzymy zmienne do zsumowania i podzielenia przez ilość ocen - w ten sposób uzyskamy średnią arytmetyczną ocen z języka polskiego
sredniaJpolski = 0
liczbaOcenJezykPolski = len(jPolskiOceny); # zliczamy ilość ocen - czyli ile ocen znajduje się w tablicy jPolskiOceny

# Tworzymy pętlę do zsumwania wszystkich ocen - tworzymy zmienną pomocniczą ocena

for ocena in jPolskiOceny:
    sumaOcenJpolski = sumaOcenJpolski + ocena

print("Suma ocen z języka polskiego:", sumaOcenJpolski)
print("Średnia ocen z języka polskiego:", sumaOcenJpolski/liczbaOcenJezykPolski)
print("Zaookrąglona średnia ocen do 2 miejsc po przecinku z języka polskiego:", round(sumaOcenJpolski/liczbaOcenJezykPolski,2))




