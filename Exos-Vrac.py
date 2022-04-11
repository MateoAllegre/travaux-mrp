# Exercices Python en vrac.

# Remarques : Supprimer pass, laisser le doc string (avant le code).
# Ne pas changer la structure du code donné. 

#------------- Fonction pour tester vos fonctions. ----------------------------
# verbose=True  => tous les tests (positifs et négatifs) s'affichent.
# verbose=False => Seuls les tests négatifs s'affichent.
# Ne rien modifier d'autre dans cette fonction.
# NB : les fonctions qui ne font qu'afficher des résultats sont testées ad hoc.
def teste_fonction(retour_attendu, f_1, *args, verbose=True):
    resulat_retourné = f_1(*args)
    affichage = "-- Test de " + f_1.__name__ +\
              "(" + ", ".join([("'" + x + "'") if type(x) == str else str(x)
                               for x in args]) +\
              ") :"
    if resulat_retourné == retour_attendu:
        if verbose:
            print(affichage + " Réussi")
    else:
        print(affichage + "\n" + "**"*12 + "\n   ERREUR !!\n" +
                f"Retour attendu : {retour_attendu}\n"
              + f"Retour obtenu  : {resulat_retourné}\n" + "**"*12)

#------------------------------------------------------------------------------
def somme_des_entiers_liste(liste):
    """Prend en entrée une liste d'entiers et retourne la somme de ses
    entiers."""
    somme = 0
    for x in liste:
        somme += x
    return somme

# Tests (ne rien modifier)
teste_fonction(10, somme_des_entiers_liste, list(range(5)))
teste_fonction(0, somme_des_entiers_liste, [])

#------------------------------------------------------------------------------
def somme_des_entiers_positifs_liste(liste):
    """Prend en entrée une liste d'entiers et retourne la somme des
    entiers positifs de cette liste."""
    somme = 0
    for x in liste:
        if x > 0:
            somme += x
    return somme

# Tests (ne rien modifier)
teste_fonction(10, somme_des_entiers_positifs_liste, list(range(5)))
teste_fonction(5, somme_des_entiers_positifs_liste, [-1, -4, 5])
teste_fonction(0, somme_des_entiers_positifs_liste, [-1, -4, -5])

#------------------------------------------------------------------------------
def entiers_pairs_liste(liste):
    """Prend en entrée une liste d'entiers et retourne la sous-liste des
    entiers pairs de cette liste."""
    L = []
    for x in liste:
        if x % 2 == 0:
            L.append(x)
    return L

# Tests (ne rien modifier)
teste_fonction([0, 2, 4], entiers_pairs_liste, list(range(6)))
teste_fonction([2, 4, -8], entiers_pairs_liste, [3, 2, 4, 11, -8])
teste_fonction([], entiers_pairs_liste, [3, 5, 11, -87])

#------------------------------------------------------------------------------
# En pratique, pour faire la chose suivante on utilisera plutôt la fonction
# zip(l1, l2) (qui ne retourne pas une liste mais un objet itérable).
def zipe_listes(liste_1, liste_2):
    """Prend en entrée deux listes et retourne une nouvelle liste composée
    de tuples (x_i, y_i) où x_i est le ième élément de la 1ère liste et y_i
    est le ième élément de la 2ème liste. NB : la liste résultat aura la
    taille de la plus petite des deux."""
    taille_zip = min(len(liste_1),len(liste_2))
    L = []
    for i in range(taille_zip):
        L.append((liste_1[i], liste_2[i]))
    return L

# Tests (ne rien modifier)
teste_fonction([(0, "A"), (1, "B"), (2, "C")],
               zipe_listes, list(range(3)), ["A", "B", "C"])
teste_fonction([(0, "A"), (1, "B"), (2, "C")],
               zipe_listes, list(range(10)), ["A", "B", "C"])
teste_fonction([], zipe_listes, list(range(10)), [])
teste_fonction([(0, "A"), (1, "B")], zipe_listes, [0, 1], ["A", "B", "C"])

