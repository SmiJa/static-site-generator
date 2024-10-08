import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("This is a text node", "bold")
    node2 = TextNode("This is a text node", "bold")
    self.assertEqual(node, node2)

  def test_eq_url(self):
    node = TextNode("This is a text node", "bold", None)
    node2 = TextNode("This is a text node", "bold", None)
    self.assertEqual(node, node2)

  def test_eq_type(self):
    node = TextNode("This is a text node", None)
    node2 = TextNode("This is a text node", None)
    self.assertEqual(node, node2)

  def test_eq_text_empty(self):
    node = TextNode("", "bold", None)
    node2 = TextNode("", "bold", None)
    self.assertEqual(node, node2)

if __name__ == "__main__":
  unittest.main()