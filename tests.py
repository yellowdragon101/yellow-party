import unittest
from untitled import get_compass_dir

class TestMethods(unittest.TestCase):
    def test_create_deck(self):
        self.assertEqual(get_compass_dir((0,0), (0,1)), 'N')
        self.assertEqual(get_compass_dir((0,0), (1,0)), 'E')
        self.assertEqual(get_compass_dir((0,0), (0,-1)), 'S')
        self.assertEqual(get_compass_dir((0,0), (-1,-0)), 'W')


if __name__ == '__main__':
    unittest.main()