import sys
import os
import track_distance
from pathlib import Path

if __name__ == '__main__':
  # might just want to iter over them for a time savings perspective
  # although that's probably premature optimization
  
  # was used to test out os.listdir() iteration
  # num = 0
  # might want to use Path from pathlib
  #for file in os.listdir('targetData/'):
  #  filename = os.fsdecode(file)
  #  if filename.endswith('.gpx'):
  #    num = num + 1
  #    print(num)

  # .iterdir() only considers 
  for p in Path('targetData/').iterdir():
    if p.suffix == '.gpx':
      f = open(p)
      print(p.stat().st_size)
      print(p)

  #print(num)


  # iterate over all .gpx files in the current directory and 
  print('do things')