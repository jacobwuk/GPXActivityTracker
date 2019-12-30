import track_distance as td
class Activity:
  ""
  def __init__(self, filename):
    # TODO: add input checking for the filename
    self.filename = filename
    # cumulative distance, in meters
    self.distance = td.cumulative_track_distance(filename)
    # cumulative time, in seconds
    if activityType is None:
      self.type = None
    else:
      self.type = activityType

  # Getters and Setters
  
  @input(self,str)
  def set_activity_type(self, activityType):
    self.type = activityType

  def get_activity_type(self):
    if self.type is None:
      return 'N/A'
    else:
      return self.type