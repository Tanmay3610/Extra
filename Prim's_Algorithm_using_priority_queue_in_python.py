#Prims Algorithm
#By: Tanmay Agarwal
from collections import defaultdict
class priority_queue:
    def __init__(self):
        self.pq = []
        self.queue_size = 0

    def print_queue(self):
        print(self.pq)

    @staticmethod
    def parent(key):
        return int((key-1)/2)

    @staticmethod
    def left(key):
        return int((2*key) + 1)

    @staticmethod
    def right(key):
        return int((2*key) + 2)

    def swap(self,a,b):
        temp = self.pq[a]
        self.pq[a] = self.pq[b]
        self.pq[b] = temp

    def not_empty(self):
        if len(self.pq) == 0:
            return False
        return True

    def min_heapify(self,index):
        smallest = index
        index_weight,_ = self.pq[index]
        if priority_queue.left(index) >= 0 and priority_queue.left(index)<self.queue_size:
            left_comparison_weight,_ = self.pq[priority_queue.left(index)]
            if left_comparison_weight < index_weight:
                smallest = priority_queue.left(index)
        if priority_queue.right(index) >= 0 and priority_queue.right(index)<self.queue_size:
            right_comparison_weight,_ = self.pq[priority_queue.right(index)]
            if right_comparison_weight < index_weight:
                smallest = priority_queue.right(index)
        if smallest is not index:
            self.swap(smallest,index)
            self.min_heapify(smallest)
    
    def extract_mini(self):
        ret = self.pq[0]
        self.pq[0] = self.pq[self.queue_size - 1]
        self.queue_size = self.queue_size - 1
        self.pq.pop()
        if self.queue_size != 0:
            self.min_heapify(0)
        return ret

    def push(self,weight,vertex):
        self.pq.append((weight,vertex))
        i = self.queue_size
        self.queue_size = self.queue_size + 1
        weight_parent,_ = self.pq[priority_queue.parent(i)]
        weight_child,_ = self.pq[i]
        while priority_queue.parent(i) >=0 and weight_parent > weight_child:
            self.swap(priority_queue.parent(i),i)
            i = priority_queue.parent(i)
            weight_parent,_ = self.pq[priority_queue.parent(i)]
            weight_child,_ = self.pq[i]

        
class Graph:
    def __init__(self):
        self.pq = priority_queue()
        self.adjacency_list = defaultdict(list)

    def addEdge(self,a,b,c):
        self.adjacency_list[a].append((b,c))
        self.adjacency_list[b].append((a,c))

    def print_graph(self):
        print(self.adjacency_list)

    def get_number_of_nodes(self):
        maximum = 0
        for i in self.adjacency_list:
            maximum = max(maximum,i)
            for j in self.adjacency_list[i]:
                maximum = max(maximum,j[0])
        return maximum
    
    @staticmethod
    def cost_minimum_spanning_tree(minimum_spanning_tree):
        print(minimum_spanning_tree)

    def prims(self,number_of_nodes):
        visited = [False for i in range(number_of_nodes + 1)]
        minimum_spanning_tree = []
        self.pq.push(0,0)
        count = 0
        while self.pq.not_empty() and count < number_of_nodes:
            count = count + 1
            _,min_vertex = self.pq.extract_mini()
            visited[min_vertex] = True
            minimum_spanning_tree.append(min_vertex)
            for j in self.adjacency_list[min_vertex]:
                if visited[j[0]] == False:
                    self.pq.push(j[1],j[0]) 
        Graph.cost_minimum_spanning_tree(minimum_spanning_tree)
        
g = Graph() 
g.addEdge(0, 1, 4) 
g.addEdge(0, 7, 8) 
g.addEdge(1, 2, 8) 
g.addEdge(1, 7, 11) 
g.addEdge(2, 3, 7) 
g.addEdge(2, 8, 2) 
g.addEdge(2, 5, 4)
g.addEdge(3, 4, 9) 
g.addEdge(3, 5, 14) 
g.addEdge(4, 5, 10) 
g.addEdge(5, 6, 2)
g.addEdge(6, 7, 1) 
g.addEdge(6, 8, 6) 
g.addEdge(7, 8, 7)
g.prims(g.get_number_of_nodes())
