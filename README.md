# Smart Coffee Machine Project

This project involves the development of a smart coffee machine using the M5Stack platform. The system allows users to purchase coffee using an RFID badge, and it automatically deducts the corresponding amount from their account. The system is designed to be interactive, providing real-time feedback via LEDs and an integrated display.

## Table of Contents

- [Hardware Components](#hardware-components)
- [Software Components](#software-components)
- [Project Description](#project-description)
- [Functions and Logic](#functions-and-logic)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Hardware Components

- **M5GO IoT Kit**: The main development board.
- **RGB LED Unit**: Provides visual feedback to the user.
- **RFID Unit**: Used to scan and identify user badges.
- **Watering Unit**: Controls the pump for dispensing coffee.

## Software Components

- **uiflow**: The M5Stack development environment.
- **M5mqtt**: MQTT library for handling communication between the machine and the display.
- **M5ui**: User interface library for the M5Stack display.

## Project Description

The project consists of two main parts:

1. **Coffee Machine Interface**: Displays coffee options and prices on the screen, and uses an RFID badge to deduct money from the user's account.
2. **Account Balance Display**: Shows the current balance and transaction details on a separate M5Stack display.

### Coffee Machine Interface

The coffee machine offers three types of coffee with different prices. The user can select a coffee size by pressing one of the three buttons (A, B, C). The system checks if the user has sufficient funds in their account. If the user has enough money, the system will proceed to dispense the coffee, otherwise, it will notify the user of insufficient funds.

### Account Balance Display

This part of the project runs on a separate M5Stack unit and subscribes to the relevant MQTT topics to display the badge ID, transaction amount, and updated account balance.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
