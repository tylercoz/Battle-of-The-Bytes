# Goal

Given a [Binary Search Tree](https://en.wikipedia.org/wiki/Binary_search_tree) with the following API:
 - assume the BST object starts at the root node
 - .left returns the left child of BST, also a BST object
 - .right returns the right child of BST, also a BST object
 - .key returns the value of the current node.

 return a List containing each node in order from top-to-bottom, left-to-right.

 Hint: A queue could be helpful here.

# Example

Given:

    4
   /  \
  2    6
 / \  / \
1   3 5   7

it would output:
[4, 2, 6, 1, 3, 5, 7]
