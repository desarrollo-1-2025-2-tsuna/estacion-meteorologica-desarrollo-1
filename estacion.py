import dht22
import anemo
import rain_gauge
import machine
import network
import mqtt_client
import socket

class EstacionMeteorologica:
  def __init__(self, 
    dht_pin,
    anemo_pin,
    pluvio_pin
  ):
    self.send_time_s = 10

    self.rtc = machine.RTC()
    self.dht_sensor = dht22.DHT22Sensor(pin_number=dht_pin)
    self.anemo_sensor = anemo.AnemometroSensor(pin_number=anemo_pin)
    self.pluvio_sensor = rain_gauge.PluviometroSensor(pin_number=pluvio_pin)

    self.measures = {
      'tiempo': self.rtc.datetime(),
      'temperatura': None,
      'humedad': None,
      'viento': None,
      'lluvia': None,
      }

    self.connections = [
      {'SSID' : "Tsuna's Infinix Note 40 Pro", 'PASSWORD' : 'joanisa21'},
      {'SSID' : 'Univalle', 'PASSWORD' : 'Univalle'},
    ]

    self.wlan = network.WLAN()
    self.initializeWifi()

    self.mqtt_client = None
    self.initializeMQTT()

  def getTime(self):
    self.measures['tiempo'] = self.rtc.datetime()

  def getTemperature(self):
    self.measures['temperatura'] = self.dht_sensor.getTemperature()

  def getHumidity(self):
    self.measures['humedad'] = self.dht_sensor.getHumidity()

  def getWind(self):
    self.measures['viento'] = self.anemo_sensor.getWindSpeed()

  def getRain(self):
    self.measures['lluvia'] = self.pluvio_sensor.getRainfall()

  def getMeasures(self):
    self.getTime()
    self.getTemperature()
    self.getHumidity()
    self.getWind()
    self.getRain()

  def sendMeasures(self):
    print("Enviando mediciones:", self.measures)

    try:
      self.mqtt_client.publish(
        topic="estacion/mediciones",
        msg=str(self.measures)
      )
      print("Mediciones enviadas correctamente.")
    except Exception as e:
      print("Error al enviar las mediciones:", e)
      self.mqtt_client.connected = False

  def initializeWifi(self):
    self.wlan.active(True)
    if not self.wlan.isconnected():
      for connection in self.connections:
        self.wlan.connect(connection['SSID'], connection['PASSWORD'])
        while not self.wlan.isconnected():
          machine.idle()

        if self.wlan.isconnected():
          break

    print('Conexión WiFi establecida:', self.wlan.ifconfig(), self.wlan.status())

    s = socket.socket()
    s.connect(("8.8.8.8", 53))
    s.close()

  def initializeMQTT(self):
    if self.mqtt_client is not None:
      try:
        self.mqtt_client.client.disconnect()
      except Exception as e:
        pass

    self.mqtt_client = mqtt_client.MQTTClient(
      client_id="estacion_meteorologica_1",
      server="192.168.20.27",
    )
