from machine import Pin
from neopixel import NeoPixel
import time
import estacion

estacion = estacion.EstacionMeteorologica(
  dht_pin=4,
)

def main():
  while True:
    measurements = estacion.obtener_mediciones()
    time.sleep(1)
    print(measurements['tiempo'])
    print(measurements['temperatura'])
    print(measurements['humedad'])

if __name__ == "__main__":
  main()