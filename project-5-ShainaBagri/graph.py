from stack_array import * #Needed for Depth First Search
from queue_array import * #Needed for Breadth First Search

class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = {}
        self.visited = False
        self.color = "White"

    def __repr__(self):
        return ("{!r} : {!r}").format(self.id, self.adjacent_to)


class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        try:
            f = open(filename, "r")
            if f.mode == 'r':
                text = f.read()
            f.close()
        except:
            raise FileNotFoundError
        vertices = text.split()
        self.lis = {}
        i = 0
        while i < len(vertices):
            v1 = vertices[i]
            v2 = vertices[i + 1]
            if v2 not in self.lis:
                self.lis[v2] = Vertex(v2)
            if v1 not in self.lis:
                self.lis[v1] = Vertex(v1)
            self.lis[v1].adjacent_to[v2] = self.lis[v2]
            self.lis[v2].adjacent_to[v1] = self.lis[v1]
            i += 2

    def add_vertex(self, key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        if key not in self.lis:
            self.lis[key] = Vertex(key)

    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        if key in self.lis:
            return self.lis[key]
        return None

    def add_edge(self, v1, v2):
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        self.lis[v1].adjacent_to[v2] = self.lis[v2]
        self.lis[v2].adjacent_to[v1] = self.lis[v1]

    def get_vertices(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        verts = []
        for i in self.lis:
            verts.append(i)
        verts.sort()
        return verts

    def conn_components(self): 
        '''Returns a list of lists.  For example, if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''
        ans = []
        popped = 0
        verts = self.get_vertices()
        z = 0
        s = Stack(1000)
        while popped<len(self.lis):
            templis = []
            while self.lis[verts[z]].visited:
                z += 1
            s.push(verts[z])
            while not s.is_empty():
                v = s.pop()
                if not self.lis[v].visited:
                    self.lis[v].visited = True
                    popped += 1
                    templis.append(v)
                    rev = []
                    for i in self.lis[v].adjacent_to:
                        rev.append(i)
                    for i in range(len(rev)):
                        s.push(rev[len(rev)-i-1])
            templis.sort()
            ans.append(templis)
        return ans

    def is_bipartite(self):
        '''Returns True if the graph is bicolorable and False otherwise.
           This method MUST use Breadth First Search logic!'''
        for i in self.lis:
            self.lis[i].color = "White"
        popped = 0
        verts = self.get_vertices()
        z = 0
        q = Queue(1000)
        while popped<len(self.lis):
            while self.lis[verts[z]].color!="White":
                z += 1
            q.enqueue(verts[z])
            while not q.is_empty():
                v = q.dequeue()
                if self.lis[v].color=="White":
                    self.lis[v].color = "Black"
                    popped += 1
                    first = True
                    for i in self.lis[v].adjacent_to:
                        q.enqueue(i)
                        if self.lis[v].adjacent_to[i].color == self.lis[v].color and first:
                            if self.lis[v].color == "Black":
                                self.lis[v].color = "Red"
                            elif self.lis[v].color == "Red":
                                self.lis[v].color = "Black"
                        elif self.lis[v].adjacent_to[i].color == self.lis[v].color and not first:
                            return False
                        if self.lis[v].adjacent_to[i].color != "White":
                            first = False
        return True
