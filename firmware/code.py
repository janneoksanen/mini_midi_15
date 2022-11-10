import time
import board
from digitalio import DigitalInOut, Direction, Pull
import usb_midi
import adafruit_midi

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

s1 = DigitalInOut(board.GP4)
s1.direction = Direction.INPUT
s1.pull = Pull.DOWN

s2 = DigitalInOut(board.GP7)
s2.direction = Direction.INPUT
s2.pull = Pull.DOWN

s3 = DigitalInOut(board.GP10)
s3.direction = Direction.INPUT
s3.pull = Pull.DOWN

s4 = DigitalInOut(board.GP13)
s4.direction = Direction.INPUT
s4.pull = Pull.DOWN

s5 = DigitalInOut(board.GP16)
s5.direction = Direction.INPUT
s5.pull = Pull.DOWN

s6 = DigitalInOut(board.GP3)
s6.direction = Direction.INPUT
s6.pull = Pull.DOWN

s7 = DigitalInOut(board.GP6)
s7.direction = Direction.INPUT
s7.pull = Pull.DOWN

s8 = DigitalInOut(board.GP9)
s8.direction = Direction.INPUT
s8.pull = Pull.DOWN

s9 = DigitalInOut(board.GP12)
s9.direction = Direction.INPUT
s9.pull = Pull.DOWN

s10 = DigitalInOut(board.GP15)
s10.direction = Direction.INPUT
s10.pull = Pull.DOWN

s11 = DigitalInOut(board.GP2)
s11.direction = Direction.INPUT
s11.pull = Pull.DOWN

s12 = DigitalInOut(board.GP5)
s12.direction = Direction.INPUT
s12.pull = Pull.DOWN

s13 = DigitalInOut(board.GP8)
s13.direction = Direction.INPUT
s13.pull = Pull.DOWN

s14 = DigitalInOut(board.GP11)
s14.direction = Direction.INPUT
s14.pull = Pull.DOWN

s15 = DigitalInOut(board.GP14)
s15.direction = Direction.INPUT
s15.pull = Pull.DOWN


USB_MIDI_channel = 1  # pick your USB MIDI out channel here, 1-16
usb_midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=USB_MIDI_channel - 1)
from adafruit_midi.program_change import ProgramChange
from adafruit_midi.control_change import ControlChange

debounce_delay = 0.3 # seconds

# set the led on by default
led.value = True

while True:
    if s1.value:
        led.value = False
        usb_midi.send(ProgramChange(1))
        time.sleep(debounce_delay)
        led.value = True
    if s2.value:
        led.value = False
        usb_midi.send(ProgramChange(2))
        time.sleep(debounce_delay)
        led.value = True
    if s3.value:
        led.value = False
        usb_midi.send(ProgramChange(3))
        time.sleep(debounce_delay)
        led.value = True
    if s4.value:
        led.value = False
        usb_midi.send(ProgramChange(4))
        time.sleep(debounce_delay)
        led.value = True
    if s5.value:
        led.value = False
        usb_midi.send(ProgramChange(5))
        time.sleep(debounce_delay)
        led.value = True
    if s6.value:
        led.value = False
        usb_midi.send(ControlChange(1,1))
        time.sleep(debounce_delay)
        led.value = True
    if s7.value:
        led.value = False
        usb_midi.send(ControlChange(2,2))
        time.sleep(debounce_delay)
        led.value = True
    if s8.value:
        led.value = False
        usb_midi.send(ControlChange(3,3))
        time.sleep(debounce_delay)
        led.value = True
    if s9.value:
        led.value = False
        usb_midi.send(ControlChange(4,4))
        time.sleep(debounce_delay)
        led.value = True
    if s10.value:
        led.value = False
        usb_midi.send(ControlChange(5,5))
        time.sleep(debounce_delay)
        led.value = True
    if s11.value:
        led.value = False
        usb_midi.send(ControlChange(6,6))
        time.sleep(debounce_delay)
        led.value = True
    if s12.value:
        led.value = False
        usb_midi.send(ControlChange(7,7))
        time.sleep(debounce_delay)
        led.value = True
    if s13.value:
        led.value = False
        usb_midi.send(ControlChange(8,8))
        time.sleep(debounce_delay)
        led.value = True
    if s14.value:
        led.value = False
        usb_midi.send(ControlChange(9,9))
        time.sleep(debounce_delay)
        led.value = True
    if s15.value:
        led.value = False
        usb_midi.send(ControlChange(10,10))
        time.sleep(debounce_delay)
        led.value = True
