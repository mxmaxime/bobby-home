from camera.detect_motion import DetectMotion
from pathlib import Path 
from sound.sound import Sound
import paho.mqtt.client as mqtt
import json


class Camera():

    def __init__(self, get_mqtt_client):
        self.mqtt_client = get_mqtt_client(client_name='rpi4-alarm-motion-DETECT')

    def start(self):
        from picamera import PiCamera
        DetectMotion(PiCamera(), self._presenceCallback)

    def _presenceCallback(self, presence: bool, picture_path: str):
        payload = {
            # @TODO
            'device_id': 'some device id',
        }

        self.mqtt_client.publish('motion/camera', payload=json.dumps(payload), qos=1)

        with open(picture_path, 'rb') as image:
            filecontent = image.read()
            byteArr = bytes(filecontent)

        self.mqtt_client.publish('motion/picture', payload=byteArr, qos=1)
        # s = Sound()
        # s.alarm()
