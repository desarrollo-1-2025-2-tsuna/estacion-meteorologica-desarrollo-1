from machine import Pin
from neopixel import NeoPixel
import time
import estacion

estacion = estacion.EstacionMeteorologica(
  dht_pin=4,
  anemo_pin=5,
  pluvio_pin=9,
)

def main():
  start_time = time.ticks_ms()

  while True:
    checkearConexion()

    estacion.getMeasures()

    tiempo_transcurrido = time.ticks_diff(time.ticks_ms(), start_time)
    
    if tiempo_transcurrido >= estacion.send_time_s * 1000:
      start_time = time.ticks_ms()
      estacion.sendMeasures()

    time.sleep_ms(100)

def checkearConexion():
  if not estacion.wlan.isconnected():
    estacion.initializeWifi()

  if not estacion.mqtt_client.connected:
    estacion.initializeMQTT()

if __name__ == "__main__":
  main()