#------------------------------------------------------------------------------
def transforme_liste_en_dico(liste):
    """La liste d'entrée contient des tuples à 2 éléments (x, y). La fonction
    doit retourner un dictionnaire dont les éléments sont x:y. Si la liste
    contient plusieurs couples avec x en 1er champ, le dico contiendra
    les valeurs du dernier couple de la liste."""
##    dico = {}
##    for tpl in liste:
##        dico[tpl[0]] = tpl[1]
##    return dico
    return {tpl[0] : tpl[1] for tpl in liste}            ## Encore mieux :   return {x : y for (x,y) in liste}

# Tests (ne rien modifier)
teste_fonction({1:2, "A":66, ("Toto", "Tata"):"Alfred"},
               transforme_liste_en_dico,
               [(1, 2), ("A", 66), (("Toto", "Tata"), "Alfred")])
teste_fonction({1:55, 3:4}, transforme_liste_en_dico,
                            [(1, 2), (3, 4), (1, 55)])

#------------------------------------------------------------------------------
def affiche_contenu_liste(liste_info):
    """liste_info est une liste de tuples à 3 champs, représentant
    une personne :
    Le 1er champ est un tuple de 2 chaines représentant le nom et le prénom de
    la personne, dans cet ordre.
    Le 2ème champ est un entier représentant l'age de la personne.
    Le 3ème champ est un booléen qui vaut True ssi la personne est une femme.
    La fonction ne retourne rien mais affiche ces informations sous la forme :
    M. James Bond a 50 ans. (M. est remplacé par Mme si c'est une femme)."""

    for personne in liste_info:
        (nom, prenom), age, femme = personne
        print(f'{"Mme" if femme else "M."} {prenom} {nom} a {age} {"ans" if age>1 else "an"}.')

##    ENCORE MIEUX :

##    for (nom, prenom), age, femme in liste_info:
##        print(f'{"Mme" if femme else "M."} {prenom} {nom} a {age} ans.')

##    DECONSEILLE car moins lisible :
        
##    for personne in liste_info:
##        print(f'{"Mme" if personne[2] else "M."} {personne[0][1]} {personne[0][0]} a {personne[1]} ans.')

# Tests (ne rien modifier)
print('--'*10 + ' Exercice "Affiche contenu liste" '+ '--'*10)
liste_glob = [(("Nobel", "Alfred"), 55, False),
              (("Bond", "James"), 50, False),
              (("Disney", "Mimi"), 20, True),
              (("Le chat", "Felix"), 1, False)]
affiche_contenu_liste(liste_glob)

#------------------------------------------------------------------------------
def extrait_liste_prénoms(liste_info):
    """Même entrée que la fonction affiche_contenu_liste. Ici la fonction
    retourne une liste uniquement composée des prénoms de la liste d'entrée."""
    return [prenom for (_, prenom), _, _ in liste_info]

# Tests (ne rien modifier)
teste_fonction(["Alfred", "James", "Mimi", "Felix"],extrait_liste_prénoms,
               [(("Nobel", "Alfred"), 55, False),
                (("Bond", "James"), 50, False),
                (("Disney", "Mimi"), 20, True),
                (("Le chat", "Felix"), 1, False)])

#------------------------------------------------------------------------------
# On utilisera en pratique la méthode join(liste_de_chaines) des chaines.
# Ecrivez la fonction suivante sans utiliser cette méthode join(..).
# Testez votre fonction en la comparant aux résultats obtenus avec join(...)
def concat_chaines_avec_separateur(separateur, liste_chaines):
    """Prend en entrée une chaine separateur et une liste de chaines.
    Retourne la chaine composée des chaines de la liste, séparées par le
    séparateur."""
    res = liste_chaines[0]
    for i in liste_chaines[1:]:
        res += separateur + i
    return res

# Tests (ne rien modifier)
teste_fonction("aa--bb--cc", concat_chaines_avec_separateur,
               "--", ["aa", "bb", "cc"])
