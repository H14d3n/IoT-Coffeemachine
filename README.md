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

- **M5Stack Core**: The main development board.
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

## Functions and Logic

### `clearCache()`

This function resets the values of several global variables and publishes empty values to the MQTT topics.

### `badgeCheck()`

Checks if a badge is present and reads the badge's UID.

### `badgeID()`

Determines which account the badge belongs to and checks if there are enough funds to complete the transaction. It updates the account balance and provides feedback via the RGB LED.

### `buttonA_wasPressed()`, `buttonB_wasPressed()`, `buttonC_wasPressed()`

These functions handle button presses for selecting different coffee sizes. They check the badge, clear the cache, set the price, and initiate the transaction if there are enough funds.

### `ttimer1()`

Handles the completion of the coffee dispensing process, turning off the pump and updating the RGB LED status.

### MQTT Callback Functions

- **`fun_preis_()`**: Updates the displayed transaction amount.
- **`fun_badgeID_()`**: Updates the displayed badge ID.
- **`fun_kontostand_()`**: Updates the displayed account balance.
- **`fun_initPump_()`**: Controls the coffee pump based on the received MQTT message.

## Installation

1. Clone this repository to your local machine.
2. Install the necessary dependencies via the M5Stack UIFlow environment.
3. Configure the MQTT broker IP, username, and password in the code.

## Usage

1. Power on the M5Stack units and ensure they are connected to the same MQTT broker.
2. Present your RFID badge to the coffee machine unit.
3. Select the desired coffee size by pressing the corresponding button.
4. The transaction will be processed, and the coffee will be dispensed if there are sufficient funds.
5. Check the separate display for account balance and transaction details.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
