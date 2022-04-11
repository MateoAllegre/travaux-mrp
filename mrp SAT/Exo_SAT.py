import random

# Allegre mateo
# Laurencot mathieu
# Payard clement

"""Data structure of a formula F.
   -----------------------------
    A variable is a string (with no ',', no '&', no ' ' and no '-')
    A positive literal is a variable. 
    A negative literal is a variable with an additional '-' as first character.
    A clause is a list of literals.
    A formula is a list of clauses.
    
    The dictionary of a formula is the dictionary whose keys are the variables
    of the formula. 

   Boolean values of variables, literals, clauses, formulas.
   ---------------------------------------------------------
    An assignment for a formula is a Boolean value for each variable of the 
    dictionary of the formula. 
    Given a formula F and an assignment A:
        The boolean value of a positive literal with variable x is the Boolean
            value of A[x].
        The boolean value of a negative literal with variable x (-x) is the 
            Boolean value of not(A[x]).
        The boolean value of a clause is the logical OR Boolean value 
            of its literals. A clause is 'satisfied' if its value is True.
        The boolean value of a formula is the logical AND Boolean value 
            of its clauses. A formula is 'satisfied' if its value is True.
    
    Illustration.
    ------------
    F = [['a', '-b', 'c'], ['-a', 'b', '-d'], ['a', 'b', 'c'], ['-b', 'd', '-e']]
    The dictionary of F has keys 'a', 'b', 'c', 'd', 'e'
    An example of an assignment:
    {'a':False, 'b':True, 'c':True, 'd':False, 'e':False}
"""


def get_formula_from_file(file):
    """Extract a formula from file and returns it as a list.
    In file:
        A variable is a string (with no ',', no '&', no ' ' and no '-').
        A literal is either:
            a variable (positive literal) or a variable beginning with
            '-' (negative literal).
        Literals in clauses are separated by ','.
        Clauses are separated by '&'.
        Formula is on one line in the file.
    Example of formula: a,-b,cloclo&b,-a,-c&d,-a,-b&-cloclo,-name,-a,-b
    """
    formule = []
    with open(file) as fichier:
        tempo = fichier.readline()
        tempo = tempo.split("&")
        for i in tempo:
            formule.append(i.split(","))
    return formule


def variable_of_literal(literal):
    """Returns the name of the variable of the literal."""
    return literal.strip('-')


def sign_of_literal(literal):
    """Returns the sign of the literal: '-' for a negative literal and
    '+' otherwise."""
    if(literal[0] == '-'):
        return '-'
    else:
        return '+'


def set_of_variables_from_formula(f):
    """Returns the set of the names of variables appearing in the formula."""
    formula_set = set()
    for clause in f:
        for literal in clause:
            formula_set.add(variable_of_literal(literal))
    return formula_set

def construct_dictionary_from_vars(set_of_vars):
    """Constructs a dictionary from the set of variables.
    The value of each entry is None (no assignment)."""
    return {x:None for x in set_of_vars}


def random_assignment(d):
    """Takes a dictionary as input and puts a random Boolean value to each
    variable. """
    for key,_ in d.items():
        d[key] = (random.randint(0, 1) == 0) # mieux : for v in dictionary: dictionary[v] = random.choice([True, False])
    return d #on modifie donc pas besoin de return


def boolean_value_of_literal(assignment, literal):
    """Given an assignment and a literal, returns the Boolean value of the
       literal."""
    val = assignment[variable_of_literal(literal)]
    if sign_of_literal(literal) == '+':
        return val
    else:
        return not val


def boolean_value_of_clause(assignment, clause):
    """Given an assignment and a clause, returns the Boolean value of the
       clause."""
    for litteral in clause:
        if(boolean_value_of_literal(assignment, litteral)):
            return True
    return False
        
def boolean_value_of_formula(assignment, formula):
    """Given an assignment and a formula, returns the Boolean value of the
       formula."""
    for clause in formula:
        if(boolean_value_of_clause(assignment, clause) == False):
            return False
    return True


def number_of_true_clauses(assignment, formula):
    """Given an assignment and a formula, returns the number of clauses having
       a Boolean value True."""
    true_clause = 0
    for clause in formula:
        if(boolean_value_of_clause(assignment, clause)):
            true_clause += 1
    return true_clause


def number_of_clauses(formula):
    """Returns the number of clauses of the formula."""
    return len(formula)


