import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns


class DataProcessor:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.df = None

    def read_data(self):
        self.df = pd.read_csv(self.csv_file)
        return self.df


class GraphBuilder:
    def __init__(self, df):
        self.df = df
        self.G = nx.Graph()

    def build_graph(self):
        for _, row in self.df.iterrows():
            authors_id = row["Author(s) ID"].split("; ")
            authors = row["Authors"].split("; ")
            affiliations = row["Affiliations"].split("; ")

            authors_information = list(zip(authors_id, authors, affiliations))

            for index, (id_1, name_1, affiliation_1) in enumerate(authors_information):
                if not self.G.has_node(id_1):
                    self.G.add_node(id_1, name=name_1, affiliation=affiliation_1)

                for id_2, name_2, affiliation_2 in authors_information[index + 1 :]:
                    if not self.G.has_node(id_2):
                        self.G.add_node(id_2, name=name_2, affiliation=affiliation_2)

                    if not self.G.has_edge(id_1, id_2):
                        self.G.add_edge(
                            id_1,
                            id_2,
                            weight=1,
                        )
        return self.G


class Visualizer:
    def __init__(self, graph):
        self.graph = graph

    def plot_assortativity(self):
        degrees = dict(self.graph.degree())
        avg_neighbor_degrees = nx.average_neighbor_degree(self.graph)

        data = {
            "Node Degree": list(degrees.values()),
            "Average neighbor degree": list(avg_neighbor_degrees.values()),
        }
        df = pd.DataFrame(data)

        plt.figure(figsize=(10, 6))
        sns.regplot(
            x="Node Degree", y="Average neighbor degree", data=df, scatter_kws={"s": 50}
        )
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("node_degree_assortativity.png")


def main() -> None:
    csv_file = "../requisito_01/ods_17.csv"  # Altere aqui

    data_processor = DataProcessor(csv_file)
    df = data_processor.read_data()

    graph_builder = GraphBuilder(df)
    G = graph_builder.build_graph()

    visualizer = Visualizer(G)
    visualizer.plot_assortativity()


if __name__ == "__main__":
    main()
