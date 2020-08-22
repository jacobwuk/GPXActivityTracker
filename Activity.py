import os
import track_distance as td
from pathlib import Path

def extract_meta(filename_path):
  # gotta do a thing
  return (0 ,0)

class Activity:
  ""
  def __init__(self, filepath:Path, owner='Public', actName='Activity'):
    if not filepath.exists():
      exit()
      #throw an error
      #sys.stderr()
    # load default settings, if present    
    self._filepath = filepath
    self._owner = owner
    self._actName = actName
    # dateTime, elapsed time of the activity
    self._startTime, self._endTime, self._elapsedTime = extract_meta(filepath)
    # calculated fields
    self._distance, self._eleGain, self._eleLoss = td.cumulative_track_distance(filepath) 

    # Getters
    @property
    def filepath(self):
      return self._filepath

    @property
    def owner(self):
      return self._owner

    @property
    def actName(self):
      return self._actName
    
    @property
    def distance(self):
      return self._distance
    
    @property 
    def eleGain(self):
      return self._eleGain

    @property
    def eleLoss(self):
      return self._eleLoss

    @property
    def eleGainLoss(self):
      return (self._eleGain, self._eleLoss)
    # Setters, only allowed for _type, _owner
    # Only unit conversion methods are allowed after initialization
  
    @property
    @input(self,str)
    def set_actName(self, actName):
      self._actName = actName

  def get_activity_type(self):
    if self.type is None:
      return 'N/A'
    else:
      return self.type

class Run(Activity):
  pass
