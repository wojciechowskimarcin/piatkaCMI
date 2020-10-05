import array

x = array.array('b')
x.append(5)
x.extend([6,7,8])
print("To jest element tablicy:", x[0], ",", x[1])

### Listy

tekst = "To jest lekcja Pythona"
print("Trzecia litera ze zmiennej tekst to:"+tekst[2])

lista = [1,2,3,4,5,6,7,8]
print("ilość elementów w lista:", len(lista))
print (lista*3)
lista.append(9)
lista.append(["a", "b"])
print (lista)
print("Tablica w tablicy, wartość:",lista[9][0])
lista.insert(10,2)
print (lista)
print("Ilość elementów w tablicy:",len(lista))
print("Ilość elementów w podtablicy:",len(lista[9]))
print("Ilość dwójek", lista.count(2))
print("Położenie pierwszej dwójki", lista.index(2))
lista2 = [-10,-125, 10, 190]
print("Wartość max Lista2:", max(lista2), ", wartość min:", min(lista2))
lista2.sort()
print(lista2)
lista2.clear()
print(lista2)

skok =5
for i in range(0,20,skok):
    print(i+1)

print(list(range(10)))

#numeracja elementów listy
print ("------ enumetate -------")
x=list(range(10))
for i in enumerate(x):
    print(i)


### Kolekcje
# Zbiory (sets)

# Lista (list)
lista = [1,2,3,4,5,6,7,8]
# Słownik (dictionary)
slownik = {1: "Poniedziałek", 2:"Wtorek", 7:"Niedziela"}
print(slownik[7])
print(slownik)
slownik['a'] = "abecadło"
print(slownik)
print(slownik.get('a'))

#Próba wykorzystania wyjątków do generowania błędu zamiast KeyError
try:
    print(slownik['b'])
except KeyError:
    print("Nie ma takiego klucza")

#Wykorzystanie metody get do wygenerowania komunikatu o błędzie
print(slownik.get('b', "Nie ma takiego klucza!!"))

for el in slownik:
    print(el)

for el in slownik.values():
    print(el)

for el in slownik:
    print("slownik[",el,"] =",slownik[el])

#Usuwanie elementów
print(slownik.pop(1))
print(slownik)

##### Funkcje #####
def dodaj(x,y=1,z=0):
    print("x:",x,"y:",y,"z:",z)
    return(x+y+z)

print(dodaj(2,3))
print(dodaj(5,2,3))
print(dodaj(False,2,3))

def fun(a=20, imie="Andrzej", nazwisko="Nawrocki"):
        return imie+" "+nazwisko+" ma "+str(a)+"lat"

fun()
fun(40,"Jan")

fun1 = fun
c=fun1(40, "Andrzej", "Duda")

def funkcja(nazwaFunkcji, adresZam):
    return nazwaFunkcji+" mieszka w miejscowości "+adresZam

print(funkcja(fun(30, "Janek", "Wiśniewski"),"Kożuchów"))

def silnia(x):
    if x<=1:
        return 1
    else:
        return silnia(x-1)*x


print(silnia(5))

import random
print(random.randint(1,5))

from random import randint #Z klasy random pobranie metody randint
print(randint(1,10))

from math import pi
print(pi)

from math import sqrt as pierwiastek

print("Pierwiastek z 16 = ",pierwiastek(16))