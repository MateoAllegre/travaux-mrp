import random
from tkinter import N

"""Each agency has a name (a string) and each candidate has a name (a string).
The same number n of agencies and candidates. 
An instance is:
    + A dictionary containing the choices of the agencies: 
    its keys are the names of agencies and the value of an entry 
    is the list of choices of this agency. 
    + A dictionary containing the choices of the candidates: 
    its keys are the names of candidates and the value of an entry 
    is the list of choices of this candidate.
Each list must be a permutation of the n elements of the choices.

An assignment is: 
    a candidate C for each agency A and 
    an agency A for each candidate C.
    This must be symmetric: A->C iff C->A.
An assignment is represented by two dictionaries. Each element (candidate or 
agency) is a key and its assigned element is a value. 
"""

#------------------------------------------------------------------------------
def extract_instance_from_file(file):
    """Get the instance in the file. Return n + a dictionary containing the
    choices of the n agencies + a dictionary containing the choices of the
    n candidates (return a 3-tuple).
    The format of a file is:
    n (alone on the first line)
    followed by n lists for agencies followed by n lists for candidates.
    Each line is X:Y1:Y2:...:Yn where X is agency or candidate and the Yi's are
    the choices of X. The separator is ':' with no space between elements."""
    n = -1
    choix_agences = {}
    choix_candidats = {}
    with open(file, "r", encoding="utf8") as f:
        n = int(next(f))
        
        # Création du dictionnaire des choix des agences
        for i in range(n):
            l = next(f)
            data = l.split(":")
            data[-1] = data[-1][:-1] # Enlève le '\n' en retirant le dernier caractère du dernier "champ"
            choix_agences[data[0]] = data[1:]
            
        # Création du dictionnaire des choix des candidats
        for i in range(n):
            l = next(f)
            data = l.split(":")
            data[-1] = data[-1][:-1] # Enlève le '\n' en retirant le dernier caractère du dernier "champ"
            choix_candidats[data[0]] = data[1:]
            
    # Correction : On peut enlever le \n et split avec : data = line.strip().split(":")
            
    return n, choix_agences, choix_candidats

#------------------------------------------------------------------------------
def is_coherent(choices_agencies, choices_candidates):
    """Function that verifies if the two dictionaries are coherent i.e. if
     each value is a list containing each appropriated element exactly once.
      Returns True if it is the case and raises an
      Exception('Incorrect choices') otherwise."""
    pass


#------------------------------------------------------------------------------
def generate_random_instance(n, version_number=1):
    """Generate a random instance with n agencies, n candidates and put the
    result in a file that is named GSEntries_Rand_{n}_{version_number}
    (for example GSEntries_Rand_10_3) to distinguish different random files."""
    pass


#------------------------------------------------------------------------------
def is_assignment_symmetric(agen_assignment, candidate_assignment):
    """Boolean function that returns True if the assignments are coherent,
    symmetric."""
    pass


#------------------------------------------------------------------------------
def number_of_non_stable_couples(agencies_assign, candidates_assign,
                                 agencies_choices, candidates_choices):
    """Returns the number of non stable couples in the assignment."""
    nsc = 0     # Nombre de couples non stables
    for a in agencies_choices.keys():
        a_choices = agencies_choices[a]
        index_max = a_choices.index(agencies_assign[a])
        for c in a_choices[:index_max]:
            c_choices = candidates_choices[c]
            if c_choices.index(a) < c_choices.index(candidates_assign[c]):
                nsc += 1
    return nsc


#------------------------------------------------------------------------------
def generate_random_assignment(agencies_choices, candidates_choices):
    """Returns a random assignment as a 2 tuple of dictionaries."""
    agency_to_candidate = {}
    candidate_to_agency = {}
    agencies = {i for i in agencies_choices.keys()}
    candidates = {i for i in candidates_choices.keys()}
    for a in agencies:      # Note : à cause des sets, on n'a pas de garantie sur l'ordre
        c = random.choice(list(candidates))
        agency_to_candidate[a] = c
        candidate_to_agency[c] = a
        candidates.discard(c)
    return agency_to_candidate, candidate_to_agency

#------------------------------------------------------------------------------
"""
# Correction de la fonction du dessus
def correc_generate_random_assignment(agencies_choices, candidates_choices):
    list_of_candidates = list(candidates_choices.keys())
    random.shuffle(list_of_candidates)
    agencies_assignment = {a : c for a, c in zip(agencies_choices.keys(), list_of_candidates)}
    candidates_assignment = {c : a for a, c in agencies_assignment.items()}
    return agencies_assignment, candidates_assignment
"""
#------------------------------------------------------------------------------

