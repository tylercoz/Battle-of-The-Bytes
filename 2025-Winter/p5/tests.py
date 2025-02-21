import unittest
from bst import BST
from p5 import top_down_sort #type: ignore

class TestBST(unittest.TestCase):
  def test_null_bst(self):
    self.assertEqual(
      top_down_sort(None),
      []
    )

  def test_one(self):
    bst = BST(0)
    self.assertEqual(
      top_down_sort(bst),
      [0]
    )


  def test_example(self):
    bst = BST(4)
    bst.insert(2)
    bst.insert(6)
    bst.insert(1)
    bst.insert(3)
    bst.insert(5)
    bst.insert(7)

    self.assertEqual(
      top_down_sort(bst),
      [4, 2, 6, 1, 3, 5, 7],
    )

  def test_example_2(self):
    bst = BST(3)
    bst.insert(5)
    bst.insert(6)
    bst.insert(7)
    bst.insert(1)
    bst.insert(4)
    bst.insert(9)
    bst.insert(8)
    bst.insert(15)

    self.assertEqual(
      top_down_sort(bst),
      [3, 1, 5, 4, 6, 7, 9, 8, 15],
    )

if __name__ == '__main__':
  unittest.main()
