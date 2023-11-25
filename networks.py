import math
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random

DEFAULT_NUM_AGENTS = 100


class NetworkBase:
    """Social network superclass with common methods."""

    def edges(self):
        return nx.edges(self.graph)

    def nodes(self):
        return nx.nodes(self.graph)

    def neighbors(self, agent_id):
        return nx.neighbors(self.graph, agent_id)

    def get_network_properties(self):
        num_edges = self.graph.number_of_edges()
        num_nodes = self.graph.number_of_nodes()
        average_degree = 2 * num_edges / num_nodes
        return num_nodes, num_edges, average_degree

    def get_random_agent_nodes(self, num_random_nodes):
        agent_nodes = list(self.graph.nodes)
        random_agent_nodes = random.sample(agent_nodes, num_random_nodes)
        return random_agent_nodes

    def draw(self):
        pos = nx.spring_layout(self.graph)  # Positions of the nodes
        nx.draw(self.graph, pos, with_labels=True, node_size=200)
        plt.title("Network Graph")
        plt.show()


class RandomNetwork(NetworkBase):
    """A randomly configured, highly-connected social network."""

    def __init__(self, num_agents=DEFAULT_NUM_AGENTS, edge_probability=0.2, draw=False):
        self.num_agents = num_agents
        self.edge_probability = edge_probability
        self.graph = nx.erdos_renyi_graph(self.num_agents, self.edge_probability)

        # Draw the graph
        if draw:
            pos = nx.spring_layout(self.graph)  # Positions of the nodes
            nx.draw(self.graph, pos, with_labels=True, node_size=200)
            plt.title("Network (Random Network)")
            plt.show()


class PolarizedCrowd(NetworkBase):
    """A polarized crowd social network."""

    def __init__(self, num_agents=DEFAULT_NUM_AGENTS, edge_probability=0.2, draw=False):
        # Create two separate networks
        group1 = nx.erdos_renyi_graph(int(num_agents / 2), edge_probability)
        group2 = nx.erdos_renyi_graph(math.ceil(num_agents / 2), edge_probability)

        # Rename nodes in group2 to have distinct node names
        group2 = nx.relabel_nodes(group2, {node: node + int(num_agents / 2) for node in group2.nodes})

        # Connect the two groups with ~10% of the total nodes
        cross_edges = []
        for _ in range(int(num_agents * .1)):
            cross_edges.append((np.random.randint(0, int(num_agents / 2)),
                                np.random.randint(int(num_agents / 2), num_agents)))

        # Create an empty graph
        self.graph = nx.Graph()

        # Add nodes and edges from both groups
        self.graph.add_nodes_from(group1)
        self.graph.add_nodes_from(group2)
        self.graph.add_edges_from(group1.edges)
        self.graph.add_edges_from(group2.edges)

        # Add the cross-edges between the groups
        self.graph.add_edges_from(cross_edges)

        # Draw the graph
        if draw:
            pos = nx.spring_layout(self.graph)  # Positions of the nodes
            nx.draw(self.graph, pos, with_labels=True, node_size=200)
            plt.title("Network (Polarized Crowd)")
            plt.show()


class CommunityClusters(NetworkBase):
    """A community clusters social network."""

    def __init__(self, num_agents=DEFAULT_NUM_AGENTS, edge_probability=0.3, num_clusters=5, draw=False):
        # Calculate the size of each cluster
        cluster_size = int(num_agents / num_clusters)
        print('cluster size: ', cluster_size)

        # Create an empty graph
        community_clusters = nx.Graph()

        # Create clusters and connect them
        for i in range(num_clusters):
            if i == 0:
                # If num_agents and num_clusters are configured to where each cluster cannot have the same size,
                # add the "remainder" nodes to the first cluster.
                extra_nodes = num_agents - (cluster_size * num_clusters)
                cluster = nx.erdos_renyi_graph(cluster_size + extra_nodes, edge_probability)
                cluster = nx.relabel_nodes(cluster, {node: node + i * cluster_size for node in cluster.nodes})
            else:
                cluster = nx.erdos_renyi_graph(cluster_size, edge_probability)
                cluster = nx.relabel_nodes(cluster, {node: node + extra_nodes + i * cluster_size for node in cluster.nodes})
            community_clusters.add_nodes_from(cluster)
            community_clusters.add_edges_from(cluster.edges)

        # Connect all clusters to each other
        for i in range(num_clusters):
            for j in range(i + 1, num_clusters):
                nodes_cluster1 = list(range(i * cluster_size, (i + 1) * cluster_size))
                nodes_cluster2 = list(range(j * cluster_size, (j + 1) * cluster_size))
                edge_to_add = random.choice(nodes_cluster1), random.choice(nodes_cluster2)
                community_clusters.add_edge(*edge_to_add)

        # Draw the graph
        if draw:
            pos = nx.spring_layout(community_clusters)  # Positions of the nodes
            nx.draw(community_clusters, pos, with_labels=True, node_size=200)
            plt.title("Network (Community Clusters)")
            plt.show()

        self.graph = community_clusters
