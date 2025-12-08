import machine
import time
import umqtt.simple as mqtt

class MQTTClient:
  def __init__(self, client_id, server, port=1883, user=None, password=None):
    try:
      self.client = mqtt.MQTTClient(client_id, server, port, user, password)
      self.client.connect()
      self.connected = True
    except Exception as e:
      self.connected = False

  def publish(self, topic, msg):
    self.client.publish(topic, msg)

  def subscribe(self, topic):
    self.client.subscribe(topic)

  def set_callback(self, callback):
    self.client.set_callback(callback)

  def check_msg(self):
    self.client.check_msg()