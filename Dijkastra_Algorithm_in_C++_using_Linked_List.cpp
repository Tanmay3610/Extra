//Dijkastra Algorithm in C++ using Linked List
//By: Tanmay Agarwal
#include <bits/stdc++.h>
using namespace std;

typedef struct alist{
	int weight;
	int vertex;
	alist *next;
}alist;

typedef struct Node{
	int vertex;
	Node *next;
	alist *list_head;
}Node;

Node *head = NULL;
Node *p = NULL;

void add_vertex(int b, int c, Node *itr){
	alist *p1 = itr->list_head;
	while(p1->next != NULL)
		p1 = p1->next;
	alist *new_vertex = (alist*)malloc(sizeof(alist));
	new_vertex->next = NULL;
	new_vertex->vertex = b;
	new_vertex->weight = c;
	p1->next = new_vertex;
}

void add_node(int a, int b, int c){
	Node *new_node = (Node*)malloc(sizeof(Node));
	new_node->vertex = a;
	new_node->next = NULL;
	alist *new_vertex = (alist*)malloc(sizeof(alist));
	new_vertex->vertex = b;
	new_vertex->weight = c;
	new_vertex->next = NULL;
	new_node->list_head = new_vertex;
	if(head == NULL)
		head = new_node;
	else{
		p = head;
		while(p->next != NULL)
			p = p->next;
		p->next = new_node;
	}
}

void find_edge(int a, int b, int c){
	int flag = 0;
	p = head;
	while(p != NULL){
		if(p->vertex == a){
			add_vertex(b,c,p);
			flag = 1;
			break;
		}
		p = p->next;
	}
	if (flag == 0)
		add_node(a,b,c);
}

void add_edge(int a, int b, int c){
	find_edge(a,b,c);
}

void show(){
	cout<<"--------------------"<<endl;
	cout<<"Adjacecny List of the graph"<<endl;
	cout<<"--------------------"<<endl;
	p = head;
	while(p != NULL){
		cout<<p->vertex<<"->";
		alist *p1 = p->list_head;
		while(p1 != NULL){
			cout<<p1->vertex<<"("<<p1->weight<<"),";
			p1 = p1->next;
		}
		cout<<endl;
		p = p->next;
	}
	cout<<"--------------------"<<endl;
}

void show_result(int *distance, int n){
	cout<<"--------------------"<<endl;
	cout<<"Dijkastra Algorith result"<<endl;
	cout<<"--------------------"<<endl;
	cout<<"Minimum Distance from 0 to:"<<endl;
	for (int i = 0; i<n+1; i++){
		if (distance[i]>1000000 || distance[i] < -1000000)
			cout<<i<<" is not connected to 0"<<endl;
		else cout<<i<<" is "<<distance[i]<<endl;
	}		
	cout<<"--------------------"<<endl;
}

int find_min_vertex(bool *visited, int *distance, int n){
	int min_vertex = -1;
	for(int i = 0; i<n+1; i++){
		if(!visited[i]){
			if(min_vertex == -1 || distance[min_vertex] > distance[i])
				min_vertex = i;
		}
	}
	return min_vertex;
}

Node* find_pointer(int min_vertex){
	p = head;
	int flag = 0;
	while(p != NULL){
		if(p->vertex == min_vertex){
			flag = 1;
			break;
		}			
		p = p->next;
	}
	if (flag == 1)
		return p;
	return NULL;
}

void dijkastra(int n){
	bool visited[n+1];
	for(int i = 0; i<n+1; i++)
		visited[i] = false;
	int distance[n+1];
	for(int i = 0; i<n+1; i++)
		distance[i] = INT_MAX;
	distance[0] = 0;
	for(int i = 0; i<n; i++){
		int min_vertex = find_min_vertex(visited,distance,n);
		visited[min_vertex] = true;
		Node *ptr = find_pointer(min_vertex);
		if (ptr == NULL)
			continue;
		alist *p1 = ptr->list_head;
		while(p1 != NULL){
			if(!visited[p1->vertex]){
				int dist = distance[min_vertex] + p1->weight;
				if(dist<distance[p1->vertex])
					distance[p1->vertex] = dist;
			}
			p1 = p1->next;
		}
	}
	show_result(distance,n);
}

int get_number_of_nodes(){
	int number = 0;
	p = head;
	while(p != NULL){
		number = max(number,p->vertex);
		alist *p1 = p->list_head;
		while(p1 != NULL){
			number = max(number,p1->vertex);
			p1 = p1->next;
		}
		p = p->next;
	}
	return number;
}

int main(){
	add_edge(0,2,4);
	add_edge(1,4,1);  
	add_edge(4,8,1);  
	add_edge(4,7,1);  
	add_edge(7,9,1);  
	add_edge(9,12,1); 
	add_edge(8,10,1); 
	add_edge(10,13,1);
	add_edge(10,12,1);
	add_edge(5,1,1);  
	add_edge(5,4,1);  
	add_edge(5,6,1);  
	add_edge(6,11,1); 
	add_edge(11,10,1);
	add_edge(3,2,1);  
	add_edge(2,4,1);  
	add_edge(8,9,1);
	int number_of_nodes = get_number_of_nodes();  
	dijkastra(number_of_nodes);
	show();
	return 0;
}
