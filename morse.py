import RPi.GPIO as GPIO
import time

Pin=8
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Pin,GPIO.OUT)


MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def dot():
  GPIO.output(Pin,1)
  time.sleep(0.2)
  GPIO.output(Pin,0)
  time.sleep(0.2)

def dash():
  GPIO.output(Pin,1)
  time.sleep(0.5)
  GPIO.output(Pin,0)
  time.sleep(0.2)

def send_signal(text):
    for letter in text:
        print(letter)
        for symbol in MORSE_CODE_DICT[letter.upper()]:
            if symbol == '-':
                print("dash")
                dash()
            elif symbol == '.':
                print("dot")
                dot()
            else:
                time.sleep(0.2)
        time.sleep(0.2)
if __name__=='__main__':
    input = "exterminated"
    send_signal(input)
