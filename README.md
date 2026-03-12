# 안녕하세요 👋 / Hi there

**Biomedical Engineering M.S. · Firmware & Embedded Systems**  
의료기기 · 산업 인프라를 위한 펌웨어 개발에 관심이 있습니다.

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
> Tinker board 2s를 활용한  기반 고압 산소 챔버 제어 시스템 

- PID control ( 비례제어 벨브 4 ~ 20MA )
- SPI ADC (MAX1032), DAC Daisy Chain (AD5420), digital isolators (ADUM1400 / ISO7421)
- Solenoid driver (DRV110), sensors: MBS3000 · HX93BDC · AO-09 · SprintIR-WX-100
- 9-item regulatory validation (의료기기 규격 검증 9항목 수행)
- WebSocket + REST API 기반 IoT 모니터링

---

### 🚲 Rehabilitation Bicycle Force Measurement
> ESP32 Feather V2 기반 4채널 로드셀 동기화 수집 시스템

- 4× ADS1232 interrupt-driven SPI, synchronized across channels 
- PSRAM 2MB 활용 — 최대 36분 / 1.65MB 무지연 버퍼링
- Real-time web monitor via WebSocket (SPIFFS hosted)
- Text / Binary 선택 저장

---

## 📫 Contact

[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=flat&logo=github&logoColor=white)](https://bromine1997.github.io/web-porfolio)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/bromine1997)
