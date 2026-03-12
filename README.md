# 안녕하세요 👋 / Hi there

**회로 설계부터 펌웨어, 제어까지 실제 시스템을 구현하는 임베디드 개발자입니다.**  
*From schematic to firmware to control — I build systems that work in the real world.*

---

## 🛠 Tech Stack

**Microcontrollers**  
![STM32](https://img.shields.io/badge/STM32-03234B?style=flat&logo=stmicroelectronics&logoColor=white)
![ESP32](https://img.shields.io/badge/ESP32-E7352C?style=flat&logo=espressif&logoColor=white)
![ATmega](https://img.shields.io/badge/ATmega-00979D?style=flat&logo=arduino&logoColor=white)

**Interface & Protocol**  
![SPI](https://img.shields.io/badge/SPI-555555?style=flat)
![I2C](https://img.shields.io/badge/I2C-555555?style=flat)
![UART](https://img.shields.io/badge/UART-555555?style=flat)
![WebSocket](https://img.shields.io/badge/WebSocket-010101?style=flat)

**Tools**  
![C](https://img.shields.io/badge/C-A8B9CC?style=flat&logo=c&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=flat&logo=cplusplus&logoColor=white)
![Arduino](https://img.shields.io/badge/Arduino-00878A?style=flat&logo=arduino&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)

---

## 📂 Projects

### 🏥 Development of an Android OS-Based Control and Monitoring System for Hyperbaric Oxygen Chambers Using Internet of Things (IoT) Technology — *Graduate Thesis*
> Tinker board 2s를 활용한 고압 산소 챔버 제어 시스템

- PID control (비례제어 밸브 4~20mA)
- SPI ADC (MAX1032), DAC Daisy Chain (AD5420), digital isolators (ADUM1400 / ISO7421)
- Solenoid driver (DRV110), sensors: MBS3000 · HX93BDC · AO-09 · SprintIR-WX-100
- 9-item regulatory validation (의료기기 규격 검증 9항목 수행)
- WebSocket + REST API 기반 IoT 모니터링

---

### 🚲 Rehabilitation Bicycle Force Measurement
> ESP32 Feather V2 기반 4채널 로드셀 동기화 수집 시스템

- 4× ADS1232 interrupt-driven SPI, synchronized across channels
- PSRAM 2MB 활용 — 최대 36분 
- WebSocket (using SPIFFS) 
- Text / Binary 선택 저장

---

### ⚙️ ATmega4809 Peripheral Control System
> ATmega4809 기반 제어 시스템 / Microchip Studio

- SPI · TWI(I2C) · UART 인터페이스 직접 구현 ( Interrupt)
- Stepper motor 제어, Rotary SW 입력 처리
- RTC (PCF8563 · DS1621), External EEPROM (D24FC512) 연동
- ADC 기반 아날로그 센서 수집

---

## 📫 Contact

[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=flat&logo=github&logoColor=white)](https://bromine1997.github.io/web-porfolio)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/bromine1997)

