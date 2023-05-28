class Kruksal:
    def __init__(self,indextices):
        self.V = indextices
        self.graph=[]
    
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
    
    def find(self,parent,node):
        if (parent[node]==node):
            return node                                 #recursion until self parent doesnt occur
        parent[node]= self.find(parent,parent[node])
        return parent[node]                             #path compression
    
    def union(self,parent,rank,x,y):

        x_parent = self.find(parent,x)      #find parent of both
        y_parent = self.find(parent,y)

        if rank[x_parent] < rank[y_parent]:
            parent[x] = y_parent
            rank[y_parent]+=1
        elif rank[x_parent] > rank[y_parent]:
            parent[y] = x_parent
            rank[x_parent]+=1
        else:
            parent[y]= x_parent
            rank[x_parent]+=1
    
    def kruskalAlgo(self):
        parent=[]
        rank=[]
        mst=[]

        index,edges =0,0

        self.graph= sorted(self.graph,key=lambda item:item[2])         #sorting the graph based on weight

        for node in range(self.V):      #initializing self parent and rank 0 
            parent.append(node)
            rank.append(0)
        
        while edges < self.V-1:             #upto indextices-1 edges in mst (rule)
            u,v,w= self.graph[index]
            index+=1
            u_parent= self.find(parent,u)
            v_parent= self.find(parent,v)

            if u_parent!=v_parent:
                edges+=1
                mst.append([u,v,w])
                self.union(parent,rank,u,v)         #Watch out here
            
        print("Mininmum Spanning Tree: ")
        for u,v,w in mst:
            print(f"{u} - {v}: {w}")


g= Kruksal(4)
g.addEdge(0,1,10)
g.addEdge(0,2,6)
g.addEdge(0,3,5)
g.addEdge(1,3,15)
g.addEdge(2,3,4)

g.kruskalAlgo()

