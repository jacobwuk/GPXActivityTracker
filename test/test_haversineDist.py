import unittest
#import track_distance
from track_distance import haversine_distance

class TestHaversine(unittest.TestCase):
	
	# pole to pole is ~20,000km
	def test_poleToPole(self):
		self.assertEqual(20000, int(haversine_distance((90,180),(-90,180))))

	# this result pulled from scikit learn's haversine function... which is the same calculation
	# probably want to find better examples
	def test_BAirportToParisAirport(self):
		self.assertAlmostEqual(11099540.35582, haversine_distance((-34.833333, -58.5166646),(49.0083899664, 2.53844117956)))

if __name__ == '__main__':
	unittest.main()