import unittest

# modeled off http://www.openp2p.com/pub/a/python/2004/12/02/tdd_pyunit.html

from classes import *

class ClassesTests(unittest.TestCase):
    def testOne(self):
        page = Page("generator/test.md")
        page.load_metadata()
        print page.metadata.tags
        self.failUnless(set(page.metadata.tags) ==
            set(['Slate Star Codex', 'Python', 'Haskell', 'Debian', 'programming', 'computing']))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
