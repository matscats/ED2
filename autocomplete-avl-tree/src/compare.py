import time
import matplotlib.pyplot as plt
from avl_tree import AVLTree
from binary_tree import BinaryTree
from corpus import Corpus


# Função para medir o tempo de busca em uma AVL Tree
def time_avl_search(avl_tree, prefix):
    start_time = time.perf_counter()
    result = avl_tree.words_with_prefix(prefix)
    end_time = time.perf_counter()
    return len(result), end_time - start_time


def time_binary_search(binary_tree, prefix):
    start_time = time.perf_counter()
    result = binary_tree.words_with_prefix(prefix)
    end_time = time.perf_counter()
    return len(result), end_time - start_time


# Função para medir o tempo de busca em uma lista
def time_list_search(word_list, prefix):
    start_time = time.time()
    result = [word for word in word_list if word.startswith(prefix)]
    end_time = time.time()
    return len(result), end_time - start_time


def main():
    # Carregar corpus e criar estruturas de dados
    CORPUS_PATH = "static/corpus.pdf"
    corpus = Corpus(CORPUS_PATH)
    corpus.process_text(
        lower_text=True,
        remove_punctuation=True,
        remove_digits=True,
        remove_roman_numerals=True,
    )

    # Criação das estruturas de dados
    avl_tree = AVLTree()
    binary_tree = BinaryTree()
    word_list = []

    for word in corpus.get_words():
        avl_tree.add(word)
        binary_tree.add(word)
        if word not in word_list:
            word_list.append(word)

    # Lista para armazenar os tempos de busca
    avl_times = []
    binary_times = []
    list_times = []

    # Prefixo para busca
    prefix = "a"

    # Número de iterações para a busca
    num_iterations = 1000

    for _ in range(num_iterations):
        # Medir o tempo de busca na AVL Tree
        avl_result, avl_time = time_avl_search(avl_tree, prefix)
        avl_times.append(avl_time)

        # Medir o tempo de busca na AVL Tree
        binary_result, binary_time = time_binary_search(avl_tree, prefix)
        binary_times.append(binary_time)

        # Medir o tempo de busca na lista
        list_result, list_time = time_list_search(word_list, prefix)
        list_times.append(list_time)

    # Plotar os resultados
    plt.plot(avl_times, label="AVL Tree")
    plt.plot(binary_times, label="Binary Tree")
    plt.plot(list_times, label="List")
    plt.xlabel("Iteration")
    plt.ylabel("Time (seconds)")
    plt.title("Search Performance Comparison")
    plt.legend()
    plt.savefig("static/search_performance_comparison.png")
    plt.close()


if __name__ == "__main__":
    main()
