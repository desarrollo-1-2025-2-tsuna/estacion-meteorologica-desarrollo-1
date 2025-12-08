import machine
import time

class AnemometroSensor:
  def __init__(self, pin_number):
    self.pin_number = pin_number

    self.counter_wind = 0
    self.time_wind_speed = 50
    self.time_wind = 0
    self.wind_speed = 0

    self.pin = machine.Pin(pin_number, machine.Pin.IN, machine.Pin.PULL_UP)
    self.pin.irq(trigger=machine.Pin.IRQ_FALLING, handler=self.contadorCallback)

  def getWindSpeed(self):
    self.wind_speed = self.counter_wind * 2.4 / self.time_wind_speed
    self.counter_wind = 0
    return self.wind_speed

  def contadorCallback(self, pin):
    if (time.ticks_ms() - self.time_wind) > 150:
      self.counter_wind += 1
      self.time_wind = time.ticks_ms()
