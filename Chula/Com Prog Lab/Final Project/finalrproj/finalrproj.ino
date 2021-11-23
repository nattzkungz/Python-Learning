// Template ID, Device Name and Auth Token are provided by the Blynk.Cloud
// See the Device Info tab, or Template settings
#define BLYNK_TEMPLATE_ID           "TMPLerLnR0SA"
#define BLYNK_DEVICE_NAME           "Quickstart Device"
#define BLYNK_AUTH_TOKEN            "AgSCRDEJ7OARSow5Uk6mUCmOpLMYNiaz"

// Comment this out to disable prints and save space
#define BLYNK_PRINT Serial

#include <WiFi.h>
#include <WiFiClient.h>
#include <BlynkSimpleEsp32.h>
#include <DHT.h>

char auth[] = "AgSCRDEJ7OARSow5Uk6mUCmOpLMYNiaz";
char ssid[] = "americanpie";
char pass[] = "ra1su5555";

#define DHTPIN 2          // What digital pin we're connected to
#define DHTTYPE DHT11     // DHT 11
const int ledPin = 22;
int ledState = LOW;

DHT dht(DHTPIN, DHTTYPE);
BlynkTimer timer;

// This function sends Arduino's up time every second to Virtual Pin (5).

BLYNK_CONNECTED() {
  Blynk.syncVirtual(V2);
}

// When App button is pushed - switch the state
BLYNK_WRITE(V2) {
  ledState = param.asInt();
  digitalWrite(ledPin, ledState);
}
void sendSensor()
{
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (isnan(h) || isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  Blynk.virtualWrite(V5, h);
  Blynk.virtualWrite(V6, t);
}

void setup()
{
  Serial.begin(115200);

  Blynk.begin(auth, ssid, pass);
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, ledState);
  dht.begin();
  timer.setInterval(1000L, sendSensor);
}

void loop()
{
  Blynk.run();
  timer.run();
}
