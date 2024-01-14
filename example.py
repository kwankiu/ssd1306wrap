from machine import Pin, SoftI2C
import time
import ssd1306

# Set I2C on IO0 and IO1
i2c = SoftI2C(sda=Pin(1), scl=Pin(0))

# Using default address 0x3C
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Fill White Background
display.fill(1)

# Draw a outlined rectangle
display.fill_rect(4, 4, 32, 32, 0)
display.fill_rect(4, 8, 24, 16, 1)

# Display normal text
display.text('Hello World', 4, 12, 0)

# Update Display
display.show()
    
# Main loop
while True:
    
    # Wait 2 seconds
    time.sleep(2)

    # Clear Background
    display.clear()

    # Display text with default font size (2)
    display.wrap("ABC", 28, 8)
  
    # Display text with font size 3
    display.wrap("ABC", 28, 24, 3)

    # Display bold text
    display.bold_text("1234", 28, 48, 1)

    # Draw some vertical lines
    display.vline(9, 8, 40, 1)
    display.vline(16, 2, 40, 1)
    display.vline(23, 8, 40, 1)
    display.vline(105, 8, 40, 1)
    display.vline(112, 2, 40, 1)
    display.vline(119, 8, 40, 1)

    # Update Display
    display.show()

    # Wait 2 seconds
    time.sleep(2)

    # Fill White Background
    display.fill(1)

    # Display a text in white background with default font size 4
    display.wrap("HELLO", 16, 20, 4, 0)

    # Update Display
    display.show()

