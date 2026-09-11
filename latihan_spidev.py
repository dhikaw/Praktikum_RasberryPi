import spidev
import time
spi = spidev.SpiDev()
spi.open(0, 1)
try:
while True:
resp = spi.xfer2([0xAA])
time.sleep(1)
print("spi out: " + str(resp))
except KeyboardInterrupt:
spi.close()