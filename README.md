# PioDotEnv

This library performs constant definitions by .env files in PlatformIO projects.

## Usage

You can read the constants in the code by adding a `.env` file to the project root

```.env
WIFI_SSID=YOUR_WIFI_SSID_SSID
WIFI_PASS=YOUR_WIFI_PASS
```

```cpp
#include <Arduino.h>
#include <WiFi.h>
#include <PioDotEnv.h>

void setup() {
    Serial.begin(115200);
    WiFi.begin(DEF_TO_STR(WIFI_SSID), DEF_TO_STR(WIFI_PASS));
    Serial.printf("SSID: %s", DEF_TO_STR(WIFI_SSID));
    while (WiFi.status() != WL_CONNECTED) {
        Serial.print(".");
        delay(500);
    }
    Serial.println();
    Serial.printf("IP Address: %s", WiFi.localIP().toString());
}

void loop() {
}
```
