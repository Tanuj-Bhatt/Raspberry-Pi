# Import the required libraries
import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

# Define the Morse code dictionary
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/'
}

# Define a function to convert text to Morse code
def text_to_morse(text):
    morse = ''
    for char in text.upper():
        if char in morse_code:
            morse += morse_code[char] + ' '
    return morse

# Define the function to blink the LED
def blink_led(morse):
    for char in morse:
        if char == '.':
            GPIO.output(18, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(18, GPIO.LOW)
            time.sleep(0.5)
        elif char == '-':
            GPIO.output(18, GPIO.HIGH)
            time.sleep(1.5)
            GPIO.output(18, GPIO.LOW)
            time.sleep(0.5)
        elif char == ' ':
            time.sleep(1.5)
        elif char == '/':
            time.sleep(3.0)

# Define the main function
def main():
    try:
        while True:
            text = input("Enter a message: ")
            morse = text_to_morse(text)
            print(morse)
            blink_led(morse)
    except KeyboardInterrupt:
        print("Program interrupted")
    finally:
        GPIO.cleanup()

# Run the main function
if __name__ == '__main__':
    main()
