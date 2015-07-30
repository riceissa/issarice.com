import unittest
from tags import *

class TestStringMethods(unittest.TestCase):

  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)

class BasicTags(unittest.TestCase):
    def test_simple(self):
        data = TagDag()
        data.add_tag(TagNode("University of Washington", aliases=["uw"]))
        uw_courses = TagNode("University of Washington course review", aliases=["uw courses"])
        data.add_tag(uw_courses)
        self.assertTrue("uw" in data)

class MoreRealistic(unittest.TestCase):
    # this test is deprecated
    def test_education(self):
        """TODO: Docstring for test_education.
        :returns: TODO

        """
        tag_list = [
            TagNode("University of Washington", aliases=["uw"]),
            TagNode("University of Washington course review", aliases=["uw courses"]),
            TagNode("education"),
            TagNode("Massachusetts Institute of Technology", aliases=["MIT"]),
            TagNode("University of California, Berkeley", aliases=["ucb"]),
        ]
        dag = TagDag(casing="smart")
        dag.add_tags(tag_list)
        dag.add_children("education", ["uw", "mit", "ucb"])
        dag.add_parent("uw courses", "uw")
        self.assertTrue(dag.implies("uw", "education"))
        self.assertTrue(dag.implies("mit", "education"))
        self.assertTrue(dag.implies("ucb", "education"))
        self.assertTrue(dag.implies("uw courses", "education"))
        self.assertFalse(dag.implies("ucb", "mit"))

    def test_adding_order(unittest.TestCase):
        pass

    def test_programming(unittest.TestCase):
        """
        Test example using onotology of computing/programming related tags.
        """
        dag = TagDag()
        dag.add_tags([
            TagNode("computing"),
            TagNode("Linux"),
            TagNode("Python", aliases=["py"]),
            TagNode(),
            TagNode(),
            TagNode(),
        ])

if __name__ == '__main__':
    unittest.main()
