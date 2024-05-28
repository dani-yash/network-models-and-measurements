# Network Models and Measurements

Graph Model Generators

Generate the following list of undirected unweighted graphs:

	1.	Erdős-Rényi Random Graph Model
	•	Three (3) graphs based on the Erdős-Rényi random graph model (er1, er2, er3).
	2.	Watts–Strogatz Small-World Graph Model
	•	Three (3) graphs based on the Watts–Strogatz small-world graph model (ws1, ws2, ws3).
	3.	Barabási–Albert Preferential Attachment Model
	•	Three (3) graphs based on the Barabási–Albert preferential attachment model (ba1, ba2, ba3).

Each graph  G(N, E)  should be about the same size, including  N \approx 1,000  nodes and  E \approx 10,000  edges. Remember to report the parameter values of the graph generator you used to create the graph. In addition, for each graph  G(N, E) , obtain its giant connected component  CC_G  and report its size (#nodes, #edges) in a table.

Graph Measurements

For each of the graphs above (i.e., focus only on the associated giant connected component  CC_G ), report:

	1.	Node Degree Distribution
	•	The node degree distribution of the graph (as a plot).
	2.	Local Clustering Coefficient Distribution
	•	The distribution of the local clustering coefficient of the nodes of the graph (as a plot).
	3.	Global Clustering Coefficient
	•	The global clustering coefficient of the graph (a number).
	4.	Shortest Path Length Distribution
	•	The distribution of the shortest path lengths of the graph (as a plot).
	5.	Average Shortest Path Length
	•	The average shortest path length of the graph (a number).
	6.	Diameter of the Graph
	•	The diameter of the graph (a number).

Whenever a plot is required, report the most informative/appropriate type of plot, or present more than one plot using your best judgment.

Discussion

Briefly comment on:

	1.	How the properties of the graphs coming from the same graph model compare to each other?
	2.	How the properties of the graphs coming from different graph models compare to each other?