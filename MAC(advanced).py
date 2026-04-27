# Deprecated: Use mac_tool.py instead

# Version (0.2) Advanced Version
""" Works with all systems """
import os
from random import randint
print("Type 'z' to check your network interface")
begin=input("1. enp3s0\n2. wlp2s0\n$ ")
a=str(randint(1000, 9999))
b=str(randint(1000, 9999))
c=str(randint(10, 99 ))
e=(f"00:{a[0]+a[1]}:{b[2:]}:{b[0]+b[1]}:{a[2:]}:{c}") #RANDOM MAC ADDRESS
if begin=="1":
	de="sudo ip link set dev enp3s0 down" #DISABLES WLP2S0
	ce=m=(f"sudo ip link set dev enp3s0 address {e}") #CHANGES MAC ADDRESS TO RANDOM
	ee="sudo ip link set dev enp3s0 up" #ENABLES WLP2S0
	os.system(de)
	os.system(ce)
	os.system(ee)
elif begin=="2":
	de="sudo ip link set dev wlp2s0 down" #DISABLES WLP2S0
	ce=m=(f"sudo ip link set dev wlp2s0 address {e}") #CHANGES MAC ADDRESS TO RANDOM
	ee="sudo ip link set dev wlp2s0 up" #ENABLES WLP2S0
	os.system(de)
	os.system(ce)
	os.system(ee)
elif begin=="z":
	os.system("ip a")
else:
	print("""\t\t\t).   .( \n\t\t\t   | \n\t\t\t  ---\nNO INTERFACE FOUND, Please check your by pressing 'z' key\nis 'ip' installed in your system ?""")
	
