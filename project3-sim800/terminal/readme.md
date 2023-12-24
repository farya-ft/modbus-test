
# Work with SIM800 by terminal

Open terminal:

	sudo picocom /dev/ttyUSB0 -b 9600

## step1

Check health status:

	AT
	
If you see OK in reply, then:

## step2 send SMS

For Set SMS Text Mode:

	AT+CMGF=1
	
If you see OK:

	AT+CMGS="+491795228587"
	
Then you should see > , else, try again.

If you see >, write your message, then press CTRL+Z



	
