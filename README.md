# 📦 RFID Inventory Warehouse System

A lightweight, WiFi-enabled inventory management solution that automates the tracking of goods moving in and out of a facility using RFID technology.

## 🚀 Features
- **Instant Identification:** Scans passive RFID tags to identify items in milliseconds.
- **Stock Analytics:** Tracks "In-flow" vs "Out-flow" to provide real-time stock levels.
- **Automated Reordering:** Flags items that fall below a set threshold.
- **Wireless Sync:** Connects directly to the dashboard via WiFi without a host PC.

## ⚙️ Engineering Logic
- **Hardware:** NodeMCU interfaces with the MFRC522 RFID module via SPI communication.
- **Software:** Python manages a localized database (or CSV) to cross-reference Tag IDs with product names and quantities.
