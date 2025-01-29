# mon_dict = ()
# print(mon_dict)
# ma_list = [("a", 1), ("b", 2), ("c", 3)]
# diction_list = dict(ma_list)
# print(diction_list)
# print(diction_list[a])
mon_dictionnaire = {"nom": "einstein", "prénom": "albert", "année_naissance": 1879}
# print(mon_dictionnaire)
# print(mon_dictionnaire["année_naissance"])
# print(mon_dictionnaire.get("num_telephone"))
mon_dictionnaire["num_telephone"] = 2025
print(mon_dictionnaire)
ancien_numero = mon_dictionnaire.pop("num_telephone")
# print(mon_dictionnaire)
# print(ancien_numero)
# for clef in mon_dictionnaire:
#     print(clef)
# for valeur in mon_dictionnaire.values():
#     print(valeur)
# for clef in mon_dictionnaire.keys():
#     print(clef)
#
for clef, valeur in mon_dictionnaire.items():
    print(f"L'attribut {clef} a pour valeur: {valeur}.")


operations = {
    "addition": lambda x, y: x + y,
    "difference": lambda x, y: x - y,
    "multiplication": lambda x, y: x * y,
    "double": lambda x: x * 2,
}
print(operations["double"](2))
cubes = {x:x**3 for x in range(1, 10)}
print(cubes)
carree_pairs = {x : x**2 for x in range(5) if x % 2 == 0}
carree_divi_trois = {x : x**2 for x in range(11) if x % 3 == 0}
print(carree_divi_trois)
produits = {"fraise": 2, "banana": 5, "pain": 3}
produits_prix = {prods: f"{prix}$" for prods, prix in produits.items()}
print(produits_prix)
