from m5stack import *
from m5ui import *
from uiflow import *
from m5mqtt import M5mqtt
import time
import unit


setScreenColor(0xffffff)
rgb_0 = unit.get(unit.RGB, unit.PORTB)
rfid_0 = unit.get(unit.RFID, unit.PORTA)


Konto1 = None
Konto2 = None
badgeConnected = None
BadgeUID = None
Preis = None
enoughMoney = None



Title1 = M5Title(title="Kaffeemaschine", x=3, fgcolor=0xFFFFFF, bgcolor=0x5c4d09)
kaffeeklein = M5TextBox(18, 203, "Kaffee Klein", lcd.FONT_Default, 0x000000, rotate=0)
kaffeemittel = M5TextBox(118, 203, "Kaffee Mittel", lcd.FONT_Default, 0x000000, rotate=0)
kaffeegross = M5TextBox(217, 203, "Kaffee Gross", lcd.FONT_Default, 0x000000, rotate=0)
image0 = M5Img(1, 45, "res/coffee.jpg", True)
preis1 = M5TextBox(26, 219, "1.50 CHF", lcd.FONT_Default, 0x000000, rotate=0)
preis2 = M5TextBox(126, 219, "2.50 CHF", lcd.FONT_Default, 0x000000, rotate=0)
preis3 = M5TextBox(229, 219, "3.50 CHF", lcd.FONT_Default, 0x000000, rotate=0)


# Describe this function...
def clearCache():
  global Konto1, Konto2, badgeConnected, BadgeUID, Preis, enoughMoney
  m5mqtt.publish(str('preis'), str(None), 0)
  m5mqtt.publish(str('badgeID'), str(None), 0)
  m5mqtt.publish(str('kontostand'), str(None), 0)

# Describe this function...
def badgeCheck():
  global Konto1, Konto2, badgeConnected, BadgeUID, Preis, enoughMoney
  if rfid_0.isCardOn():
    badgeConnected = True
    BadgeUID = rfid_0.readUid()
  else:
    badgeConnected = False

# Describe this function...
def badgeID():
  global Konto1, Konto2, badgeConnected, BadgeUID, Preis, enoughMoney
  if BadgeUID == '49b674a81':
    m5mqtt.publish(str('preis'), str(Preis), 1)
    m5mqtt.publish(str('badgeID'), str('49b674a81'), 1)
    if Konto1 >= Preis:
      Konto1 = Konto1 - Preis
      m5mqtt.publish(str('kontostand'), str(Konto1), 1)
      enoughMoney = True
    else:
      m5mqtt.publish(str('kontostand'), str('Saldo zu klein'), 1)
      enoughMoney = False
  else:
    m5mqtt.publish(str('preis'), str(Preis), 1)
    m5mqtt.publish(str('badgeID'), str('96175a17'), 1)
    if Konto2 >= Preis:
      Konto2 = Konto2 - Preis
      m5mqtt.publish(str('kontostand'), str(Konto2), 1)
      enoughMoney = True
    else:
      m5mqtt.publish(str('kontostand'), str('Saldo zu klein'), 1)
      enoughMoney = False


def buttonA_wasPressed():
  global Konto1, Konto2, badgeConnected, BadgeUID, Preis, enoughMoney
  badgeCheck()
  if badgeConnected == True:
    clearCache()
    wait_ms(10)
    Preis = 1.5
    badgeID()
    if enoughMoney == True:
      rgb_0.setColorAll(0xffcc00)
      m5mqtt.publish(str('initPump'), str(True), 0)
      timerSch.run('timer1', 8000, 0x01)
    else:
      rgb_0.setColorAll(0xff0000)
  else:
    rgb_0.setColorAll(0xff0000)
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  global Konto1, Konto2, badgeConnected, BadgeUID, Preis, enoughMoney
  badgeCheck()
  if badgeConnected == True:
    clearCache()
    wait_ms(10)
    Preis = 2.5
    badgeID()
    if enoughMoney == True:
      rgb_0.setColorAll(0xffcc00)
      m5mqtt.publish(str('initPump'), str(True), 0)
      timerSch.run('timer1', 12000, 0x01)
    else:
      rgb_0.setColorAll(0xff0000)
  else:
    rgb_0.setColorAll(0xff0000)
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonC_wasPressed():
  global Konto1, Konto2, badgeConnected, BadgeUID, Preis, enoughMoney
  badgeCheck()
  if badgeConnected == True:
    clearCache()
    wait_ms(10)
    Preis = 3.5
    badgeID()
    if enoughMoney == True:
      rgb_0.setColorAll(0xffcc00)
      m5mqtt.publish(str('initPump'), str(True), 0)
      timerSch.run('timer1', 16000, 0x01)
    else:
      rgb_0.setColorAll(0xff0000)
  else:
    rgb_0.setColorAll(0xff0000)
  pass
btnC.wasPressed(buttonC_wasPressed)

@timerSch.event('timer1')
def ttimer1():
  global Konto1, Konto2, badgeConnected, BadgeUID, Preis, enoughMoney
  m5mqtt.publish(str('initPump'), str(False), 0)
  rgb_0.setColorAll(0x33cc00)
  speaker.sing(247, 1)
  pass


Konto1 = 120
Konto2 = 1.5
m5mqtt = M5mqtt('maschine', '10.5.43.47', 1883, 'admin', 'Bfo12345', 300)
m5mqtt.start()
m5mqtt.publish(str('Status'), str('Online'), 0)
m5mqtt.set_last_will(str('Status'),str('Offline'))
while True:
  wait_ms(2)
