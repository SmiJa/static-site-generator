import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
  def test_eq(self):
    node = HTMLNode("p", "Hello World", None, {})
    node2 = HTMLNode("p", "Hello World", None, {})
    self.assertEqual(node, node2)

  def test_eq_props(self):
    node = HTMLNode("a", "Art Portfolio", None, {"href": "https://mrjasonsmith.com"})
    node2 = HTMLNode("a", "Art Portfolio", None, {"href": "https://mrjasonsmith.com"})
    self.assertEqual(node, node2)

  def test_eq_list(self):
    child1 = LeafNode("li", "Movies")
    child2 = LeafNode("li", "Video Games")
    children = [child1, child2]
    node = HTMLNode("ul", None, children, None)
    node2 = HTMLNode("ul", None, children, None)
    self.assertEqual(node, node2)

  def test_eq_text_empty(self):
    node = HTMLNode()
    node2 = HTMLNode()
    self.assertEqual(node, node2)

  def test_eq_leaf(self):
    node1 = LeafNode("p", "Hello World!").to_html()
    node2 = "<p>Hello World!</p>"
    self.assertEqual(node1, node2)

if __name__ == "__main__":
  unittest.main()