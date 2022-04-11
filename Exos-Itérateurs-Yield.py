# Exercices Python sur les itérateurs, yield, yield from.
# Utilisez chaque itérateur pour produire des éléments. 

#------------------------------------------------------------------------------
def iter_syracuse(n):
    """Prend en entrée un entier n>0. Retourne un itérateur sur les éléments de
    la suite de syracuse lorsque le terme initial est n."""
    # PAIR : /2
    # IMPAIR : *3 + 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        yield n

#------------------------------------------------------------------------------
def iter_fibo():
    """Générateur des éléments de la suite de Fibonacci."""
    a = 0
    b = 1
    while True:
        a,b = b,a+b
        yield a

#------------------------------------------------------------------------------
def look_and_say_iter(z, k=1):
    """La suite Look and say mise en oeuvre avec un itérateur."""
    yield z
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
        yield z

#------------------------------------------------------------------------------
def iter_tous_les_facteurs(mot):
    """Création d'un itérateur qui génére tous les facteurs non vides du mot
    donné en paramètre. Exemple : tous les facteurs de la chaine "abcd" sont :
    a ab abc abcd b bc bcd c cd d """ 
    for dep in range(len(mot)):
        for fin in range(dep,len(mot)):
            yield mot[dep:fin+1]

#------------------------------------------------------------------------------
def iter_toutes_les_listes_binaires(n):
    """Itérateur produisant toutes les listes de {0, 1} de taille n."""
    L = [0] * n
    yield L
    
    while L != [1] * n:
        for i in range(0, len(L)):
            if L[i] == 1:
                L[i] = 0
            else:
                L[i] = 1
                break
        yield L

#------------------------------------------------------------------------------

def est_premier(n):
    if n == 1:
        return False
    
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

#------------------------------------------------------------------------------
def iter_nombres_premiers(v=1):
    """Itérateur produisant tous les nombres premiers à partir de v."""
    while True:
        if est_premier(v):
            yield v
        v += 1

#------------------------------------------------------------------------------
        
##def iter_tous_les_sous_ensembles(ensemble):
##    """Itérateur produisant tous les sous-ensembles possibles de l'ensemble
##    donné en entrée."""
##    liste = list(ensemble)
##    n = len(ensemble)
##
##    L = [0] * n
##    yield set()
##    
##    while L != [1] * n:
##        for i in range(0, n):
##            if L[i] == 1:
##                L[i] = 0
##            else:
##                L[i] = 1
##                break
##            
##        sous_ens = set()
##        for i in range(0, n):
##            if L[i] == 1:
##                sous_ens.add(liste[i])
##        yield sous_ens

def iter_tous_les_sous_ensembles(ensemble):
    liste = list(ensemble)
    n = len(ensemble)

    it = iter_toutes_les_listes_binaires(n)
    
    for L in it:
        sous_ens = set()
        for i in range(0, n):
            if L[i] == 1:
                sous_ens.add(liste[i])
        yield sous_ens

#------------------------------------------------------------------------------

it = iter_syracuse(46)
for i in it:
    print(i)

print("---")

fibo = iter_fibo()
for i in range(10):
    print(next(fibo))

print("---")

las = look_and_say_iter('1', 10)
for i in las:
    print(i)

print("---")

fact = iter_tous_les_facteurs("abcd")
for i in fact:
    print(i)

print("---")

bin = iter_toutes_les_listes_binaires(5)
for i in bin:
    print(i)

print("---")

prime = iter_nombres_premiers(1)
for i in range(20):
    print(next(prime))

print("---")

sous_ens = iter_tous_les_sous_ensembles({1,2,3,4,5,6})
for i in sous_ens:
    print(i)

print("---")

print("Done")
