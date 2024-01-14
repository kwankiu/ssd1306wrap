# OLED Display Library for Micropython (ssd1306wrap)
A micropython library with font size support for 128x64 pixel ssd1306 oled display.

Based on [ssd1306.py](https://github.com/stlehmann/micropython-ssd1306/blob/master/ssd1306.py) from micropython module. 

Modifications based on [ssd1306big](https://github.com/nickpmulder/ssd1306big) by [Nick Mulder](https://github.com/nickpmulder)

![display demo gif](https://github.com/kwankiu/ssd1306wrap/blob/main/display_demo.GIF)

### Connecting the OLED to microcontroller:
- Rasberry Pi Pico (or RP2040) default I2C connections: SDA to GP8 and SCL to GP9.
- ESP32 can be configured to any pins unless occuiped by USB or UART (e.g. IO18 and 19 are occupied on ESP32-C3)
- Should works on ESP8266 as well but havent tested.

### Additional features to the original ssd1306 library:
- Added a function wrap() that display text that can set different font size. 
(wrap is based on a new, larger font was drawn using framebuffer lines by Nick Mulder.)

- Added a function bold_text() that display text in bold style
- Added a function bold_wrap() that display wrap() in bold style
- Added a function bold_wrap() that display wrap() in overlap (3D-like) style (overlap values are 0=no overlap,1=one overlap,2=two overlap(default))

 This library is open source, and can be used for free for any purpose. 

![example photo A through X](https://github.com/kwankiu/ssd1306wrap/blob/main/a-x.jpg)
![example photo Y, Z, numbers and punctuation](https://github.com/kwankiu/ssd1306wrap/blob/main/y-.jpg)
