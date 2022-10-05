from collections import defaultdict 


class Graph: 

    def __init__(self): 
        self.edges = defaultdict(list) 
    
    def addEdge(self, u, v): 
        self.edges[u].append(v)
        
    def generate_random_graph(self, distribution): 
        """TODO: Create this """
    
class CountRepublicans(Graph): 
    def __init__(self): 
        super.__init__() 
    
    def DFS(self, start_node): 
        """
        Depth first search from start_node, returns count 
        of all members who are republicans
        """


network = Graph() 
network.generate_random_graph(Proaility distribution) 
network.DFS(startnode)