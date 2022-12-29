import matplotlib.pyplot as plt
import networkx as nx

fig, ax = plt.subplots()

G = nx.Graph()
nodes_california = ["Los Angeles", "San Diego", "San Francisco"]
nodes_florida = ["Miami", "Orlando", "Tampa"]

G.add_nodes_from(nodes_california)
G.add_nodes_from(nodes_florida)

G.add_edge("California", "Los Angeles")
G.add_edge("California", "San Diego")
G.add_edge("California", "San Francisco")
G.add_edge("Florida", "Miami")
G.add_edge("Florida", "Orlando")
G.add_edge("Florida", "Tampa")

nx.draw(G, with_labels=True)

fig
