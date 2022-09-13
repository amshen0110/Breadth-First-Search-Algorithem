# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 22:28:22 2022

@author: shenb
"""

#BFS path finding

def BFS(graph, node1, node2):
    #g is goal and s is start
    explored_list = []
    queue = [[node1]]
    
    if node1 == node2:
        print("These are the same node")
        return
    
    while queue:
        pathway = queue.pop(0)
        n = pathway[-1]
        
        if n not in explored_list:
            adjacents = graph[n]
            
            for adjacent in adjacents:
                new_pathway = list(pathway)
                new_pathway.append(adjacent)
                queue.append(new_pathway)
                if adjacent == node2:
                    print("The shortest pathway is ", *new_pathway)
                    return
            explored_list.append(n)
    print("A connecting pathway is non existent")
    
    return
    
if __name__ == "__main__":
    
    #graph dictionaries
    graph = {'A': ['B', 'E', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F', 'G'],
            'D': ['B', 'E'],
            'E': ['A', 'B', 'D'],
            'F': ['C'],
            'G': ['C']}
    
    BFS(graph, 'A', 'D')
