# Recepty: Uložte si níže uvedenou strukturu do proměnné recept na začátek nového programu. Vypište pomocí funkce print kolik bude celé jídlo stát korun zaokrouhlené na celé koruny nahoru.
recept = {
  'nazev': 'Batáty se šalvějí a pancettou',
  'narocnost': 'stredni',
  'doba': 30,
  'ingredience': [
    ['batát', '1', '15 kč'],
    ['olivový olej', '2 lžíce', '2 kč'],
    ['pancetta', '4-6 plátků', '21 kč'],
    ['přepuštěné máslo', '2 lžíce', '5 kč'],
    ['mletý černý pepř', '1/2 lžičky', '0.5 kč'],
    ['sůl', '1/2 lžičky', '0.1 kč'],
    ['muškátový oříšek', 'špetka', '1 kč'],
    ['česnek', '2 stroužky', '1 kč'],
    ['šalvějové lístky', '20-25', '12 kč']
  ]
}


# vypis key "ingredience" jako seznam seznamu
suroviny = recept["ingredience"]
#print(suroviny)
#print(type(suroviny))

# vypis polozky ceny ze seznamu seznamu pomoci for cyclu >> seznam stringu
cena = [i[2] for i in suroviny]
#print(cena)

# split polozek seznamu podle mezery na seznam seznamů
cena_split = [(r.split(' ')) for r in cena]
#print(cena_split)

# vypis pouze hodnot bez meny >> seznam stringu a prevod stringu na float >> seznam floatu
cena_hodnota = [float(i[0]) for i in cena_split]
#print(cena_hodnota)

# suma floatu zaokrouhlena nahoru
cena_pokrmu = round(sum(cena_hodnota))
print(cena_pokrmu)


