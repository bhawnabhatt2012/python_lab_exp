import threading,time
import os
import re


def pingNetwork(threadName,ipAddr):
    f=os.popen("ping the ip"+ipAddr)
    for line in f.readlines():
        if re.search("(.*)received=4(.*)",line):
            print(ipAddr,"ACTIVE")
        else:
            print(ipAddr,'INACTIVE')


no_of_ip_addr=int(input("enter the number of IP addresses which is to be entered:-"))
for i in range (no_of_ip_addr):
    ip_addr=input("enter the ip address"+str(i+1)+":")
    t=threading.Thread(target=pingNetwork,args=("thread"+str(i+1),ip_addr))
    t.start()
    time.sleep(1)