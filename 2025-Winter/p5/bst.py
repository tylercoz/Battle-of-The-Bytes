class BST:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def insert(self, val):
      node = BST(val)

      if val <= self.key:
        if self.left:
          self.left.insert(val)
        else:
          self.left = node
      if val > self.key:
        if self.right:
          self.right.insert(val)
        else:
          self.right = node

    def in_order(self):
      if self.left:
        self.left.in_order()
      print(self.key, end=' ')
      if self.right:
        self.right.in_order()

def main():
  bst = BST(4)
  bst.insert(2)
  bst.insert(6)
  bst.insert(1)
  bst.insert(3)
  bst.insert(5)
  bst.insert(7)
  bst.in_order()
  print()

if __name__ == '__main__':
  main()
