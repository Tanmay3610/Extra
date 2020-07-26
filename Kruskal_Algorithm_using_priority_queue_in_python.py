#Kruskal Algorithm using priority queue
#By: Tanmay Agarwal
from collections import defaultdict

class priority_queue:
    def __init__(self):
        self.pq = []
        self.queue_size = 0

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

    def print_queue(self):
        print(self.pq)

    def push(self,weight,vertex_a, vertex_b):
        self.pq.append((weight,vertex_a,vertex_b))
        i = self.queue_size
        self.queue_size = self.queue_size + 1
        parent_weight,_,_ = self.pq[priority_queue.parent(i)]
        child_weight,_,_ = self.pq[i]
        while priority_queue.parent(i) >= 0 and parent_weight>child_weight:
            self.swap(priority_queue.parent(i),i)
            i = priority_queue.parent(i)
            parent_weight,_,_ = self.pq[priority_queue.parent(i)]
            child_weight,_,_ = self.pq[i]

    def not_empty(self):
        if len(self.pq) == 0:
            return False
        return True
    
    def min_heapify(self,index):
        smallest = index
        index_weight,_,_ = self.pq[index]
        if priority_queue.right(index) >= 0 and priority_queue.right(index)<self.queue_size:
            right_comparison_weight,_,_ = self.pq[priority_queue.right(index)]
            if right_comparison_weight < index_weight:
                smallest = priority_queue.right(index)
        if priority_queue.left(index) >= 0 and priority_queue.left(index)<self.queue_size:
            left_comparison_weight,_,_ = self.pq[priority_queue.left(index)]
            if left_comparison_weight < index_weight:
                smallest = priority_queue.left(index)
        if smallest is not index:
            self.swap(smallest,index)
            self.min_heapify(smallest)

    def extract_mini(self):
        ret = self.pq[0]
        self.pq[0] = self.pq[self.queue_size - 1]
        self.queue_size = self.queue_size - 1
        self.pq.pop()
        if self.queue_size is not 0:
            self.min_heapify(0)
        return ret
                    
class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)
        self.pq = priority_queue()

    def addEdge(self,a,b,c):
        self.adjacency_list[a].append((b,c))
        self.adjacency_list[b].append((a,c))
        
    def print_graph(self):
        print(self.adjacency_list)

    def get_number_of_nodes(self):
        maximum = 0
        for i in self.adjacency_list:
            maximum = max(i,maximum)
            for j in self.adjacency_list[i]:
                maximum = max(maximum,j[0])
                maximum = max(maximum,j[1])
        return maximum

    def kruskal(self,number_of_nodes):
        visited = [False for i in range(number_of_nodes + 1)]
        result = []
        for i in self.adjacency_list:
            for j in self.adjacency_list[i]:
                self.pq.push(j[1],i,j[0])
        self.pq.print_queue()
        count = 0
        while self.pq.not_empty() and count < number_of_nodes + 1:
            count = count + 1
            _,min_vertex,_ = self.pq.extract_mini()
            visited[min_vertex] = True
            result.append(min_vertex)
            for i in self.adjacency_list[min_vertex]:
                if visited[i[1]] == False:
                    weight = i[0]
                    vertex_a = i[1]
                    vertex_b = min_vertex
                    self.pq.push(weight,vertex_a,vertex_b)
        print(result)

g = Graph()
g.addEdge(0,1,2)
g.addEdge(1,2,3)
g.addEdge(2,3,1)
number_of_nodes = g.get_number_of_nodes()
g.kruskal(number_of_nodes)
g.print_graph()
