import sys, os, glob
import track_distance
from pathlib import Path

if __name__ == '__main__':  
  # Scan the current directory (and any sub-dirs) for .gpx files
    #TODO: when settings/storage is figured out this can be converted to read
    # the specified storage location (and check that it exists) by kwargs
  #for p in glob.glob('**/*.gpx', recursive=True):
  gpxFiles = glob.glob('**/*.gpx', recursive=True)
  print(len(gpxFiles), 'file(s) found')
  for p in gpxFiles:
    f = open(p)
    print('file:', Path(p).stem)
    print('meters covered:', track_distance.cumulative_track_distance(f), '\n')

def find_all():
  """ Prints the distance covered in all .gpx files in the current dir (and sub-dirs)
  """
  gpxFiles = glob.glob('**/*.gpx', recursive=True)
  print(len(gpxFiles), 'file(s) found')
  for p in gpxFiles:
    f = open(p)
    print('file:', Path(p).stem)
    print('meters covered:', track_distance.cumulative_track_distance(f), '\n')
