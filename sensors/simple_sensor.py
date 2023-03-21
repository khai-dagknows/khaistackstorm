from st2reactor.sensor.base import Sensor
import eventlet
import random

class SimpleSensor(Sensor):
    def __init__(self, sensor_service, config):
        super(HelloSensor, self).__init__(sensor_service=sensor_service, config=config)
        self._logger = self.sensor_service.get_logger(name=self.__class__.__name__)
        self._stop = False

    def setup(self):
        pass

    def run(self):
        while not self._stop:
            self._logger.debug("HelloSensor dispatching trigger...")

            list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            choice = random.choice(list1)

            payload = {"random_number": choice}
            self.sensor_service.dispatch(trigger="khai_simple_sensor_event", payload=payload)
            eventlet.sleep(60)

        pass

    def cleanup(self):
        self._stop = True
        pass

    def add_trigger(self, trigger):
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass
