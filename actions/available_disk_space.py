import sys

from st2common.runners.base_action import Action

class AvailableDiskSpace(Action):
  def run(self, str):
    print("AvailableDiskSpace invoked with: " + str)
    return (True, str)
