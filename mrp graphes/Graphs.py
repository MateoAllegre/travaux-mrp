import queue
import random
import Special_Graphs

"""A vertex is a string.
A graph is a dictionary; its keys are vertices and the value associated to a
key/vertex u is the set of neighbors of u in G.
"""

def extract_graph_from_file(file):
    """Takes a file name as input and extracts the graph inside it.
    The file is composed of n lines, where n is the total number of vertices.
    Each line is of the form u:v1:v2:...:vk where u is a vertex and the
    vi's are its neighbors. If u has no neighbor, the corresponding line is u:
    This function returns a dictionary representing the graph:
    Its keys are vertices and its values are the sets of neighbors
    of each vertex. """
    graph = {}
    with open(file, "r", encoding="utf8") as f:
        for ligne in f:
            ligne_liste = ligne.strip('\n').split(':')
            graph[ligne_liste[0]] = {vertex for vertex in ligne_liste[1:]}
    return graph

def set_of_vertices(graph):
    """Returns the set of vertices of the graph."""
    return set(graph.keys())

def set_of_neighbors(graph, u):
    """Returns the set of neighbors of vertex u in the graph."""
    return graph[u]


def degree_of(graph, u):
    """Returns the numbers of neighbors of vertex u in the graph."""
    return len(graph[u])


def are_neighbors(graph, u, v):
    """Boolean function returning True if u and v are neighbors in the graph.
     Returns False otherwise."""
    return u in graph[v]


def number_of_vertices(graph):
    """Returns the number of vertices of the graph."""
    return len(set_of_vertices(graph))


def number_of_edges(graph):
    """Returns the number of edges of the graph.
    We suppose that it is NON directed."""
    somme = 0
    for vertex in set_of_vertices(graph):
        somme += degree_of(graph, vertex)
    return int(somme/2) # Each edge is counted twice

def is_symmetric(graph):
    """Boolean function returning True if the dictionary representing the graph
    is symmetric: u is a neighbor of v iff v is a neighbor of u.
    Returns False otherwise and print a non symmetric couple."""
    for vertex in set_of_vertices(graph):
        for neighbor in set_of_neighbors(graph, vertex):
            if vertex not in set_of_neighbors(graph, neighbor):
                return False
    return True


def bfs(graph, r):
    """Makes the BFS of the graph from vertex r. Returns a tuple
    (parent, d, color)."""
    parent = {}
    d = {}
    color = {}
    for u in set_of_vertices(graph):
        if u != r:
            color[u] = "BLANC"
            d[u] = 1000000
            parent[u] = None
    color[r] = "GRIS"
    d[r] = 0
    parent[r] = None
    F = [r]
    while len(F) > 0:
        u = F[0]
        for v in set_of_neighbors(graph, u):
            if color[v] == "BLANC":
                color[v] = "GRIS"
                d[v] = d[u] + 1
                parent[v] = u
                F.append(v)
        F.pop(0)
        color[u] = "NOIR"
    return parent, d, color

def color_graph_by_list(graph, list_of_vertices):
    """Takes as input a graph and a list of its vertices. This function colors
    the graph with this list and returns a tuple (c, color) where:
     + color is the constructed coloration (a dictionary whose keys are the
     vertices and values are colors (integers > 0)) and
     + c is the number of colors used by the coloration color."""
    c = 1
    color = {}
    for u in list_of_vertices:
        u_color = 1
        forbidden_colors = set()
        for v in set_of_neighbors(graph, u):
            if v in color.keys():
                forbidden_colors.add(color[v])
        while u_color in forbidden_colors:
            u_color += 1
        color[u] = u_color
        if u_color > c:
            c = u_color
    return c, color

def color_graph_by_random_lists(graph, number_of_iterations=1):
    """Takes as input a graph, and an integer number_of_iterations.
    Runs number_of_iterations times the coloring function of the graph on
    random lists of vertices of the graph and returns the best coloring found
    (the one using the lowest number of colors)."""
    list_of_vertices = list(set_of_vertices(graph))
    min_c = -1
    for i in range(number_of_iterations):
        random.shuffle(list_of_vertices)
        c, color = color_graph_by_list(graph, list_of_vertices)
        if min_c == -1 or c < min_c:
            min_c = c
            best_coloring = color
    return best_coloring

def is_stable(graph, set_s):
    """Boolean function taking as input a graph and a set of vertices.
    It returns True if this set is a stable of the graph (there is no edge
     between vertices of this set in the graph).
     Returns False otherwise."""
    for u in set_s:
        for v in set_s:
            if are_neighbors(graph, u, v):
                return False
    return True

def is_proper_coloring(graph, color):
    """Takes as input a graph and a coloring (a dictionary having the set of
    vertices as keys and colors (integers > 0) as values).
    Returns True if color is a proper coloring of the graph.
    Returns False otherwise and print a message to indicate the error."""
    for u in set_of_vertices(graph):
        for v in set_of_vertices(graph):
            if are_neighbors(graph, u, v) and color[u] == color[v]:
                print(f"{u} et {v} sont adjacents et de la même couleur : {color[u]}")
                return False
    return True