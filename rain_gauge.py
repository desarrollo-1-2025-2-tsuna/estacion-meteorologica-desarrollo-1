import machine
import time

class PluviometroSensor:
  def __init__(self, pin_number):
    self.pin_number = pin_number

    self.counter_rain = 0

    self.time_rain = 0
    self.precipitation = 0

    self.pin = machine.Pin(pin_number, machine.Pin.IN, machine.Pin.PULL_UP)
    self.pin.irq(trigger=machine.Pin.IRQ_FALLING, handler=self.contadorCallback)

  def getRainfall(self):
    self.precipitation = self.counter_rain * 0.2794
    self.counter_rain = 0
    return self.precipitation

  def contadorCallback(self, pin):
    if (time.ticks_ms() - self.time_rain) > 150:
      self.counter_rain += 1
      self.time_rain = time.ticks_ms()
