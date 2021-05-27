# Autobus mezi Zdebudevsí a Kozoprdy jezdí čtyřikrát denně každý všední den v týdnu. Za poslední týden jsme naměřili počty pasažérů pro každou jízdu tam i zpět. Data jsou uložená v souboru pasazeri.txt. Jízda vždy obsahuje dvě čísla oddělená čárkou, která udávají počet pasažérů směrem tam a směrem zpět.(5 radku x 4X2 sloupce)
    # Napište program, který pro první den vypíše, kolik pasažérů jelo celkem směrem tam a kolik směrem zpět.
    # Nechť váš program vypisuje součty pasažérů ze celý týden, tedy kolik lidí za celý týden jelo směrem tam a kolik směrem zpět.

###############################################################################################################################################

# Otevření souboru jako vstupních dat

with open("pasazeri.txt", encoding='utf-8') as vstup:

# rozdělení vstupu na seznam

    for radek in vstup:
      tam = [ sloupec[0] for sloupec in vstup ]
      zpet = [ sloupec[1] for sloupec in vstup ]

      tam_int = [int(pocet) for pocet in tam]
      zpet_int = [int(pocet) for pocet in zpet]

tam_tyden = sum(tam_int)
zpet_tyden = sum(zpet_int)

print(f"Smerem tam jelo za cely tyden: {tam_tyden}")
print(f"Smerem zpet jelo za cely tyden:{zpet_tyden}")

tam_prvniden = sum(tam_int[0:5])
zpet_prvniden = sum(zpet_int[0:5])

print(f"Smerem tam jelo prvni den: {tam_prvniden}")
print(f"Smerem zpet jelo prvni den:{zpet_prvniden}")