# spitest.py
# A brief demonstration of the Raspberry Pi SPI interface, using the Sparkfun
# Pi Wedge breakout board and a SparkFun Serial 7 Segment display:
# https://www.sparkfun.com/products/11629
import os
import time
import spidev

# We only have SPI bus 0 available to us on the Pi
bus = 0

#Device is the chip select pin. Set to 0 or 1, depending on the connections
device = 1

# Enable SPI
spi = spidev.SpiDev()

# Open a connection to a specific bus and device (chip select pin)
spi.open(bus, device)

# Set SPI speed and mode
spi.max_speed_hz = 50000
spi.mode = 1


time.sleep(5)

# Turn on one segment of each character to show that we can
# address all of the segments

while 1:

    # The last character
    result = spi.readbytes(2)
    print(result[1]+result[0]*2**8)

    # print(result)

    # Pause so we can see them
    time.sleep(0.1)

spi.close()
