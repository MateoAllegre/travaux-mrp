# This file must be renamed Special_Graphs.py

# ------ Hypercube graphs -------

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

def list_to_str(l):
    str_from_list = ""
    for i in l:
        str_from_list += str(i)
    return str_from_list

def hypercube_graph(d):
    """Constructs the hypercube graph of dimension d and write it in file Hd.
    Each vertex is associated to a binary word of length d.
    For example '001101' is a vertex of hypercube of dimension 6.
    Two vertices are neighbors iff they differ on exactly one bit.
    For example, 01001 and 01101 are neighbors in hypercube(5)."""
    with open("H" + str(d), "w") as f:
        for binary_list in iter_toutes_les_listes_binaires(d):
            f.write(list_to_str(binary_list))
            for i in range(d):
                neighbor = binary_list.copy()
                neighbor[i] = 0 if neighbor[i] == 1 else 1
                f.write(":" + list_to_str(neighbor))
            f.write('\n')

        # Erase last \n
        f.seek(f.tell()-1)
        f.truncate()


# ------ Complete graphs -------

def complete_graph(n):
    """Constructs a complete graph of n vertices and write it in file Kn."""
    with open("K" + str(n), "w") as f:
        for binary_list in iter_toutes_les_listes_binaires(n):
            f.write(list_to_str(binary_list))
            for neighbor in iter_toutes_les_listes_binaires(n):
                f.write(":" + list_to_str(neighbor))
            f.write('\n')
            
        # Erase last \n
        f.seek(f.tell()-1)
        f.truncate()

# ------ Grid graphs -------

def format_vertex(x, y):
    return f"({x},{y})"

def grid_graph(p, q):
    """Constructs a grid pXq and write it in file GridpXq."""
    with open("Grid" + str(p) + "X" + str(q), "w") as f:
        for x in range(p):
            for y in range(q):
                f.write(format_vertex(x, y))
                if x != 0:
                    f.write(":" + format_vertex(x-1, y))
                if y != 0:
                    f.write(":" + format_vertex(x, y-1))
                if x != p-1:
                    f.write(":" + format_vertex(x+1, y))
                if y != q-1:
                    f.write(":" + format_vertex(x, y+1))
                f.write('\n')

        # Erase last \n
        f.seek(f.tell()-1)
        f.truncate()

# ------ Torus graphs -------

def torus_graph(p, q):
    """Constructs a torus pXq and write it in file ToruspXq."""
    with open("Torus" + str(p) + "X" + str(q), "w") as f:
        for x in range(p):
            for y in range(q):
                f.write(format_vertex(x, y))
                f.write(":" + format_vertex((x-1) % p,     y    ))
                f.write(":" + format_vertex(    x    , (y-1) % q))
                f.write(":" + format_vertex((x+1) % p,     y    ))
                f.write(":" + format_vertex(    x    , (y+1) % q))
                f.write('\n')

        # Erase last \n
        f.seek(f.tell()-1)
        f.truncate()

# hypercube_graph(5)
# complete_graph(3)
# grid_graph(3,5)
# torus_graph(4,3)