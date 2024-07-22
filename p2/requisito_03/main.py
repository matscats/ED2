import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import combinations
from networkx.algorithms import bipartite


class CSVReader:
    def __init__(self, filename):
        self.filename = filename

    def read_csv(self):
        return pd.read_csv(self.filename)


class GraphBuilder:
    def __init__(self, df):
        self.df = df
        self.G = nx.Graph()

    def build_graph(self):
        for _, row in self.df.iterrows():
            authors = row["Authors"].split(", ")
            for author1, author2 in combinations(authors, 2):
                if self.G.has_edge(author1, author2):
                    self.G[author1][author2]["weight"] += 1
                else:
                    self.G.add_edge(author1, author2, weight=1)
        return self.G


class NetworkAnalysis:
    def __init__(self, graph):
        self.graph = graph

    def analyze(self):
        analysis = {
            "num_vertices": self.graph.number_of_nodes(),
            "num_edges": self.graph.number_of_edges(),
            "degree_assortativity_coefficient": nx.degree_assortativity_coefficient(
                self.graph
            ),
            "num_connected_components": nx.number_connected_components(self.graph),
            "giant_component_size": len(
                max(nx.connected_components(self.graph), key=len)
            ),
            "average_clustering_coefficient": nx.average_clustering(self.graph),
        }
        return analysis


def main():
    # Read the CSV file
    reader = CSVReader("../ods/ods_17.csv")
    df = reader.read_csv()

    # Build the graph
    graph_builder = GraphBuilder(df)
    G = graph_builder.build_graph()

    # Analyze the network
    network_analysis = NetworkAnalysis(G)
    analysis_results = network_analysis.analyze()

    # Print analysis results
    print(f"Number of vertices: {analysis_results['num_vertices']}")
    print(f"Number of edges: {analysis_results['num_edges']}")
    print(
        f"Degree assortativity coefficient: {analysis_results['degree_assortativity_coefficient']}"
    )
    print(
        f"Number of connected components: {analysis_results['num_connected_components']}"
    )
    print(f"Size of giant component: {analysis_results['giant_component_size']}")
    print(
        f"Average clustering coefficient: {analysis_results['average_clustering_coefficient']}"
    )


if __name__ == "__main__":
    main()