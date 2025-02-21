import unittest
from p8 import justify #type: ignore

class TestAdd(unittest.TestCase):
  def test_one(self):
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    self.assertEqual(
      justify(words, maxWidth),
      ["This    is    an",
       "example  of text",
       "justification.  "]
    )

  def test_two(self):
    words = ["What","must","be","acknowledgment","shall","be"]
    maxWidth = 16
    self.assertEqual(
      justify(words, maxWidth),
      ["What   must   be",
       "acknowledgment  ",
       "shall be        "]
    )

  def test_three(self):
    words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 20
    self.assertEqual(
      justify(words, maxWidth),
      ["Science  is  what we",
       "understand      well",
       "enough to explain to",
       "a  computer.  Art is",
       "everything  else  we",
       "do                  "]
    )

if __name__ == '__main__':
  unittest.main()
