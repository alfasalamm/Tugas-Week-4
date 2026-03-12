import paho.mqtt.client as mqtt

subscribe_topic = "alfasalamm"
server = "mqtt-dashboard.com"

def on_connect(client, userdata, flags, rc, properties):
    if rc == 0:
        print("Berhasil terhubung")
        client.subscribe(subscribe_topic)
    else:
        print("Gagal koneksi, kode:", rc)

def on_message(client, userdata, message):
    print("Data diterima:", message.payload.decode())

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect(server, 1883, 60)
client.loop_forever()