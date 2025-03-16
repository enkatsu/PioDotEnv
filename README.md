# PioDotEnv

This library performs constant definitions by .env files in PlatformIO projects.

## Installation

Yo can do something like this. Edit platformio.ini and add:

```ini
lib_deps =
    https://github.com/enkatsu/PioDotEnv.git
```

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
    WiFi.begin(DEF_TO_STRING(WIFI_SSID), DEF_TO_STRING(WIFI_PASS));
}

void loop() {
}
```
