import sys, os, glob
import track_distance
from pathlib import Path

def locate_gpx_files(sourceDir='.'):
  """ Prints the distance covered in all .gpx files in the current dir (and sub-dirs)
  """
  if sourceDir == '.':
    # Default handling: accumulate all .gpx files, including those in sub-dirs
    return glob.glob('**/*.gpx', recursive=True)
  else:
    #check whether the path is valid
    # if it is, return all gpx files with filepath as a stem
    if Path(sourceDir).exists():
      return glob.glob(sourceDir/'**/*.gpx', recursive=True)
    else:
      print(sourceDir, 'is not a valid directory!')

if __name__ == '__main__':  
  # Scan the current directory (and any sub-dirs) for .gpx files
    #TODO: when settings/storage is figured out this can be converted to read
    # the specified storage location (and check that it exists) by kwargs
  gpxFiles = locate_gpx_files()
  print('{0} file(s) found'.format(len(gpxFiles)))
  for p in gpxFiles:
    f = open(p)
    print('file: {0}\nmeters covered: {1}\n'.format(Path(p).stem, track_distance.cumulative_track_distance(f)))