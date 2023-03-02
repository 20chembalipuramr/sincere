from time import sleep
import sys

def pprint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    sleep(0.08)

def ppprint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    sleep(0.042)