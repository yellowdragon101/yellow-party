import unittest
from untitled import get_compass_dir

class TestMethods(unittest.TestCase):
    def test_create_deck(self):
        self.assertEqual(get_compass_dir((0,0), (0,1)), 'N')
        self.assertEqual(get_compass_dir((0,0), (1,0)), 'E')
        self.assertEqual(get_compass_dir((0,0), (0,-1)), 'S')
        self.assertEqual(get_compass_dir((0,0), (-1,-0)), 'W')
        
        self.assertEqual(get_compass_dir((0,0), (1,10)), 'N')
        self.assertEqual(get_compass_dir((0,0), (10, 1)), 'E')
        self.assertEqual(get_compass_dir((0,0), (1,-10)), 'S')
        self.assertEqual(get_compass_dir((0,0), (-10,1)), 'W')


if __name__ == '__main__':
    unittest.main()