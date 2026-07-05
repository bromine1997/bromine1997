<div align="center">
  <img src="./assets/header.svg" alt="서보민 (Bromine) — Embedded Developer" width="100%"/>
</div>

<img src="./assets/section-tech.svg" alt="Tech Stack" width="100%"/>

<img src="./assets/tech-stack.svg" alt="MCU: STM32, ESP32, ATmega, Tinker Board 2S / Language: C, C++, Java / PCB: PADS / Tools: Git / IDE: STM32CubeIDE, Keil uVision, Microchip Studio, Arduino IDE, Android Studio" width="100%"/>

<img src="./assets/divider.svg" alt="" width="100%"/>

<img src="./assets/section-projects.svg" alt="Projects" width="100%"/>

<img src="./assets/project-hbot.svg" alt="IoT-Based Hyperbaric Oxygen Chamber Control System" width="100%"/>

<details>
<summary>&nbsp;🏥 <b>세부 스펙 보기 — HBOT Chamber Control System</b></summary>

> Graduate Thesis · 사물인터넷(IoT) 기술을 활용한 안드로이드OS 기반 고압산소챔버 제어 및 모니터링 시스템 개발에 관한 연구
> *Development of an Android OS-Based Control and Monitoring System for Hyperbaric Oxygen Chambers Using Internet of Things (IoT) Technology*

- Schematic design using PADS Logic
- Component selection based on datasheet review (sensors & valve)
- Solenoid driver (DRV110) with Peak-and-Hold PWM — 소비전력 66% 감소
- PID control (4–20 mA proportional valve)
- SPI ADC (MAX1032), DAC Daisy Chain (AD5420)
- Digital isolators (ADUM1400 / ADUM1200 / ISO7421)
- Sensors:
  - MBS3000 · 압력 센서 (4–20 mA)
  - HX93BDC · 온습도 센서 (4–20 mA)
  - AO-09 · 산소 농도 센서 (9–13 mV)
  - SprintIR-WX-100 · CO₂ 농도 센서 (UART)
- WebSocket + REST API-based IoT monitoring

</details>

<img src="./assets/divider.svg" alt="" width="100%"/>

<img src="./assets/project-bike.svg" alt="Rehabilitation Bicycle Force Measurement System" width="100%"/>

<details>
<summary>&nbsp;🚲 <b>세부 스펙 보기 — Rehabilitation Bicycle Force Measurement</b></summary>

> ESP32 Feather V2 기반 4채널 로드셀 동기화 수집 시스템

- 4× ADS1232 interrupt-driven SPI
- Synchronized acquisition across channels
- 2MB PSRAM for extended data logging
- WebSocket-based monitoring using SPIFFS
- Text / Binary selectable storage
- Component selection based on datasheet review

</details>

<img src="./assets/divider.svg" alt="" width="100%"/>

<img src="./assets/project-atmega.svg" alt="ATmega4809 Peripheral Control System" width="100%"/>

<details>
<summary>&nbsp;⚙️ <b>세부 스펙 보기 — ATmega4809 Peripheral Control</b></summary>

> ATmega4809 기반 제어 시스템 · Microchip Studio

- Direct implementation of SPI, TWI(I2C), and UART
- Interrupt-based peripheral handling
- Stepper motor control and rotary switch input processing
- RTC (PCF8563 · DS1621) integration
- External EEPROM (D24FC512) interfacing
- ADC-based analog sensor acquisition

</details>

<img src="./assets/divider.svg" alt="" width="100%"/>

<img src="./assets/section-activity.svg" alt="Activity" width="100%"/>

<img src="./assets/activity-grid.svg" alt="Activity" width="100%"/>

<img src="./assets/divider.svg" alt="" width="100%"/>

<img src="./assets/section-contact.svg" alt="Contact" width="100%"/>

<div align="center">

[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=github&logoColor=white)](https://bromine1997.github.io/portfolio/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/bromine1997)
[![Blog](https://img.shields.io/badge/Blog-20C997?style=for-the-badge&logo=hugo&logoColor=white)](https://bromine1997.github.io/)

</div>

<div align="center">
  <img src="./assets/footer.svg" alt="" width="100%"/>
</div>
