import math as m
from lxml import etree as et
# Average radius of Earth, in meters
# NASA, volumetric mean radius: https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
EARTH_RADIUS = 6371000

def cumulative_track_distance(filename):
  """Computes the cumulative distance traversed in a .gpx file, in meters.

  Sums up the distance between each point in the file. NOTE: Currently all 
  point->point transistions are treated as valid; this method does not check
  for continuity. Does not account for changes in elevation.
  
  Args:
    filename: The name of a .gpx file.

  Returns:
    The cumulative distance, in meters, traversed in the .gpx file  
  """
  
  tree = et.parse(filename)
  root = tree.getroot()
  # root currently points towards {default}gpx 
  # extract the root node of the sub-tree containing the tracks
  trkRoot = root.find('trk', root.nsmap)
  # hold the extracted (lat, long) as a tuples in decimal degrees
  coords = []
  elev = []

  # Activities can be segmented, accumulate points from all segments 
  # TODO: Decide how to deal with "disjoint" segments. For now, the segments
  # are treated as continuous, but in reality this can introduce "jumps"
  # if the distance between the end and start of the next seg is large. 
  # (tracking was paused on the device, segments were deleted from the .gpx)
  # "Large" is just relative maaan, so may want to have some statistics
  # to detect anomolous separation (avg dist moved, +- some % of that is ok)

  # Each trkseg is a set of points, Suunto Ambit 3 creates a new trkseg after a pause  
  for seg in trkRoot.findall('trkseg', root.nsmap):
    # In the future, may want to calculate the distance traversed in each segment 
    # separately and then sum the segments
    for pt in seg.findall('trkpt', root.nsmap):
      # trkpt tags contain the values lat, lon: <trkpt lat= , lon= >
      coords.append( (float(pt.get('lat')), float(pt.get('lon'))) )

  havDist = 0
  
  for i in range(len(coords) - 1):
    havDist = havDist + haversine_distance(coords[i], coords[i + 1])

  return havDist


def haversine_distance(cordA, cordB):
  """
  Returns the great circle distance between two decimal gps coordinates.

  Calculated by the haversine formula: https://en.wikipedia.org/wiki/Haversine_formula 
  
  Args:
      cordA: A (float lat, float long) coordinate tuple of the starting point. 
      cordB: A (float lat, float long) coordinate tuple of the end point.
  
  Returns:
    The distance, in meters, between the two points
  """
  d = 2.0 * EARTH_RADIUS * haversine(cordA, cordB)
  return d

def haversine(ptA, ptB):
  ''' Returns the haversine component per: https://en.wikipedia.org/wiki/Haversine_formula '''
  radxA, radyA = m.radians(ptA[0]), m.radians(ptA[1])
  radxB, radyB = m.radians(ptB[0]), m.radians(ptB[1])
  hav = m.sin((radxB - radxA) / 2)**2 + m.cos(radxA) * m.cos(radxB) * m.sin((radyB - radyA) / 2)**2
  return m.asin(m.sqrt(hav))