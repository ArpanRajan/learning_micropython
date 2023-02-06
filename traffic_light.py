from machine import Pin
import utime

class Light:
    """Represents a single light. Owns the Pin for the light, and is responsible for activating it
    """
    def __init__(self, pin_no, duration):
        """Inits the Light

        Args:
            pin_no (int): GPIO pin number.
            duration (int): seconds to run the light
        """
        self.pin = Pin(pin_no, Pin.OUT)
        self.duration = duration
        self.pin.off()
    
    def activate(self):
        """Activates the light for duration number of seconds.
        """
        self.pin.on()
        utime.sleep(self.duration)
        self.pin.off()
    
class TrafficLight:
    """Represents a traffic light, with a go, slow, and stop signal.
    Light order is stop, slow, go.
    """
    def __init__(self, go_num, slow_num, stop_num):
        self.go = Light(go_num, 5)
        self.slow = Light(slow_num, 2)
        self.stop = Light(stop_num, 7)

        self.lights = [self.stop, self.slow, self.go]

    def run(self):
        """Activate each light in order.
        """
        for light in self.lights:
            light.activate()

if __name__ == '__main__':
    l = TrafficLight(13, 14, 15)
    while True:
        l.run()
