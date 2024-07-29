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
            authors = row["Authors"].split("; ")
            for i, author1 in enumerate(authors):
                for author2 in authors[i + 1 :]:
                    if not self.G.has_edge(author1, author2):
                        self.G.add_edge(author1, author2, weight=1)

        for _, row in self.df.iterrows():
            authors = row["Authors"].split("; ")
            author_ids = row["Author(s) ID"].split("; ")
            affiliations = row["Affiliations"].split("; ")
            for author, author_id, affiliation in zip(
                authors, author_ids, affiliations
            ):
                if author not in self.G.nodes:
                    self.G.add_node(
                        author,
                        id_scopus=author_id,
                        name=author,
                        affiliation=affiliation,
                    )
        return self.G


class Visualizer:
    def __init__(self, graph):
        self.graph = graph

    def plot_assortativity(self):
        # Calcular o grau dos nós e o grau médio dos vizinhos
        degrees = dict(self.graph.degree())
        avg_neighbor_degrees = nx.average_neighbor_degree(self.graph)

        # Preparar os dados para o seaborn
        data = {
            "Node Degree": list(degrees.values()),
            "Average neighbor degree": list(avg_neighbor_degrees.values()),
        }
        df = pd.DataFrame(data)

        # Criar o gráfico
        plt.figure(figsize=(10, 6))
        sns.regplot(
            x="Node Degree", y="Average neighbor degree", data=df, scatter_kws={"s": 50}
        )
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("node_degree_assortativity.png")


# Uso das classes para realizar a tarefa
csv_file = "../requisito_01/ods_17.csv"

# Processamento dos dados
data_processor = DataProcessor(csv_file)
df = data_processor.read_data()

# Construção do grafo
graph_builder = GraphBuilder(df)
G = graph_builder.build_graph()

# Visualização
visualizer = Visualizer(G)
visualizer.plot_assortativity()
