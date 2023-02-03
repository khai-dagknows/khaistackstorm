import sys

from st2common.runners.base_action import Action

class CpuUsage(Action):
  def run(self, str):
    print("CpuUsage invoked with: " + str)
    return (True, 80)
