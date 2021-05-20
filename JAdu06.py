# Prvočíslo: Požádej uživatele o zadání celého čísla. Následně urči, zda je toto číslo prvočíslo. 
    # Prvočíslo je číslo, které je dělitelné beze zbytku pouze 2 čísly - 1 a sebou samotným.

number = int(input("Zadej celé číslo: "))
# prvočísla jsou větší než 1
if number > 1:
   # omezující podmínky
   for i in range(2,number):
       if (number % i) == 0:
           print(number,"není prvočíslo")
           print(i,"krát",number//i,"je",number)
           break
   else:
       print(number,"je prvočíslo")
       
# zadaná čísla menší než 1 nejsou prvočísly - nejedná se o přirozená čísla
else:
   print(number,"není prvočíslo")




