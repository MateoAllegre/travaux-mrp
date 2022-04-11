 
"""Voici du code de test à ajouter après la définition de vos fonctions
(à la fin de votre fichier).
Interdiction de modifier les lignes suivantes. Interdition d'utiliser
une autre bibliothèque que random. Seuls les résultats des appels suivants
doivent s'afficher, rien d'autre. """

f1 = [['aa', '-bbbb', '-c'], ['-aa', '-bbbb', '-dd'], ['aa', 'bbbb', 'c'],
     ['-bbbb', 'd', '-e']]
dico_f1 = construct_dictionary_from_vars(set_of_variables_from_formula(f1))
print("La formule est :", f1)
print(f"L'ens. de ses var. est : {set_of_variables_from_formula(f1)}.")

print(f"La variable contenue dans le litéral {'aa'} est : " + 
      variable_of_literal('aa'))

print(f"La variable contenue dans le litéral {'-dd'} est : " +
      variable_of_literal("-dd"))

for var in dico_f1:
    dico_f1[var] = True

print("Voici une affectation où toutes les varaibles sont à True :\n",
      dico_f1)

print("Avec cette affectation on a les valeurs Boll. suivantes :")

une_clause = f1[0]
for litéral in une_clause:
      print(f"Le litéral {litéral} a la valeur : ",
            boolean_value_of_literal(dico_f1, litéral))

for clause in f1:
    print(f"La clause {clause} a la valeur : ",
        boolean_value_of_clause(dico_f1, clause))  

print(f"La formule a la valeur : ",
      boolean_value_of_formula(dico_f1, f1))

print(f"La formule a {number_of_true_clauses(dico_f1, f1)} clauses à Vrai.")

liste_nbr_clauses_vraies = evaluate_all_assignments(f1)
liste_nbr_clauses_vraies.sort()
print(f"Liste (triée) du nombre de clauses vraies de la formule : ")
print(liste_nbr_clauses_vraies)
print(f"La longueur de cette listes est : {len(liste_nbr_clauses_vraies)}.")

print("Construisons un itérateur d'affectations un peu plus gros...")
dico = {chr(i) : None for i in range(65, 65 + 26)} 
it = iter_all_assignments(dico)
print("Voici l'itérateur généré : ", it)
print("Explorons un peu cet itérateur...")
for _ in range(3):
    print(next(it))

