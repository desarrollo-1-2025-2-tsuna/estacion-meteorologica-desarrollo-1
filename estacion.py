import dht22
import machine

class EstacionMeteorologica:
    def __init__(self, dht_pin):
      self.rtc = machine.RTC()
      self.dht_sensor = dht22.DHT22Sensor(pin_number=dht_pin)

      self.mediciones = {
        'tiempo': self.rtc.datetime(),
        'temperatura': None,
        'humedad': None
       }

    def obtener_tiempo(self):
      self.mediciones['tiempo'] = self.rtc.datetime()

    def obtener_temperatura(self):
      self.mediciones['temperatura'] = self.dht_sensor.getTemperature()

    def obtener_humedad(self):
      self.mediciones['humedad'] = self.dht_sensor.getHumidity()

    def obtener_mediciones(self):
      self.obtener_tiempo()
      self.obtener_temperatura()
      self.obtener_humedad()
      return self.mediciones