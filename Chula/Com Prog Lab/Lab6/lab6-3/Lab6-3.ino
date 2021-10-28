#include <M5Stack.h>
#include <Arduino.h>

#include <WiFi.h>
#include <WiFiMulti.h>

#include <HTTPClient.h>

#define USE_SERIAL Serial

WiFiMulti wifiMulti;


void setup() {

    USE_SERIAL.begin(115200);

    USE_SERIAL.println();
    USE_SERIAL.println();
    USE_SERIAL.println();

    for(uint8_t t = 4; t > 0; t--) {
        USE_SERIAL.printf("[SETUP] WAIT %d...\n", t);
        USE_SERIAL.flush();
        delay(1000);
    }

    wifiMulti.addAP("americanpie", "ra1su5555");

}

String ip = "http://ip-api.com/json/";


void loop() {
    if (M5.BtnA.wasPressed()) {
      ip = "http://ip-api.com/json/161.200.192.243";
    } else if (M5.BtnB.wasPressed()) {
      ip = "http://ip-api.com/json/202.47.249.7";
    } else if (M5.BtnC.wasPressed()) {
      ip = "http://ip-api.com/json/203.131.212.198";
    }
    // wait for WiFi connection
    if((wifiMulti.run() == WL_CONNECTED)) {
        HTTPClient http;
        USE_SERIAL.print("[HTTP] begin...\n");
        http.begin(ip); 
        USE_SERIAL.print("[HTTP] GET...\n");
        int httpCode = http.GET();
        if(httpCode > 0) {
            USE_SERIAL.printf("[HTTP] GET... code: %d\n", httpCode);
            if(httpCode == HTTP_CODE_OK) {
                String payload = http.getString();
                USE_SERIAL.println(payload);
            }
        } else {
            USE_SERIAL.printf("[HTTP] GET... failed, error: %s\n", http.errorToString(httpCode).c_str());
        }
        http.end();
    }
    delay(1000);
    M5.update();
}
