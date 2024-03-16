# AVLTree Autocomplete Program

This Python program is designed to store words in an AVLTree data structure, enabling the implementation of an autocomplete feature. Given a prefix, the program returns a list of words found in the tree.

## Purpose
The purpose of this program is to demonstrate the implementation of an autocomplete feature using an AVLTree data structure. Words are stored in the tree, and the program allows users to retrieve words based on a given prefix efficiently.

## Data Source
The words used to populate the AVLTree are extracted from the novel "Memórias Póstumas de Brás Cubas" (The Posthumous Memoirs of Brás Cubas) by Machado de Assis. This data source provides a diverse range of words for testing and demonstration purposes.

## Author
This program was developed by Mateus Cavalcanti Alves Teixeira Silva.

## How to Run
To execute the program, follow these steps:

1. Create a virtual environment:
`
$ python -m venv venv
`

2. Activate the virtual environment:
`
$ . venv/bin/activate
`

3. Install the required dependencies:
`
pip install -r requirements.txt
`


4. Execute the code from the root directory of the project:
`
$ streamlit run src/main.py
`

## Usage
Once the program is running, users can input a prefix into the provided interface. The program will then search the AVLTree for words that match the given prefix and display the results.
