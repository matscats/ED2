import streamlit as st
from avl_tree import AVLTree
from corpus import Corpus


@st.cache_data
def process_corpus_and_build_tree():
    CORPUS_PATH = "static/corpus.pdf"
    corpus = Corpus(CORPUS_PATH)
    corpus.process_text(
        lower_text=True,
        remove_punctuation=True,
        remove_digits=True,
        remove_roman_numerals=True,
    )

    avl_tree = AVLTree()
    for word in corpus.get_words():
        avl_tree.add(word)

    return corpus, avl_tree


def main():
    corpus, avl_tree = process_corpus_and_build_tree()

    user_input = st.text_input("Digite um prefixo para buscar a palavra:")
    if user_input:
        words = avl_tree.words_with_prefix(user_input)
        if words:
            st.write("Palavras encontradas com o prefixo '{}':".format(user_input))
            for word in words:
                st.write("- " + word)
        else:
            st.write(
                "Nenhuma palavra encontrada com o prefixo '{}'.".format(user_input)
            )


if __name__ == "__main__":
    main()