def pretty_print_formula(formula):
    """Print a nice/readable view of the formula."""
    variable = set_of_variables_from_formula(formula)
    biggest_size = max([len(x) for x in variable]) + 1
    for clause in formula:
        to_print = ""
        for lit in clause:
            to_print += str(lit)
            nb_spaces = biggest_size - len(lit)
            to_print += " " * nb_spaces
            to_print += " or "
        print(to_print[:-4])
    

def pretty_print_assigned_formula(assignment, formula):
    """Print a nice/readable view of the formula with each variable replaced
       by its Boolean value; also print the value of each clause. Illustration
       True       not(False) True        = True
       not(True)  False      not(True)   = False
       True       False      True        = True"""
    biggest_size = 10
    for clause in formula:
        to_print = ""
        for lit in clause:
            truth_value = assignment[variable_of_literal(lit)]
            bool_to_print = str(truth_value)
            if sign_of_literal(lit) == '-':
                bool_to_print = "not(" + bool_to_print + ")"
            to_print += bool_to_print
            nb_spaces = biggest_size - len(bool_to_print)
            to_print += " " * nb_spaces
            to_print += " or "
        print(to_print[:-4] + " = " + 
                str(boolean_value_of_clause(assignment, clause)))


def random_formula(n=26, c=10, min_len=1, max_len=10, file="FX"):
    """Generate a random formula with at most n variables, exactly c clauses,
       each with at least min_len literals and at most max_len literals.
    Put the final formula in file.
    Each variable must be a non capital letter (a, b, c,...,z). """
    literal_liste = []
    name_lenght = 1
    while(n > pow(26, name_lenght)):
        name_lenght+=1
    for i in range(n):
        name = ""
        for j in range(name_lenght-1, -1, -1):
            name += chr(97 + (i//pow(26, j))%26)
        literal_liste.append(name)
    with open(file, "w+") as fichier:
        for i in range(c):
            nb_leteral = random.randint(min_len, max_len)
            res_lit = []
            while(len(res_lit) < nb_leteral):
                res_lit.append(literal_liste[random.randint(0, n-1)])
                for verif in range(len(res_lit)-1):
                    if(verif == res_lit[len(res_lit)-1]):
                        res_lit.pop()
                        break
            for m in range(len(res_lit)):
                is_neg = random.randint(0, 1)
                if(is_neg == 0):
                    fichier.write("-")
                fichier.write(res_lit[m])
                if(m != len(res_lit)-1):
                    fichier.write(",")
            if(i < c-1):
                fichier.write("&")
    


def iter_all_assignments(d):
    """An iterator to generate all the possible assignments of a dictionary d.
    NB: the call returns an iterator of assignments, not the assignments."""
    variable = list(d.keys())
    n = len(variable)
    for x in variable:
        d[x] = False
    list_truth = [False] * n
    yield d
    while list_truth != [True] * n:
        for i in range(0, len(list_truth)):
            if list_truth[i]:
                list_truth[i] = False
                d[variable[i]] = list_truth[i]
            else:
                list_truth[i] = True
                d[variable[i]] = list_truth[i]
                break
        yield d


def evaluate_all_assignments(formula):
    """Returns, for each possible assignment of the variables of the formula,
    the list of the number of satisfied clauses (with Boolean value True)."""
    liter_dico = construct_dictionary_from_vars(
                    set_of_variables_from_formula(formula))
    each_assignment = iter_all_assignments(liter_dico)
    list_of_satisfied_Number = []
    for assign in each_assignment:
        satisfied_number_here = number_of_true_clauses(assign, formula)
        list_of_satisfied_Number.append(satisfied_number_here)
    return list_of_satisfied_Number



"""
Example of pretty print of formula a,-b,c&-a,b,-d&a,b,c&-b,d,-e&a,-c,e :
 a or -b or  c
-a or  b or -d
 a or  b or  c
-b or  d or -e
 a or -c or  e

Example of a pretty print of an assignment for this formula:

False      not(False) False       = True
not(False) False      not(False)  = True
False      False      False       = False
not(False) False      not(True)   = True
False      not(False) True        = True """



"""F = get_formula_from_file("FX")
print(F)
print(evaluate_all_assignments(F))"""








"""Voici du code de test à ajouter après la définition de vos fonctions
(à la fin de votre fichier).
Interdiction de modifier les lignes suivantes. Interdition d'utiliser
une autre bibliothèque que random. Seuls les résultats des appels suivants
doivent s'afficher, rien d'autre. """

"""f1 = [['aa', '-bbbb', '-c'], ['-aa', '-bbbb', '-dd'], ['aa', 'bbbb', 'c'],
     ['-bbbb', 'd', '-e']]"""

random_formula()

f1 = get_formula_from_file("FX")
print(f1)
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