teste_fonction("X Y", concat_chaines_avec_separateur, " ", ["X", "Y"])
teste_fonction("Toto", concat_chaines_avec_separateur, "++", ["Toto"])

#------------------------------------------------------------------------------
def inverse_a_et_b(mot):
    """Retourne une chaine de caractères qui est la chaine d'entrée
    dans laquelle chaque caractère a (minuscule) est remplacé par b (minuscule)
    et réciproquement."""
    st = ""
    for c in mot:
        if c == 'a':
            st += 'b'
        elif c == 'b':
            st += 'a'
        else:
            st += c
    return st

# Tests (ne rien modifier)
teste_fonction("Lb vitb es aellb", inverse_a_et_b, "La vita es bella")

#------------------------------------------------------------------------------
def remplace_a_par(mot, w):
    """Retourne une chaine de caractères qui est la chaine d'entrée 
    dans laquelle chaque caractère a (minuscule) est remplacé par la
    chaine w."""
    st = ""
    for c in mot:
        if c == 'a':
            st += w
        else:
            st += c
    return st

# Tests (ne rien modifier)
teste_fonction("LXX vitXX es bellXX", remplace_a_par, "La vita es bella", "XX")


#------------------------------------------------------------------------------
def est_palindrome(mot):
    """Fonction Bolléenne qui retourne True ssi la chaine de carcatères mot est
    un palindrome (par exemple le mot "radar" est un palindrome)."""
    return mot == mot[::-1]

# Tests (ne rien modifier)
teste_fonction(True, est_palindrome, "radar")
teste_fonction(True, est_palindrome, "A")
teste_fonction(True, est_palindrome, "")
teste_fonction(False, est_palindrome, "radars")


#------------------------------------------------------------------------------
def chaine_entiers_pairs(liste):
    """Prend en entrée une liste d'entiers positifs et retourne la chaine de
    caractères composée de la concaténation des entiers pairs de cette liste.
    Exemple : si la liste est [1,3,44,8,7,100], le résultat est la chaine :
    "448100". """
    
    return "".join([str(x) if (x%2==0) else "" for x in liste])

##    st = ""
##    for i in liste:
##        if i % 2 == 0:
##            st += str(i)
##    return st

# Tests (ne rien modifier)
teste_fonction("448100", chaine_entiers_pairs, [1,3,44,8,7,100])
teste_fonction("", chaine_entiers_pairs, [1,3,7,103])

#------------------------------------------------------------------------------
def liste_syracuse(n):
    """Prend en entrée un entier n>0. Retourne la liste des éléments de
    la suite de syracuse lorsque le terme initial est n. Rappel :
    u(i+1) = u(i) // 2 si u(i) est pair (// = division entière).
    u(i+1) = 3u(i) + 1 sinon. """
    L = [n]
    while L[-1] != 1:
        new = (L[-1] // 2) if (L[-1] % 2 == 0) else (3*L[-1] + 1)
        L.append(new)
    return L

# Tests (ne rien modifier)
teste_fonction([11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1],
             liste_syracuse, 11)
teste_fonction([8, 4, 2, 1], liste_syracuse, 8)
teste_fonction([1], liste_syracuse, 1)

#------------------------------------------------------------------------------
def look_and_say(z, k):
    """Prend en entrée une chaine z et un entier k. Construit et affiche au fur
    et à mesure k éléments de la suite "look and say". """
    L = []
    for i in range(k):
        newZ = ""
        carac_courant = z[0]
        nb_carac = 0
        for c in z:
            if c != carac_courant:
                newZ += str(nb_carac) + carac_courant
                carac_courant = c
                nb_carac = 1
            else:
                nb_carac += 1
        newZ += str(nb_carac) + carac_courant
        z = newZ
        L.append(z)
        
    nb_spaces = len(L[-1]) // 2
    for st in L:
        print(" "*(nb_spaces - len(st)//2) + st)

look_and_say("1", 18)









            
