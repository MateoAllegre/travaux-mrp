"""Codage de Huffman.
Cette verion est purement pédagogique et ne pourrait pas servir de mise en
production efficace.
Chaque étape donne lieu à des objets intermédiares qui peuvent être affichés,
visualisés, contrôlés.
Cette version code des fichiers en UTF8 dont certains caractères sont codés sur
un, deux, trois ou quatre octets."""

def get_n_for_sort(l):
    return l[0][1]

def construit_liste_ss_arbres_caracteres_nombres(fichier, affiche = True):
    """Pour chaque caractère c du fichier, constuit une liste :
    [(c,n), None, None] où n est le nombre de fois que c est présent dans le
    fichier. Une telle liste sera vue plus tard comme une feuille.
    Si affiche == True, afficher les paires (c,n) dans l'ordre croissant de n.
    """
    dico_occurrences = {}
    list_of_leaves = []
    with open(fichier, "r", encoding="utf8") as f:
        for ligne in f:
            for carac in ligne:
                if dico_occurrences.get(carac) is None:
                    dico_occurrences[carac] = 0
                dico_occurrences[carac] += 1
    for carac, nb_occurrences in dico_occurrences.items():
        list_of_leaves.append([(carac, nb_occurrences), None, None])

    if affiche:
        print(sorted(list_of_leaves, key= get_n_for_sort))
    return list_of_leaves

def construit_arbre_huffman_depuis_liste(liste_car_nbre):
    """À partir de la liste composée de listes du type [(c,n), None, None],
    construit et retourne l'arbre de Huffman suivant l'algorithme classique.
    Le résultat (l'arbre) est une liste composée de listes du type :
    [(c,n), a_1, a_2] avec :
    + n un entier.
    + c un caractère ; dans ce cas a_1 et a_2 sont None et c'est une feuille
        ou c est None ; Dans ce cas c'est un noeud interne et a_1 et a_2 sont
        des sous-arbres. Par convention, a_1 est le sous-arbre gauche codant 0
        et a_1 le sous-arbre droit codant 1."""
    arbre_huffman = liste_car_nbre.copy()
    while len(arbre_huffman) > 1:
        first_node = min(arbre_huffman, key= get_n_for_sort)
        # ou first_node = min(arbre_huffman, key= lambda x:x[0][1])
        arbre_huffman.remove(first_node)
        second_node = min(arbre_huffman, key= get_n_for_sort)
        arbre_huffman.remove(second_node)
        new_node = [(None, first_node[0][1] + second_node[0][1]), first_node, second_node]
        arbre_huffman.append(new_node)
    return arbre_huffman[0]

# Correction
def construit_table_codage_depuis_arbre_huffman(arbre):
    """Construit la table de codage à partir de l'arbre de Huffman.
    Le resultat est un dictionnaire dont les clés sont les caractères et les
    valeurs sont les codes binaires correspondant issus de l'arbre. Un code
    binaire est retourné ici sous forme de chaine de caractères de '0' et '1'.
    """
    def iter_rec_chaines_binaires(arbre, chaine_courante):
        if arbre[0][0] is not None:
            yield arbre[0][0], chaine_courante
        else:
            yield from iter_rec_chaines_binaires(arbre[1], chaine_courante + "0")
            yield from iter_rec_chaines_binaires(arbre[2], chaine_courante + "1")

    table = {}
    it = iter_rec_chaines_binaires(arbre, "")
    for (carac, code) in it:
        table[carac] = code
    return table


def code_fichier(fichier, table_codage):
    """Code chaque caractère du fichier avec la table de codage dont les clés
    sont les caractères et les valeurs les codes binaires sous forme de chaines
    de '0' et de '1'.
    Le résultat est une chaine de caractères de '0' et de '1'."""
    message_code = ""
    with open(fichier, "r", encoding="utf8") as f:
        for ligne in f:
            for carac in ligne:
                message_code += table_codage[carac]
    return message_code


def decode_message(message_binaire, arbre):
    """Prend en entrée une chaine de caractères de '0' et de '1' (message codé)
    + un arbre de huffman. Retourne le décodage sous forme d'une chaine de
    caractères."""
    message_decode = ""
    arbre_courant = arbre
    for bit in message_binaire:
        if arbre_courant[0][0] is not None:
            message_decode += arbre_courant[0][0]
            arbre_courant = arbre
        if bit == '0':
            arbre_courant = arbre_courant[1]
        elif bit == '1':
            arbre_courant = arbre_courant[2]
    return message_decode

# MARCH PA
def tree_to_dfs(arbre):
    def tree_to_dfs_rec(arbre, dfs):
        if arbre[0][0] is None:
            dfs += tree_to_dfs_rec(arbre[1], dfs + "0")
            dfs += tree_to_dfs_rec(arbre[2], dfs + "1")
        return dfs

    return tree_to_dfs_rec(arbre, "")

#----- Manipulations de ces fonctions.

# Partie codage du fichier : 
fichier = "FICHIER_ESSAI_HUFFMAN.txt"

# fichier = "test_file.txt"

#fichier = "Exo_Codage-Huffman-Simple.py" # Pour coder le fichier source...
liste_feuilles = construit_liste_ss_arbres_caracteres_nombres(fichier, False)
arbre = construit_arbre_huffman_depuis_liste(liste_feuilles)
print(arbre)
table = construit_table_codage_depuis_arbre_huffman(arbre)
message_codé = code_fichier(fichier, table) # Codage Huffman en bin. du fichier 

print(f"Le message codé est :\n{message_codé}")
print(10*"---")
print(f"La taille du message codé est de : {len(message_codé)} bits, soit " +
      f"{len(message_codé)/8} octets.")
print(10*"---")

# Partie décodage :

message_décodé = decode_message(message_codé, arbre)
print(f"Le message décodé est : \n{message_décodé}")

print("DFS de l'arbre")
print(tree_to_dfs(arbre))