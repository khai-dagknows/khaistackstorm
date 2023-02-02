import sys

from st2common.runners.base_action import Action

class ParseMemoryUsage(Action):
  def run(self, str):
    print("ParseMemoryUsage invoked")
    return (True, 2286456)
