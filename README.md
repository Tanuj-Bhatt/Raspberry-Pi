# Raspberry-Pi
How it works:
Morse Code Dictionary: The morse_code dictionary translates letters and numbers into Morse code.
Text to Morse Conversion: The text_to_morse function converts a given string to Morse code.
Blinking LED: The blink_led function takes the Morse code and blinks the LED accordingly:
A dot (.) is a short blink.
A dash (-) is a long blink.
A space between words ('/') pauses for a longer duration.
Main Loop: The main() function runs continuously, accepting user input and converting it into Morse code, which is then blinked out via the LED.
GPIO Setup:
GPIO Pin 18 is used for the LED output.
This code will keep running until you manually stop it (with a KeyboardInterrupt), and it ensures the GPIO pins are cleaned up afterward.# Raspberry-Pi
# Raspberry-Pi
