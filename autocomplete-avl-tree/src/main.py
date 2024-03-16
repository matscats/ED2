from avl_tree import AVLTree
from corpus import Corpus


def main():
    CORPUS_PATH = "static/a_republica.pdf"
    # Cria o corpus
    corpus = Corpus(CORPUS_PATH)
    # Processa o corpus usando flags booleanas
    corpus.process_text(
        lower_text=True,
        remove_punctuation=True,
        remove_digits=True,
        remove_roman_numerals=True,
    )
    # Cria a AVLTree
    avl_tree = AVLTree()
    # Preenche a AVLTree
    for word in corpus.get_words():
        avl_tree.add(word)
    # Teste
    while True:
        user_input = input("Digite um prefixo para buscar a palavra: ")
        print(avl_tree.words_with_prefix(user_input))


if __name__ == "__main__":
    main()
