from OFS.interfaces import ITraversable
from plone.cachepurging.paths import TraversablePurgePaths
from zope.interface import implements

import unittest


class FauxTraversable(object):
    implements(ITraversable)

    def virtual_url_path(self):
        return 'foo'

class TestTraversablePaths(unittest.TestCase):

    def test_traversable_paths(self):

        context = FauxTraversable()
        paths = TraversablePurgePaths(context)

        self.assertEqual(['/foo'], paths.getRelativePaths())
        self.assertEqual([], paths.getAbsolutePaths())

def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
