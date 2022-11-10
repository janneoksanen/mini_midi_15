Files included:

adafruit-circuitpython-raspberry_pi_pico-en_US-7.3.3.uf2

	A slightly modified version of Adafruit Circuitpython.
	Only difference is the name of the USB midi device.
	
adafuit_midi

	Adafruid midi library. Added here for convenience so
	that you don't have to download the whole library pack.

Adafuit CircuitPython is published under the MIT licence.
Read licence details here: 
https://docs.circuitpython.org/en/latest/docs/LICENSE.html

code.py

	The actual program that runs the board. By default MIDI
	channel is set to 1. Buttons S1 through S5 send program
	change messages 1 through 5. Buttons 6 through 15 send
	control change messages 1 through 10 with corresponding
	values 1 through 10. If you know any amount of programming
	you should have no problems customizing the code to suit
	your needs.
	
	Check out the MIDI library documentation here:
	https://docs.circuitpython.org/projects/midi/en/latest/api.html#

Installation instructions:

	1. Plug the board into USB
	2. Copy adafruit-circuitpython-raspberry_pi_pico-en_US-7.3.3.uf2
		to the root of the USB drive that appears. The USB drive will
		go away briefly while the Pico installs CircuitPython. It
		will then reappear with a directory called lib in the root
	3. Copy adafuit_midi directory with all its contents inside lib
	4. Replace the code.py file in the root of the USB drive with 
		the code.py provided by me.
	Your MiniMidi 15 is now ready to rock (or pop I don't judge)


Happy hacking, 
Janne Oksanen