import unittest

from plone.cachepurging.paths import TraversablePurgePaths

class FauxTraversable(object):
    implements(ITraversable)

class TestTraversablePaths(unittest.TestCase):
    
        
def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
