from random import randint

print("***************************************")
print("*                                     *")
print("*          KOŚCI ver. 0.1B            *")
print("*                                     *")
print("***************************************")

print("\n")
print("Witaj uzytkowniku w grze Kości")
imie = input("Podaj swoje imię: ")
wybor = input("Wciśnij literę L aby rzucić kośćmi")

while wybor != 'L':
    wybor = input("Zła litera. Wciśnij duże L: ")

wyrzucona = randint(1,6)
print("Wyrzuciłeś "+ str(wyrzucona))
if wyrzucona >= 5:
    print("WOW. Niezły wynik!!!")
else:
     print("No ... Poszło Tobie dobrze!")

