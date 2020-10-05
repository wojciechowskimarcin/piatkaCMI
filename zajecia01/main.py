imie = "Marcin"
nazwisko = "Wojciechowski"
wiek = 43
print("Cześć mam na imię " +imie+" i na nazwisko "+nazwisko)
print("Mam "+str(wiek)+" lat")
print("Za 2 lata będę miał: "+str(wiek+2)+" lat")

imiePobrane = input("Podaj swoje imie: ")
print("Masz na imię:" + imiePobrane)
wiekPobrany = input("Podaj swój wiek: ")
print("Masz "+wiekPobrany+" lat")

if wiek > int(wiekPobrany):
    print("Jestem starszy od Ciebie")
elif wiek == int(wiekPobrany):
    print("Jesteśmy w tym samym wieku")
else:
    print("Jestem młodszy od Ciebie!")

