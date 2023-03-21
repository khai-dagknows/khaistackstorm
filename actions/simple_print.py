import sys

from st2common.runners.base_action import Action

class SimplePrint(Action):
    def run(self, message):
        print(message)

        return (True, message)
