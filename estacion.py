import dht22
import machine
import network

class EstacionMeteorologica:
  def __init__(self, dht_pin):
    self.rtc = machine.RTC()
    self.dht_sensor = dht22.DHT22Sensor(pin_number=dht_pin)

    self.mediciones = {
      'tiempo': self.rtc.datetime(),
      'temperatura': None,
      'humedad': None
      }

    self.conexiones = [
      {'SSID' : 'Univalle', 'PASSWORD' : 'Univalle'},
      {'SSID' : 'VILLAMIL', 'PASSWORD' : 'solylulu12345678'},
    ]

    self.wlan = network.WLAN()
    self.inicializar_wifi()

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

  def inicializar_wifi(self):
    self.wlan.active(True)
    if not self.wlan.isconnected():
      for conexion in self.conexiones:
        self.wlan.connect(conexion['SSID'], conexion['PASSWORD'])
        while not self.wlan.isconnected():
          machine.idle()

        if self.wlan.isconnected():
          break

    print('Conexión WiFi establecida:', self.wlan.ifconfig())