# CAST 1 - PODMINKY

# Divadlo Pěst na oko pořádá soutěž o lístky na premiéru nového představení Zločin v podmínce. Pro účast v soutěži musí zájemce splnit následující dvě podmínky:
    # Sdílel alespoň 5 příspěvků divadla na sociálních sítích.
    # Letos navštívil(a) alespoň 5 představení.
    # Současně platí, že soutěžit můžou všichni členové Klubu přátel Divadla Pěst na oko, i kdyby podmínky nesplnili.
# Tvým úkolem je vytvořit program, který se uživatele zeptá na všechny potřebné informace (stačí odpověď ano/ne) a vyhodnotí, zda se může zúčastnit soutěže.

soc_media_accep = "ano"
prestaveni_accep = "ano"
klub_pratel_accep = "ano"

soc_media = str(input("Sdílel/ jsi alespoň 5 příspěvků divadla na sociálních sítích? [ano/ne]: "))
prestaveni = str(input("Navštívil/a jsi letos alespoň 5 představení divadla? [ano/ne]: "))
klub_pratel = str(input("Jsi členem klubu přátel Divadla Pěst na oko? [ano/ne]: "))



if ((soc_media == soc_media_accep) and (prestaveni == prestaveni_accep)) or (klub_pratel == klub_pratel_accep):
  print(f"Splňuješ podmínky soutěže.")
else:
  print(f"Bohužel jsi nesplnil/a podmínky soutěže.")


  # CAST 2 - PODMINKY