# noinspection PyUnresolvedReferences
import unittest
# noinspection PyUnresolvedReferences
import gift_wrapping


class TestGw(unittest.TestCase):

    def test_convexhull(self):

        result = gift_wrapping.convex_hull((0, 0),
                                           (0, 4), (4, 4), (1, 4), (0, 2), (3, 6),
                                           (-3, 6), (-4, 4), (1, 5), (-1, 3))

        self.assertEqual(result, (0, 0), (3, 6),
                         (4, 4), (-3, 6), (-4, 4))
