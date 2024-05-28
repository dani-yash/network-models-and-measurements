import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter

# The number of times the loop will run.
num_of_runs = 3

for run_number in range(num_of_runs):

    # This is the number used in all of the output, since run_number starts at 0.
    # This number will start at 1 and end at num_of_runs.
    effective_run = run_number + 1

# A. Graph Model Generators

    # The parameter values for the graph methods.
    n = 1000
    k = 20
    p = 0.1

    # Creating the graph.
    WattsStrogatzGraph = nx.watts_strogatz_graph(n, k, p)

    # Finding the largest connected component.
    largest_cc = max(nx.connected_components(WattsStrogatzGraph), key=len)

    # Making a copy of the graph that only has the greatest connected component.
    GCC = WattsStrogatzGraph.subgraph(largest_cc).copy()

    # Basic graph parameters.
    print("The n value for ws", effective_run, end=" ")
    print("was: ", n,)
    print("The k value for ws", effective_run, end=" ")
    print("was: ", k)
    print("The p value for ws", effective_run, end=" ")
    print("was: ", p)
    print("For ws", effective_run, end=", ")
    print("number of nodes in the giant connected component is: ", GCC.number_of_nodes())
    print("For ws", effective_run, end=", ")
    print("The number of edges in the giant connected component is: ", GCC.number_of_edges())

    # Graph customization code.
    plt.figure(figsize=(10, 8))

    pos = nx.spring_layout(GCC)

    node_options = {"node_color": "blue", "node_size": 15}

    edge_options = {"width": .2, "alpha": 0.15, "edge_color": "black"}

    nx.draw_networkx_nodes(GCC, pos, **node_options)

    nx.draw_networkx_edges(GCC, pos, **edge_options)

    # Saving the graph as an image.
    plt.savefig('WS{}.png'.format(effective_run), dpi=600)

    # plt.show

# B. Degree Distribution Plot

    # Returns 1000 pairs of values in a list with the first index being the source node
    # and the second index being the degree of the node.
    degrees = GCC.degree()

    # Removing source node as it is not needed.
    degrees = [node[1] for node in degrees]

    # Finding frequency.
    degree_counts = Counter(degrees)

    # Finding the number of total frequencies.
    total_freq = sum(degree_counts.values())

    # Converting the dictionary into two lists.
    degree_values = list(degree_counts.keys())
    probability_values = [value / total_freq for value in degree_counts.values()]

    # Graph customization code.
    plt.figure(figsize=(10, 6))

    plt.loglog(degree_values, probability_values, marker='o', linestyle='None')

    plt.title('Degree Distribution of Giant Connected Component')

    plt.xlabel('Degree')

    plt.ylabel('P(k)')

    plt.grid(True, which="both", ls="--")

    # Saving the graph as an image.
    plt.savefig('WS{}DD.png'.format(effective_run), dpi=600)

# B. Clustering Plot

    # Returns 1000 dictionary values with the keys as the source node
    # and the values as the clustering coefficients.
    clustering_coefficients = nx.clustering(GCC)

    # Finding degrees.
    degrees = [GCC.degree(node) for node in GCC]

    # Round the clustering coefficients to 2 decimal places to limit significant figures.
    clustering_coefficients = {node: round(clustering_coefficients[node], 2) for node in GCC}

    # Create a dictionary of frequencies.
    frequencies = {}
    for value in clustering_coefficients.values():
        if value in frequencies:
            frequencies[value] += 1
        else:
            frequencies[value] = 1

    # Finding the total number of frequencies.
    total_freq = sum(frequencies.values())

    # Find the probability of each frequency.
    frequency_values = {k: v / total_freq for k, v in frequencies.items()}

    # Graph customization code.
    plt.figure(figsize=(10, 6))

    plt.plot(frequency_values.keys(), frequency_values.values(), marker='o', linestyle='None')

    plt.title('Clustering Coefficient Distribution of Giant Connected Component')

    plt.xlabel('Rounded Clustering Coefficient')

    plt.ylabel('C(k)')

    plt.grid(True, which="both", ls="--")

    # Saving the graph as an image.
    plt.savefig('WS{}CP.png'.format(effective_run), dpi=600)

# B. Shortest Path Length Plot

    # Path lengths has 1000 dictionaries for all 1000 nodes, so a total of 1 million values.
    path_lengths = dict(nx.all_pairs_shortest_path(GCC))

    # Create a list of the keys, the source nodes.
    keys = list(path_lengths.keys())

    # Remove all paths that have a lower destination number than the starting node.
    # This removes duplicates paths, 0 to 1 should be the same as 1 to 0 so no need to double count.
    # This also creates a triangle sum.
    for key in keys:
        for neighbor in list(path_lengths[key].keys()):
            if neighbor < key:
                del path_lengths[key][neighbor]

    # A list of all the frequencies of the shortest paths for each source node.
    # Example. [1, 2, 3, 4, 4, 4, 4]
    # So this source node has these shortest paths to the other nodes.
    frequency_list = []

    # A dictionary for the frequency of shortest paths for all source nodes.
    # Example. {0: {1: 1. 2: 1, 3: 1, 4: 4}, ... , }
    # So this has all the frequencies of the shortest paths to all other nodes.
    frequency_dict = {}

    # Find the frequencies of the dictionaries inside path_lengths.
    for node in path_lengths:
        frequency_list = []
        for items in path_lengths[node].values():
            frequency_list.append(len(items))
        frequency_dict[node] = dict(Counter(frequency_list))

    # A dictionary for the collapsed frequency of all the shortest paths in the network.
    # Example. {1: 1000, 2: 10000, 3: 160000, 4: 320000, 5: 1000}
    # This simplifies all the individual dictionaries back into a smaller one.
    collapsed_frequency_dict = {}

    # Collapse the frequencies into just a few numbers.
    for node, frequencies in frequency_dict.items():
        for path_length, frequency in frequencies.items():
            if path_length in collapsed_frequency_dict:
                collapsed_frequency_dict[path_length] += frequency
            else:
                collapsed_frequency_dict[path_length] = frequency

    # Find the total number of frequencies
    total_freq = sum(collapsed_frequency_dict.values())

    # Find the probability of each frequency in the dictionary.
    collapsed_frequency_dict = {k: v / total_freq for k, v in collapsed_frequency_dict.items()}

    # Graph customization code.
    plt.figure(figsize=(10, 6))

    plt.plot(collapsed_frequency_dict.keys(), collapsed_frequency_dict.values(), marker='o', linestyle='None')

    plt.title('Shortest Path Length Distribution of Giant Connected Component')

    plt.xlabel('Distance')

    plt.ylabel('P(k)')

    plt.grid(True, which="both", ls="--")

    # Saving the graph as an image.
    plt.savefig('WS{}SP.png'.format(effective_run), dpi=600)

# B. Graph Number Measurements

    # Finds the average clustering value of the network.
    print("The average clustering coefficient for ws", effective_run, end=" ")
    print("is: ", round(nx.average_clustering(GCC), 4))

    # Finds the average length of shortest paths.
    print("The average shortest path length for ws", effective_run, end=" ")
    print("is: ", round(nx.average_shortest_path_length(GCC), 4))

    # Finds how far apart are the furthest nodes.
    print("The diameter for ws", effective_run, end=" ")
    print("is: ", nx.diameter(GCC))

    if run_number < 2:
        print()
