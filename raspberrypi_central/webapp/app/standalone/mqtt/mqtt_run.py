from utils.django.standalone_init import init
init()


from utils.mqtt import mqtt_factory  # noqa: E402
from alarm.mqtt import register  # noqa: E402

mqtt = mqtt_factory(client_id='hello-world')

register(mqtt)

mqtt._client.loop_forever()
