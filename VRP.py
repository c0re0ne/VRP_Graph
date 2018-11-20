#!/usr/bin/python3

# https://developers.google.com/optimization/routing/vrp

import os
import csv
import matplotlib.pyplot as plt
import networkx as nx

with open("data.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    string = '['
    counter = 0
    
    for row in reader:
        if (row[0]!="x" and row[1]!="y"):
            string += "("
            #string += str(row[0])
            string += row[0]
            string += ", "
            #string += str(row[1])
            string += row[1]
            string += "), "
            
    string += "]"
    string.replace("),]", ")]")
    print (string)
    #_locations = \

csvfile.close()

        
G=nx.DiGraph()

"""

if (row[1]!=0):
    m = -1
else:
    m = 1

G.add_node(counter, pos=(row[0], m*row[1]))
counter = counter + 1
"""

# Add nodes by specifying their positions
#"""
G.add_node('0', pos=(4, -4))
G.add_node('1', pos=(2, 0))
G.add_node('2', pos=(8, 0))
G.add_node('3', pos=(0, -1))
G.add_node('4', pos=(1, -1))
G.add_node('5', pos=(5, -2))
G.add_node('6', pos=(7, -2))
G.add_node('7', pos=(3, -3))
G.add_node('8', pos=(6, -3))
G.add_node('9', pos=(5, -5))
G.add_node('10', pos=(8, -5))
G.add_node('11', pos=(1, -6))
G.add_node('12', pos=(2, -6))
G.add_node('13', pos=(3, -7))
G.add_node('14', pos=(6, -7))
G.add_node('15', pos=(0, -8))
G.add_node('16', pos=(7, -8))

# Add edges by defining weight and label
#
G.add_edge('0','8',weight=1, label='')
G.add_edge('8','6',weight=1, label='')
G.add_edge('6','2',weight=1, label='')
G.add_edge('2','5',weight=1, label='')
G.add_edge('5','0',weight=1, label='')

#
#
G.add_edge('0','7',weight=2, label='')
G.add_edge('7','1',weight=2, label='')
G.add_edge('1','4',weight=2, label='')
G.add_edge('4','3',weight=2, label='')
G.add_edge('3','0',weight=2, label='')

#
#
G.add_edge('0','12',weight=2, label='')
G.add_edge('12','11',weight=2, label='')
G.add_edge('11','15',weight=2, label='')
G.add_edge('15','13',weight=2, label='')
G.add_edge('13','0',weight=2, label='')


elarge = [(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >0.5] # solid edge
esmall = [(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=0.5] # dashed edge
 
# Retrieve the positions from graph nodes and save to a dictionary
pos = nx.get_node_attributes(G,'pos')

# Draw nodes, Size Color
nx.draw_networkx_nodes(G,pos,node_size=450, node_color='yellow')

# Draw edges
nx.draw_networkx_edges(G,pos,edgelist = elarge, width = 2, edge_color='g')
nx.draw_networkx_edges(G,pos,edgelist = esmall, width = 2, edge_color='b')
#nx.draw_networkx_edges(G,pos,edgelist = esmall, arrows = False, width=7, alpha=0.3,edge_color='b')

# Draw node labels
nx.draw_networkx_labels(G,pos,font_size=15,font_family='sans-serif')

# Draw edge labels
edge_labels = dict([((u, v), d['label']) for u, v, d in G.edges(data=True)])

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.axis('off')
#plt.savefig("communication_authority_graph.eps", format='eps') # save as eps
plt.show() # display
