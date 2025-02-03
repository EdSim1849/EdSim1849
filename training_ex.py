# ex 1
def ex_1(cord1, cord2):
    distance = ((cord2[0] - cord1[0]) ** 2 + (cord2[1] - cord1[1]) ** 2) ** 0.5
    return distance


# ex 2
def ex_2(poly1, poly2):
    # racines communes (intersections)
    racines_communes = poly1.intersection(poly2)

    # racines uniques à chaque polynôme
    racines_uniques_poly1 = poly1.difference(poly2)
    racines_uniques_poly2 = poly2.difference(poly1)
    return racines_communes, racines_uniques_poly1, racines_uniques_poly2


'''
poly1 = {2, -4, 5}
poly2 = {-4, -2, 5}
result = ex_2(poly1, poly2)
print(result[0])
print(result[1])
print(result[2])
'''
# ex 3
'''
notes = {'Alice': 15, 'Bob': 12, 'Charlie': 18, 'David': 9}
a = lambda clef: notes[clef] >= 10
b = {nom: note for nom, note in notes.items() if note >= 10}
c = set(notes.values())
d = dict(filter(lambda note: note[1] > 15, notes.items()))
print(b)
print(c)
print(d)
'''

# ex 4
terme_general_suite = lambda u0, r, n: u0 + r * n
# afficher les 10 premiers termes avec u0=1 et r=3
u0, r = 1, 3
suite = [terme_general_suite(u0, r, n) for n in range(10)]
ensemble_val_paires = {u for u in suite if u % 2 == 0}
print(suite)
print(ensemble_val_paires)

position_en_pairs = {1: u for i, u in enumerate(suite)}

#ex 5
texte = ("Python est un langage de programmation puissant pour les sciences mathématiques et informatique. Par "
         "ailleurs, Python est facile à apprendre")
compter_voyelles = lambda mot: sum(1 for lettre in mot.lower() if lettre in "aeiouy")
liste_mots = texte.split()
voyelles_par_mot = {mot: compter_voyelles(mot) for mot in liste_mots}
mots_uniques = set(liste_mots)
mots_long = list(filter(lambda mot: len(mot > 5, mots_uniques)
