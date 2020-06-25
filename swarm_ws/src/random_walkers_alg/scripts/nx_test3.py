#!/usr/bin/env python
import random
import pylab
from matplotlib.pyplot import pause
import networkx as nx
pylab.ion()

graph = nx.Graph()
node_number = 2
# robot_list = [f"R_{i}" for i in range(1, 11)]
robot_list = list(range(10))
graph.add_nodes_from(robot_list)
# graph.add_node(node_number, Position=(random.randrange(0, 100), random.randrange(0, 100)))

def get_fig():
    global node_number
    # node_number += 1
    # graph.add_node(node_number, Position=(random.randrange(0, 100), random.randrange(0, 100)))
    graph.add_edge(random.choice(list(graph.nodes())),
                   random.choice(list(graph.nodes())))
    nx.draw(graph)#, pos=nx.get_node_attributes(graph,'Position'))

num_plots = 50;
pylab.show()

for i in range(num_plots):

    get_fig()
    pylab.draw()
    pause(2)
