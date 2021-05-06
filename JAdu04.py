# Napiš funkce monthOfBirth, která bude mít jeden parametr - rodné číslo. Funkce ze zadaného rodného čísla určí měsíc narození, které vrátí jako výstup. Nezapomeň, že pro ženy je k měsíci připočtena hodnota 50. Příklad: Pro hodnotu 9207054439 vrátí 7. Pro hodnotu 9555125899 vrátí 5.

RC = input("Zadej celé rodne cislo bez lomítka: ")
# část kodu pro rok
yearOfBirth = RC[0:2]
yearOfBirth_int = int(yearOfBirth)
if yearOfBirth_int < 22:
    print("rok:", 2000 + yearOfBirth_int)  # Milenial
else:
    print("rok:", 1900 + yearOfBirth_int)  # Nemilenial
# část kodu pro měsíc
monthOfBirth = RC[2:4]
monthOfBirth_int = int(monthOfBirth)
  if  monthOfBirth_int > 50:
      zeny = monthOfBirth_int - 50
     print("měsíc:", zeny)  # ženy
  else:
      print("měsíc:", monthOfBirth_int)  # muži
# část kodu co řeší den
dayOfBirth = RC[4:6]
dayOfBirth_int = int(dayOfBirth)
print("den:", dayOfBirth_int)
