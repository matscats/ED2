import pandas as pd
import networkx as nx


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
            authors = row["Authors"].split("; ")
            for i, author1 in enumerate(authors):
                for author2 in authors[i + 1 :]:
                    if not self.G.has_edge(author1, author2):
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
    csv_file = "../requisito_01/ods_17.csv"  # Altera aqui

    reader = CSVReader(csv_file)
    df = reader.read_csv()

    graph_builder = GraphBuilder(df)
    G = graph_builder.build_graph()

    network_analysis = NetworkAnalysis(G)
    analysis_results = network_analysis.analyze()

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
