from sys import argv
from stack_array import *

class Vertex:
    def __init__(self, name):
        self.name = name
        self.adj_lis = {}
        self.in_deg = 0

    def __repr__(self):
        return ("{!r} : [{!r}] {!r}").format(self.name, self.adj_lis, self.in_deg)

def tsort(vertices):
    '''
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * identically to the Unix utility {@code tsort}.  That is, one vertex per
    * line in topologically sorted order.
    *
    * Raises a ValueError if:
    *   - vertices is emtpy with the message "input contains no edges"
    *   - vertices has an odd number of vertices (incomplete pair) with the
    *     message "input contains an odd number of tokens"
    *   - the graph contains a cycle (isn't acyclic) with the message 
    *     "input contains a cycle"'''
    if len(vertices)==0:
        raise ValueError("input contains no edges")
    if len(vertices)%2==1:
        raise ValueError("input contains an odd number of tokens")

    #Adjacency List Implementation of Graph
    lis = {}
    i = 0
    while i < len(vertices):
        v1 = vertices[i]
        v2 = vertices[i+1]
        if v1 == v2:
            raise ValueError("input contains a cycle")
        if v2 not in lis:
            lis[v2] = Vertex(v2)
        if v1 not in lis:
            lis[v1] = Vertex(v1)
        lis[v1].adj_lis[v2] = lis[v2]
        lis[v2].in_deg += 1
        i += 2

    #Tsort
    s = Stack(len(lis))
    ans = ""
    for i in lis:
        if lis[i].in_deg==0:
            s.push(i)
    num_pop = 0
    while not s.is_empty():
        v = s.pop()
        num_pop += 1
        if num_pop==len(lis):
            ans = ans + lis[v].name
        else:
            ans = ans + lis[v].name + "\n"
        lis[v].in_deg = -1
        for j in lis[v].adj_lis:
            lis[j].in_deg -= 1
            if lis[j].in_deg==0:
                s.push(j)
    if num_pop<len(lis):
        raise ValueError("input contains a cycle")
    return ans

def main():
    '''Entry point for the tsort utility allowing the user to specify
       a file containing the edge of the DAG'''
    if len(argv) != 2:
        print("Usage: python3 tsort.py <filename>")
        exit()
    try:
        f = open(argv[1], 'r')
    except FileNotFoundError as e:
        print(argv[1], 'could not be found or opened')
        exit()
    
    vertices = []
    for line in f:
        vertices += line.split()
       
    try:
        result = tsort(vertices)
        print(result)
    except Exception as e:
        print(e)
    
if __name__ == '__main__': 
    main()
