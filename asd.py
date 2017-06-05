#!/usr/bin/python

import time
import pyupm_ili9341 as ili9341

# Pins (Edison)
# CS_LCD   GP44 (MRAA 31)
# CS_SD    GP43 (MRAA 38) unused
# DC       GP12 (MRAA 20)
# RESEST   GP13 (MRAA 14)
lcd = ili9341.ILI9341(31, 38, 20, 14)

# Fill the screen with a solid color
lcd.fillScreen(lcd.color565(0, 40, 16))

# Draw some shapes
lcd.drawFastVLine(10, 10, 100, ili9341.ILI9341_RED)
lcd.drawFastHLine(20, 10, 50, ili9341.ILI9341_CYAN)
lcd.drawLine(160, 30, 200, 60, ili9341.ILI9341_GREEN)
lcd.fillRect(20, 30, 75, 60, ili9341.ILI9341_ORANGE)
lcd.drawCircle(70, 50, 20, ili9341.ILI9341_PURPLE)
lcd.fillCircle(120, 50, 20, ili9341.ILI9341_PURPLE)
lcd.drawTriangle(50, 100, 10, 140, 90, 140, ili9341.ILI9341_YELLOW)
lcd.fillTriangle(150, 100, 110, 140, 190, 140, ili9341.ILI9341_YELLOW)
lcd.drawRoundRect(20, 150, 50, 30, 10, ili9341.ILI9341_RED)
lcd.drawRoundRect(130, 150, 50, 30, 10, ili9341.ILI9341_RED)
lcd.fillRoundRect(75, 150, 50, 30, 10, ili9341.ILI9341_RED)

# Write some text
lcd.setCursor(0, 200)
lcd.setTextColor(ili9341.ILI9341_LIGHTGREY)
lcd.setTextWrap(True)
lcd.setTextSize(1)
lcd._print("Text 1\n")
lcd.setTextSize(2)
lcd._print("Text 2\n")
lcd.setTextSize(3)
lcd._print("Text 3\n")
lcd.setTextSize(4)
lcd._print("Text 4\n")

# Test screen rotation
for r in range(0, 4):
    lcd.setRotation(r)
    lcd.fillRect(0, 0, 5, 5, ili9341.ILI9341_WHITE)
    time.sleep(1)

# Invert colors, wait, then revert back
lcd.invertDisplay(True)
time.sleep(2)
lcd.invertDisplay(False)

# Don't forget to free up that memory!
del lcd