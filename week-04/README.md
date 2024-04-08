# Algorithm and Data Structures 2 - Unit 1 Assignment

This repository contains two Jupyter notebooks which constitute the assignment for Unit 1 of the Algorithms and Data Structures 2 course.

## Challenges

### Challenge 1: findClosestValue Function

In this challenge, the task is to implement a function called `findClosestValue` that takes a binary tree (`tree`) and a target value (`target`) as arguments. The function should return the value in the tree that is closest to the target value. 

For the solution of this challenge, a sequential approach was implemented. It involves traversing the tree starting from the root node, and at each iteration, comparing whether the absolute difference between the current node's value and the target is less than the absolute difference between the closest value found so far and the target. If true, the next closest value is updated. 

This algorithm has a time complexity of O(log(n)) in the best case scenario when the tree is balanced, as it performs only one search in the tree.

### Challenge 2: findKthLargestValue Function

The second challenge involves finding the k-th largest value in a tree. The task is to implement the `findKthLargestValue` function, which takes a tree (`tree`) and a value (`k`) as arguments, and returns the k-th largest value in the tree.

To solve this challenge, a recursive function called `inorder_traversal` was created within the `findKthLargestValue` function. This function traverses the entire tree in inorder fashion, adding the values of the nodes to a list. After the recursion, the list is sorted in reverse order, and the k-1th value of this sorted list is returned.

The complexity of the algorithm can be analyzed primarily by the traversal of the tree, which in the best case has an order of O(log(n)). However, depending on the Python's list sorting function used, the complexity may be O(n²), O(n*log(n)), or O(n+k). Assuming Python implements the merge sort, we can expect an overall complexity of O(n*log(n)) for the algorithm.

## Author

This assignment was completed by Mateus Cavalcanti Alves Teixeira Silva. A brief explanation of the solutions can be found in the video [here](https://www.youtube.com/watch?v=5ohNyeKh9lk).

Additionally, the solutions for the challenges are available in their respective Jupyter notebooks.

Please refer to the Jupyter notebooks in this repository for detailed implementations and explanations.

