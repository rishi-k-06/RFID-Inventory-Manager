#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 4  // D2
#define RST_PIN 5 // D1
MFRC522 mfrc522(SS_PIN, RST_PIN);

void setup() {
  Serial.begin(115200);
  SPI.begin();
  mfrc522.PCD_Init();
  // WiFi Connection logic for ESP8266
}

void loop() {
  if (!mfrc522.PICC_IsNewCardPresent() || !mfrc522.PICC_ReadCardSerial()) return;

  String tagID = "";
  for (byte i = 0; i < mfrc522.uid.size; i++) {
    tagID += String(mfrc522.uid.uidByte[i], HEX);
  }
  tagID.toUpperCase();
  Serial.println("Scanned Tag: " + tagID);

  HTTPClient http;
  WiFiClient client;
  http.begin(client, "http://your-warehouse-app.com/scan");
  http.addHeader("Content-Type", "application/json");
  
  String json = "{\"id\":\"" + tagID + "\"}";
  http.POST(json);
  http.end();

  delay(2000); // Prevent duplicate scans
}
