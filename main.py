from machine import Pin
from neopixel import NeoPixel
import time
import estacion

estacion = estacion.EstacionMeteorologica(
  dht_pin=4,
)

def main():
  while True:
    checkear_conexion()

    measurements = estacion.obtener_mediciones()
    time.sleep(1)
    print(measurements['tiempo'])
    print(measurements['temperatura'])
    print(measurements['humedad'])

def checkear_conexion():
  if not estacion.wlan.isconnected():
    estacion.inicializar_wifi()

if __name__ == "__main__":
  main()