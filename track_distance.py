"""
Given a .gpx file containing a set of tracks, returns the cumulative distance
traversed. 

WARNING: This does not check for continuity in the track!
         The output distance assumes that all pt->pt transitions are valid.
"""
import math as m
from lxml import etree as et
# Average radius of Earth, in meters
# NASA, volumetric mean radius from: https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
EARTH_RADIUS = 6371000.0

def cumulative_track_distance(filename):
  # load the file
  tree = et.parse(filename)
  root = tree.getroot()
  # root currently points towards {default}gpx 
  # extract the root node of the sub-tree containing the tracks
  trkRoot = root.find('trk', root.nsmap)
  # hold the extracted (lat, long) as a tuple in decimal degrees
  coords = []
  # Activities can be segmented, accumulate points from all segments 
  # TODO: Decide how to deal with "disjoint" segments. For now, the segments
  # are treated as continuous, but in reality this can introduce "jumps"
  # if the distance between the end and start of the next seg is large.
  # "Large" is just relative maaan, so may want to have some statistics
  # to detect anomolous separation (avg dist moved, +- some % of that is ok) 
  for seg in trkRoot.findall('trkseg', root.nsmap):
    for pt in seg.findall('trkpt', root.nsmap):
      # trkpt tags contain the values lat, lon: <trkpt lat= , lon= >
      coords.append( (float(pt.get('lat')), float(pt.get('lon'))) )

  havDist = 0
  # cumulative dist = SUM[dist(i, i + 1)], i \in coords, \in [0, N - 2]
  for i in range(len(coords) - 1):
    havDist = havDist + haversine_distance(coords[i], coords[i + 1])

  return dist


def haversine_distance(cordA, cordB):
  """
  Returns the great circle distance between two decimal gps coordinates.
  
  Calculated by the haversine formula: https://en.wikipedia.org/wiki/Haversine_formula 
  
  @param cordA a (lat, long) tuple of point A 
  @param cordB a (lat, long) tuple of point B
  @return the distance, in meters, between the two points
  """
  d = 2.0 * EARTH_RADIUS * haversine(cordA, cordB)
  return d

# The Haversine function
def haversine(radA, radB):
  """
  Returns the haversine-based component of the distance calculation 
  """
  xA, yA = m.radians(radA[0]), m.radians(radA[1])
  xB, yB = m.radians(radB[0]), m.radians(radB[1])
  hav = m.asin(m.sqrt((m.sin((xB - xA) / 2)**2) + m.cos(xA) * m.cos(xB) * m.sin((yB - yA) / 2)**2))
  return hav

# For testing
if __name__ == '__main__':
  print(cumulative_track_distance('targetData/Move_2019_05_19_17_41_13_Running.gpx')/1609)