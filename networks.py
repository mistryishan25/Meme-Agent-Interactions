import networkx as nx
import random

class RandomNetwork:
    def __init__(self, num_agents, edge_probability):
        self.num_agents = num_agents
        self.edge_probability = edge_probability
        self.graph = self.generate_random_network()

    def generate_random_network(self):
        # Create a random graph (Erdős-Rényi model)
        random_network = nx.erdos_renyi_graph(self.num_agents, self.edge_probability)
        return random_network

    def get_network_properties(self):
        num_edges = self.graph.number_of_edges()
        num_nodes = self.graph.number_of_nodes()
        average_degree = 2 * num_edges / num_nodes
        return num_nodes, num_edges, average_degree

    def get_random_agent_nodes(self, num_random_nodes):
        agent_nodes = list(self.graph.nodes)
        random_agent_nodes = random.sample(agent_nodes, num_random_nodes)
        return random_agent_nodes

# Example usage:
if __name__ == "__main__":
    num_agents = 100
    edge_probability = 0.1

    random_network = RandomNetwork(num_agents, edge_probability)

    num_nodes, num_edges, average_degree = random_network.get_network_properties()
    print(f"Number of nodes: {num_nodes}")
    print(f"Number of edges: {num_edges}")
    print(f"Average degree: {average_degree}")

    random_agent_nodes = random_network.get_random_agent_nodes(10)
    print(f"Random agent nodes: {random_agent_nodes}")
