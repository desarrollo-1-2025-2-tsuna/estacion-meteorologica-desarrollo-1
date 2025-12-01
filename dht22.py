import dht
import machine

class DHT22Sensor:
  def __init__(self, pin_number):
    self.sensor = dht.DHT22(machine.Pin(pin_number))
    self.pin_number = pin_number
    try:
      self.sensor.measure()
      self.temperature = self.sensor.temperature()
      self.humidity = self.sensor.humidity()
    except Exception as e:
      print("Error inicializando el sensor en el pin {}: {}".format(pin_number, e))
      self.temperature = None
      self.humidity = None

  def getTemperature(self):
    try:
      self.sensor.measure()
      self.temperature = self.sensor.temperature()
    except Exception as e:
      print("Error leyendo la temperatura en el pin {}: {}".format(self.pin_number, e))
      self.temperature = None
    return self.temperature

  def getHumidity(self):
    try:
      self.sensor.measure()
      self.humidity = self.sensor.humidity()
    except Exception as e:
      print("Error leyendo la humedad en el pin {}: {}".format(self.pin_number, e))
      self.humidity = None
    return self.humidity