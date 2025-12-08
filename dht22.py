import dht
import machine

# Se crea la clase del DHT22
class DHT22Sensor:
  # El constructor recibe el pin donde está conectado el sensor
  # y se inicializan las variables de temperatura y humedad
  # En caso de error al inicializar el sensor, se capturan las excepciones
  def __init__(self, pin_number):
    self.sensor = dht.DHT22(machine.Pin(pin_number))
    self.pin_number = pin_number
    try:
      self.sensor.measure()
      self.temperature = self.sensor.temperature()
      self.humidity = self.sensor.humidity()
    except Exception as e:
      self.temperature = None
      self.humidity = None

  # Método para obtener la temperatura
  # Se captura cualquier excepción que pueda ocurrir durante la lectura
  def getTemperature(self):
    try:
      self.sensor.measure()
      self.temperature = self.sensor.temperature()
    except Exception as e:
      self.temperature = None
    return self.temperature

  # Método para obtener la humedad
  # Se captura cualquier excepción que pueda ocurrir durante la lectura
  def getHumidity(self):
    try:
      self.sensor.measure()
      self.humidity = self.sensor.humidity()
    except Exception as e:
      self.humidity = None
    return self.humidity

# El sensor no utiliza un protocolo demasiado complejo por que
# no es necesario implementar métodos adicionales para restablecer la conexión o manejar estados.