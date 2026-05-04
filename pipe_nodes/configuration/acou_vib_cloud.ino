#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <PubSubClient.h>
#include "super_secret2.h"

// Sensor pins
#define SOUND_PIN 33
#define VIB_PIN 34

const char* ssid = WIFI_SSID;
const char* password = WIFI_PASS;

const char* AWS_ENDPOINT = AWS_END;
const char* DEVICE_ID = DEV_ID;

WiFiClientSecure net;
PubSubClient client(net);

void setup() {
  Serial.begin(115200);
  connectAWS();
}

void loop() {

  if (!client.connected()) {
    connectAWS();
  }

  client.loop();

  // Read sensors
  int soundLevel = analogRead(SOUND_PIN);
  int vibration = analogRead(VIB_PIN);

  Serial.print("Sound: ");
  Serial.print(soundLevel);
  Serial.print(" | Vibration: ");
  Serial.println(vibration);

  // Create JSON payload
  String payload = "{";
  payload += "\"node\":\"node01\",";
  payload += "\"acoustic\":" + String(soundLevel) + ",";
  payload += "\"vibration\":" + String(vibration);
  payload += "}";

  // Publish to AWS IoT
  client.publish("leaksensor/node01/data", payload.c_str());

  Serial.println("Message published");

  delay(1000);  // faster than before, adjust if needed
}

void connectAWS() {

  Serial.println("Connecting to WiFi...");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi Connected");

  // Certificates
  net.setCACert(ROOT_CA);
  net.setCertificate(DEVICE_CERT);
  net.setPrivateKey(PRIVATE_KEY);

  client.setServer(AWS_ENDPOINT, 8883);

  Serial.println("Connecting to AWS IoT...");

  while (!client.connect(DEVICE_ID)) {
    Serial.print(".");
    delay(1000);
  }

  Serial.println("\nConnected to AWS IoT!");
}