# A partir d'une instance, renvoie un 2 tuple contenant le nombre minimal de NSC trouvé et l'assignment qui le minimise (celui-ci étant un 2 tuple comme défini plus haut)
def find_best_assignment(n, agencies_choices, candidates_choices):
    min_nsc = n*n
    nbExp = 10000
    for i in range(nbExp):
        agen_assi, cand_assi = generate_random_assignment(agencies_choices, candidates_choices)
        nsc = number_of_non_stable_couples(agen_assi, cand_assi, agencies_choices, candidates_choices)
        if nsc < min_nsc:
            min_nsc = nsc
            best_assignment = (agen_assi, cand_assi)
        if min_nsc == 0:
            return min_nsc, best_assignment

    return min_nsc, best_assignment

#------------------------------------------------------------------------------
def print_affectation(assignment, list_agencies):
    for agency in list_agencies:
        print(agency + "  " + assignment[0][agency])

#------------------------------------------------------------------------------
def gale_shapley(agencies_choices, candidates_choices):
    # Dictionnaires pour stocker l'affectation
    agen_assi = {}
    cand_assi = {}

    # Liste d'agences/candidats non liés par l'affectation
    list_free_agencies = list(agencies_choices.keys())
    list_free_candidates = list(candidates_choices.keys())

    # Dictionnaires contenant un itérateur sur les choix pour chaque agence
    iterateurs = {a:iter(agencies_choices[a]) for a in agencies_choices.keys()}

    while len(list_free_agencies) > 0: # Tant qu'il reste des agences libres

        agency = list_free_agencies[0] # Agence qu'on traite (parmi les libres)
        pot_cand = next(iterateurs[agency]) # Candidat potentiel : choix favori de l'agence (parmi ceux qui restent)

        # CAS 1 : Candidat non lié
        if pot_cand in list_free_candidates:
            # On lie le candidat et l'agence ("de force")
            agen_assi[agency] = pot_cand
            cand_assi[pot_cand] = agency

            # le candidat et l'agence ne sont plus libres
            list_free_candidates.remove(pot_cand) 
            list_free_agencies.remove(agency)

        # CAS 2 : Candidat lié
        else:
            # Liste des choix du candidat potentiel
            pot_cand_ch = candidates_choices[pot_cand]

            # CAS 2a: le candidat préfère la nouvelle agence à la sienne
            if pot_cand_ch.index(agency) < pot_cand_ch.index(cand_assi[pot_cand]):
                # L'agence n'est plus libre mais l'ancienne agence du candidat le devient
                list_free_agencies.remove(agency)
                list_free_agencies.append(cand_assi[pot_cand])

                # L'ancienne agence n'est plus liée au candidat ("divorce")
                agen_assi.pop(cand_assi[pot_cand])

                # On lie le candidat et l'agence
                agen_assi[agency] = pot_cand
                cand_assi[pot_cand] = agency

    # CAS 2b : si le candidat préférait son ancienne agence, on ne fait rien (l'itérateur s'en occupe)

    # On retourne les deux dictionnaires (i.e. l'affectation)
    return agen_assi, cand_assi

#------------------------------------------------------------------------------

def random_instance(n):
    list_agencies = ["A" + str(i) for i in range(n)]
    list_candidates = ["C" + str(i) for i in range(n)]
    agencies_choices = {}
    candidates_choices = {}
    for a in list_agencies:
        random.shuffle(list_candidates)
        agencies_choices[a] = list_candidates
    for c in list_candidates:
        random.shuffle(list_agencies)
        candidates_choices[c] = list_agencies
    return n, agencies_choices, candidates_choices

#------------------------------------------------------------------------------

def test_gale(nbExp=10000, minN=4, maxN=42):
    for i in range(nbExp):
        _, agencies_choices, candidates_choices = random_instance(random.randint(minN, maxN))
        agen_assign, cand_assign = gale_shapley(agencies_choices, candidates_choices)
        if number_of_non_stable_couples(agen_assign, cand_assign, agencies_choices, candidates_choices) != 0:
            print("oh non :(")
    print("fini")
        

############################

# Ancien tests
n, agencies_choices, candidates_choices = extract_instance_from_file("ex2.txt")
random_assign = generate_random_assignment(agencies_choices, candidates_choices)
print(random_assign[0])
print(number_of_non_stable_couples(random_assign[0], random_assign[1], agencies_choices, candidates_choices))

print('---')

n, agencies_choices, candidates_choices = extract_instance_from_file("ex.txt")
min, a = find_best_assignment(n, agencies_choices, candidates_choices)
print(min)
print_affectation(a, list(agencies_choices.keys()))

print('---')

n, agencies_choices, candidates_choices = extract_instance_from_file("ex3.txt")
print_affectation(gale_shapley(agencies_choices, candidates_choices), list(agencies_choices.keys()))

print('---')

test_gale()