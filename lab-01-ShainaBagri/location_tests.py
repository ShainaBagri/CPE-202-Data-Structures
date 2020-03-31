# CPE 202 Location Class Test Cases, Lab 1

import unittest
from location import *

class TestLocation(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        self.assertEqual(repr(loc2), "Location('Paris', 48.9, 2.4)")
    
    # Add more tests!
    def test_eq(self):
        loc = Location("SLO", 35.3, -120.7)
        loc1 = Location("Paris", 48.9, 2.4)
        loc2 = Location("SLO", 35, -120.7)
        loc3 = Location("SLO", 35.3, -120)
        loc4 = Location("SLO", 35.3, -120.7)
        loc5 = loc1
        self.assertEqual(loc == loc3, False)
        self.assertEqual(loc == loc4, True)
        self.assertEqual(loc2 == loc3, False)
        self.assertEqual(loc1 == loc5, True)

    def test_init(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc.name == "SLO", True)
        self.assertEqual(loc.lat == 35.3, True)
        self.assertEqual(loc.lon == -120.7, True)

if __name__ == "__main__":
        unittest.main()
