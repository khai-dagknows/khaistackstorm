import sys

from st2common.runners.base_action import Action

class TopMemoryConsumers(Action):
  def run(self, str):
    print("TopMemoryConsumers invoked with: " + str)
    return (True, str)
