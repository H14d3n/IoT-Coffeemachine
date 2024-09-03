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
