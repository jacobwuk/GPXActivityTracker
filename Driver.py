#!/usr/bin/env python3

import sys, os, glob
import track_distance
from pathlib import Path

# Default repo and switch if input?
DEFAULT_GPX_DIR = Path(Path.home(), '.gpx')

def glob_gpx_files(sourceDir='.'):
  """ Returns all .gpx files in the current or specified directory, recursively
  """
  if sourceDir == '.':
    # Default handling: accumulate all .gpx files, including those in sub-dirs
    return glob.glob('**/*.gpx', recursive=True)
  else:
    # if path is valid, return all gpx files with filepath as a stem
    if Path(sourceDir).exists():
      return glob.glob(str(sourceDir) + '/*.gpx', recursive=True)
    else:
      print(sourceDir, 'is not a valid directory!')

def main():
  # TODO: Handle input path from cli
  
  # Scan the current directory (and any sub-dirs) for .gpx files
    #TODO: when settings/storage is figured out this can be converted to read
    # the specified storage location (and check that it exists -> use 'with' is a good idea)
  gpxFiles = glob_gpx_files(DEFAULT_GPX_DIR)
  print('{0} file(s) found'.format(len(gpxFiles)))
  for p in gpxFiles:
    with open(p) as f:
      print('file: {0}\nmeters covered: {1}\n'.format(Path(p).stem, track_distance.cumulative_track_distance(f)))

if __name__ == '__main__':  
  main()