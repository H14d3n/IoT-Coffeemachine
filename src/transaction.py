from m5stack import *
from m5ui import *
from uiflow import *
from m5mqtt import M5mqtt
import unit


setScreenColor(0x222222)
Watering_0 = unit.get(unit.WATERING, unit.PORTB)






Title = M5Title(title="Kontostand", x=3, fgcolor=0xFFFFFF, bgcolor=0x0000FF)
badgelabel = M5TextBox(15, 46, "Badge:", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
badgeID = M5TextBox(135, 46, "-", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
transaktionlabel = M5TextBox(15, 107, "Transaktion:", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
kontolabel = M5TextBox(15, 175, "Kontostand:", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
transaktion = M5TextBox(197, 107, "-", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
konto = M5TextBox(197, 175, "-", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)

def fun_preis_(topic_data):
  # global params
  transaktion.setText(str((str(topic_data) + str('CHF'))))
  pass

def fun_badgeID_(topic_data):
  # global params
  badgeID.setText(str(topic_data))
  pass

def fun_kontostand_(topic_data):
  # global params
  konto.setText(str((str(topic_data) + str('CHF'))))
  pass

def fun_initPump_(topic_data):
  # global params
  if topic_data == 'True':
    Watering_0.set_pump_status(1)
  else:
    Watering_0.set_pump_status(0)
  pass


m5mqtt = M5mqtt('anzeige', '10.5.43.47', 1883, 'admin', 'Bfo12345', 300)
m5mqtt.subscribe(str('preis'), fun_preis_)
m5mqtt.subscribe(str('badgeID'), fun_badgeID_)
m5mqtt.subscribe(str('kontostand'), fun_kontostand_)
m5mqtt.subscribe(str('initPump'), fun_initPump_)
m5mqtt.start()
while True:
  wait_ms(2)
