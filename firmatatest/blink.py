import pyfirmata

PIN = 13 # Pin 12 is used
DELAY = 2 # A 2 seconds delay

# Adjust that the port match your system, see samples below:
# On Linux: /dev/tty.usbserial-A6008rIF, /dev/ttyACM0, 
# On Windows: \\.\COM1, \\.\COM2
PORT = '/dev/ttyACM0'

# Creates a new board 
board = pyfirmata.Arduino(PORT)

# Loop for blinking the led
while True:
    board.digital[PIN].write(1) # Set the LED pin to 1 (HIGH)
    board.pass_time(DELAY)
    board.digital[PIN].write(0) # Set the LED pin to 0 (LOW)
    board.pass_time(DELAY)
