import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
coil_A_1_pin=22
coil_A_2_pin=24
coil_B_1_pin=26
coil_B_2_pin=28
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)
forward_seq = ['1010','0110','0101','1001']
reverse_seq = list(forward_seq)
reverse_seq.reverse()
def forward(delay,steps):
for i in range(steps):
for step in forward_seq:
print(step)
set_step(step)
time.sleep(delay)
def backwards(delay,steps):
for i in range(steps):
for step in reverse_seq:
print(step)
set_step(step)
time.sleep(delay)
def set_step(step):
GPIO.output(coil_A_1_pin,step[0] =='1')
GPIO.output(coil_A_2_pin,step[1] =='1')
GPIO.output(coil_B_1_pin,step[2] =='1')
GPIO.output(coil_B_2_pin,step[3] =='1')
A = True
while(A==True):
choice = input("Enter your choice - Forward[F/f] - Reverse [R/r] - Stop[S/s]")
if(choice == 'F' or choice == 'f'):
print("Forward Motion")
forward(1,2)
set_step("0000")
time.sleep(5)
elif(choice == 'R' or choice == 'r'):
print("Reverse Motion")
backwards(1,2)
set_step("0000")
time.sleep(5)
elif(choice == 'S' or choice == 's'):
A=False
print("HALT")
time.sleep(5)
break
