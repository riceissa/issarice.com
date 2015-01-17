import unittest

# modeled off http://www.openp2p.com/pub/a/python/2004/12/02/tdd_pyunit.html

from classes import *


page = Page("generator/test.md")
page.load_metadata()

class ClassesTests(unittest.TestCase):

    def testTags(self):
        #print page.metadata.tags
        self.failUnless(set(page.metadata.tags) ==
            set(['Slate Star Codex', 'Python', 'Haskell', 'Debian', 'programming', 'computing']))

    def testTitle(self):
        self.failUnless(page.metadata.title == 'Test title')

    #def testAuthor(self):
        #self.failUnless(page.metadata.author == [])

def main():
    unittest.main()

if __name__ == '__main__':
    main()
